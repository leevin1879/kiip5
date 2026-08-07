import { getStore } from '@netlify/blobs';
import { verifyPassword, signToken, normalizeUsername } from './lib/auth.mjs';

const attempts = new Map();
const WINDOW_MS = 10 * 60 * 1000;
const MAX_ATTEMPTS = 10;

function response(status, body) {
  return new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json; charset=utf-8' } });
}

export default async request => {
  if (request.method !== 'POST') return response(405, { error: 'Phương thức không được hỗ trợ.' });

  const secret = process.env.SESSION_SECRET;
  if (!secret) return response(503, { error: 'Chức năng đăng nhập chưa được cấu hình.' });

  const ip = request.headers.get('x-nf-client-connection-ip') || 'unknown';
  const now = Date.now();
  const recent = (attempts.get(ip) || []).filter(t => now - t < WINDOW_MS);
  if (recent.length >= MAX_ATTEMPTS) return response(429, { error: 'Bạn đăng nhập sai quá nhiều lần. Vui lòng thử lại sau.' });

  let body;
  try {
    body = await request.json();
  } catch {
    return response(400, { error: 'Dữ liệu không hợp lệ.' });
  }

  const username = normalizeUsername(body.username);
  const password = String(body.password || '');

  const store = getStore('kiip5-users');
  const record = await store.get(`users/${username}`, { type: 'json' }).catch(() => null);

  if (!record || !verifyPassword(password, record.passwordHash)) {
    recent.push(now);
    attempts.set(ip, recent);
    return response(401, { error: 'Sai tên đăng nhập hoặc mật khẩu.' });
  }

  attempts.delete(ip);

  const adminUsername = normalizeUsername(process.env.ADMIN_USERNAME || 'admin');
  const role = record.role === 'admin' || username === adminUsername ? 'admin' : 'user';
  const token = signToken({ u: username, r: role }, secret);
  return response(200, { ok: true, token, username, displayName: record.displayName || username, role });
};
