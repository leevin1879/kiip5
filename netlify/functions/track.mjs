import { getStore } from '@netlify/blobs';

const attempts = new Map();
const WINDOW_MS = 60 * 1000;
const MAX_ATTEMPTS = 20;

function response(statusCode, body) {
  if (statusCode === 204) return new Response(null, { status: 204 });
  return new Response(JSON.stringify(body), {
    status: statusCode,
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
}

function clean(value, maxLength) {
  return String(value || '').replace(/[\x00-\x1f\x7f]/g, ' ').trim().slice(0, maxLength);
}

function pad(n) {
  return String(n).padStart(2, '0');
}

export default async (request, context) => {
  if (request.method !== 'POST') return response(405, { error: 'Phương thức không được hỗ trợ.' });

  const ip = request.headers.get('x-nf-client-connection-ip') || 'unknown';
  const now = Date.now();
  const recent = (attempts.get(ip) || []).filter(time => now - time < WINDOW_MS);
  if (recent.length >= MAX_ATTEMPTS) return response(204, {});

  let body = {};
  try {
    body = await request.json();
  } catch {
    body = {};
  }

  const page = clean(body.page, 200) || '/';
  const referrer = clean(body.referrer, 300);
  const userAgent = clean(request.headers.get('user-agent'), 300);
  const geo = context.geo || {};
  const ipKey = ip.replace(/[^a-zA-Z0-9.:_-]/g, '_') || 'unknown';

  const d = new Date();
  const date = `${d.getUTCFullYear()}-${pad(d.getUTCMonth() + 1)}-${pad(d.getUTCDate())}`;
  const time = `${pad(d.getUTCHours())}-${pad(d.getUTCMinutes())}-${pad(d.getUTCSeconds())}`;
  const rand = Math.random().toString(36).slice(2, 8);
  const key = `visits/${date}/${ipKey}/${time}-${rand}`;

  try {
    const store = getStore('kiip5-visits');
    await store.setJSON(key, {
      ts: d.toISOString(),
      ip,
      country: geo.country?.name || '',
      countryCode: geo.country?.code || '',
      city: geo.city || '',
      page,
      referrer,
      userAgent,
    });
    recent.push(now);
    attempts.set(ip, recent);
    return response(204, {});
  } catch (error) {
    console.error('Track write failed:', error.message);
    return response(204, {});
  }
};
