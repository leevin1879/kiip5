import { getStore } from '@netlify/blobs';
import { verifyToken } from './lib/auth.mjs';

function response(statusCode, body) {
  return new Response(JSON.stringify(body), {
    status: statusCode,
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
}

function parseKey(key) {
  // visits/{date}/{ipKey}/{time}-{rand}
  const parts = key.split('/');
  const date = parts[1] || '';
  const ipKey = parts[2] || '';
  const time = parts[3] || '';
  return { date, ipKey, time, chronologicalKey: `${date}/${time}` };
}

function decodeCursor(value) {
  if (!value) return 0;
  try {
    const parsed = JSON.parse(Buffer.from(value, 'base64url').toString('utf8'));
    return Number.isInteger(parsed.offset) && parsed.offset >= 0 ? parsed.offset : 0;
  } catch {
    return 0;
  }
}

function encodeCursor(offset) {
  return Buffer.from(JSON.stringify({ offset })).toString('base64url');
}

export default async request => {
  const adminKey = process.env.ADMIN_STATS_KEY;
  const url = new URL(request.url);
  const pageOffset = decodeCursor(url.searchParams.get('cursor'));
  const providedKey = url.searchParams.get('key') || request.headers.get('x-admin-key') || '';
  const auth = request.headers.get('authorization') || '';
  const token = auth.startsWith('Bearer ') ? auth.slice(7) : '';
  const payload = process.env.SESSION_SECRET ? verifyToken(token, process.env.SESSION_SECRET) : null;
  const authorized = payload?.r === 'admin' || (adminKey && providedKey === adminKey);
  if (!authorized) return response(401, { error: 'Bạn không có quyền quản trị.' });

  const store = getStore('kiip5-visits');

  let entries = [];
  try {
    const result = await store.list({ prefix: 'visits/' });
    entries = (result.blobs || []).slice(0, 50000);
  } catch (error) {
    console.error('Blob list failed:', error.message);
    return response(502, { error: 'Không thể đọc dữ liệu thống kê.' });
  }

  const uniqueIps = new Set();
  const perDayIps = new Map();
  entries.forEach(entry => {
    const { date, ipKey } = parseKey(entry.key);
    if (ipKey) uniqueIps.add(ipKey);
    if (date && ipKey) {
      if (!perDayIps.has(date)) perDayIps.set(date, new Set());
      perDayIps.get(date).add(ipKey);
    }
  });

  const perDayList = Array.from(perDayIps.entries())
    .map(([date, ips]) => ({ date, count: ips.size }))
    .sort((a, b) => (a.date < b.date ? 1 : -1))
    .slice(0, 30);

  const todayKey = new Date().toISOString().slice(0, 10);

  const recentKeys = entries
    .map(entry => entry.key)
    .sort((a, b) => {
      const aKey = parseKey(a).chronologicalKey;
      const bKey = parseKey(b).chronologicalKey;
      return bKey.localeCompare(aKey);
    });

  const uniqueRecentKeys = [];
  const recentIpKeys = new Set();
  for (const key of recentKeys) {
    const { ipKey } = parseKey(key);
    if (!ipKey || recentIpKeys.has(ipKey)) continue;
    uniqueRecentKeys.push(key);
    recentIpKeys.add(ipKey);
  }

  const pageKeys = uniqueRecentKeys.slice(pageOffset, pageOffset + 20);
  const pageData = await Promise.all(pageKeys.map(key => store.get(key, { type: 'json' }).catch(() => null)));
  const recent = pageData
    .filter(Boolean)
    .sort((a, b) => Date.parse(b.ts || 0) - Date.parse(a.ts || 0));
  const nextOffset = pageOffset + pageKeys.length;
  const nextCursor = nextOffset < uniqueRecentKeys.length ? encodeCursor(nextOffset) : null;

  return response(200, {
    total: uniqueIps.size,
    totalVisits: entries.length,
    uniqueIps: uniqueIps.size,
    today: perDayIps.get(todayKey)?.size || 0,
    perDay: perDayList,
    recent,
    nextCursor,
  });
};
