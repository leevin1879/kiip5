import { getStore } from '@netlify/blobs';
import { hashPassword, signToken, normalizeUsername, validUsername } from './lib/auth.mjs';

const attempts = new Map();
const WINDOW_MS = 10 * 60 * 1000;
const MAX_ATTEMPTS = 8;

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
  if (recent.length >= MAX_ATTEMPTS) return response(429, { error: 'Bạn thao tác quá nhiều lần. Vui lòng thử lại sau.' });
  recent.push(now);
  attempts.set(ip, recent);

  let body;
  try {
    body = await request.json();
  } catch {
    return response(400, { error: 'Dữ liệu không hợp lệ.' });
  }

  const username = normalizeUsername(body.username);
  const password = String(body.password || '');
  const displayName = String(body.displayName || '').trim().slice(0, 60) || username;

  if (!validUsername(username)) {
    return response(400, { error: 'Tên đăng nhập phải dài 3-20 ký tự, chỉ gồm chữ thường/số/gạch dưới.' });
  }
  if (password.length < 6) {
    return response(400, { error: 'Mật khẩu phải có ít nhất 6 ký tự.' });
  }
  const adminUsername = normalizeUsername(process.env.ADMIN_USERNAME || 'admin');

  const store = getStore('kiip5-users');
  const existing = await store.get(`users/${username}`, { type: 'json' }).catch(() => null);
  if (existing) return response(409, { error: 'Tên đăng nhập đã được sử dụng.' });

  const role = username === adminUsername ? 'admin' : 'user';
  const record = {
    username,
    displayName,
    passwordHash: hashPassword(password),
    role,
    createdAt: new Date().toISOString(),
  };
  await store.setJSON(`users/${username}`, record);

  const token = signToken({ u: username, r: role }, secret);
  return response(200, { ok: true, token, username, displayName, role });
};
