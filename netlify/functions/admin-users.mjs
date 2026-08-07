import { getStore } from '@netlify/blobs';
import { verifyToken } from './lib/auth.mjs';

function response(status, body) {
  return new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json; charset=utf-8' } });
}

function summarizeStats(stats) {
  let seen = 0;
  let correct = 0;
  Object.values(stats || {}).forEach(setStats => {
    Object.values(setStats || {}).forEach(q => {
      seen += q.seen || 0;
      correct += q.correct || 0;
    });
  });
  return { seen, correct, pct: seen ? Math.round((correct / seen) * 100) : 0 };
}

export default async request => {
  const adminKey = process.env.ADMIN_STATS_KEY;
  const url = new URL(request.url);
  const providedKey = url.searchParams.get('key') || request.headers.get('x-admin-key') || '';
  const auth = request.headers.get('authorization') || '';
  const token = auth.startsWith('Bearer ') ? auth.slice(7) : '';
  const payload = process.env.SESSION_SECRET ? verifyToken(token, process.env.SESSION_SECRET) : null;
  const authorized = payload?.r === 'admin' || (adminKey && providedKey === adminKey);
  if (!authorized) return response(401, { error: 'Bạn không có quyền quản trị.' });

  const usersStore = getStore('kiip5-users');
  const progressStore = getStore('kiip5-progress');

  let entries = [];
  let cursor;
  try {
    do {
      const page = await usersStore.list({ prefix: 'users/', cursor, paginate: true });
      entries = entries.concat(page.blobs || []);
      cursor = page.cursor;
    } while (cursor && entries.length < 20000);
  } catch (error) {
    console.error('User list failed:', error.message);
    return response(502, { error: 'Không thể đọc danh sách người dùng.' });
  }

  const result = [];
  for (const entry of entries) {
    const record = await usersStore.get(entry.key, { type: 'json' }).catch(() => null);
    if (!record) continue;
    const progress = await progressStore.get(`progress/${record.username}`, { type: 'json' }).catch(() => null);
    const summary = summarizeStats(progress?.stats);
    result.push({
      username: record.username,
      displayName: record.displayName,
      createdAt: record.createdAt,
      updatedAt: progress?.updatedAt || null,
      ...summary,
    });
  }

  result.sort((a, b) => (b.updatedAt || '').localeCompare(a.updatedAt || ''));
  return response(200, { users: result });
};
