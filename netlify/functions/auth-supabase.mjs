import { getStore } from '@netlify/blobs';
import { signToken } from './lib/auth.mjs';

const SUPABASE_URL = 'https://vemyaxemylxuayydebyw.supabase.co';
const SUPABASE_PUBLISHABLE_KEY = 'sb_publishable_ihsCaMOOobjz9AObV_l0Sw_gjgbDFHD';

function response(status, body) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
}

export default async request => {
  if (request.method !== 'POST') return response(405, { error: 'Phương thức không được hỗ trợ.' });

  const secret = process.env.SESSION_SECRET;
  if (!secret) return response(503, { error: 'Chức năng đăng nhập chưa được cấu hình.' });

  let body;
  try {
    body = await request.json();
  } catch {
    return response(400, { error: 'Dữ liệu không hợp lệ.' });
  }

  const accessToken = String(body.accessToken || '');
  if (!accessToken) return response(401, { error: 'Thiếu phiên đăng nhập Google.' });

  const userResponse = await fetch(`${SUPABASE_URL}/auth/v1/user`, {
    headers: {
      Authorization: `Bearer ${accessToken}`,
      apikey: SUPABASE_PUBLISHABLE_KEY,
    },
  });
  if (!userResponse.ok) return response(401, { error: 'Phiên đăng nhập Google không hợp lệ hoặc đã hết hạn.' });

  const user = await userResponse.json();
  if (!user.id || !user.email) return response(401, { error: 'Tài khoản Google không cung cấp đủ thông tin.' });

  const username = `google_${String(user.id).replace(/[^a-zA-Z0-9_-]/g, '')}`;
  const displayName = String(user.user_metadata?.full_name || user.user_metadata?.name || user.email)
    .trim()
    .slice(0, 60);
  const store = getStore('kiip5-users');
  const key = `users/${username}`;
  const existing = await store.get(key, { type: 'json' }).catch(() => null);
  if (!existing) {
    await store.setJSON(key, {
      username,
      displayName,
      email: String(user.email).slice(0, 254),
      role: 'user',
      provider: 'google',
      supabaseUserId: user.id,
      createdAt: new Date().toISOString(),
    });
  }

  const token = signToken({ u: username, r: 'user' }, secret);
  return response(200, { ok: true, token, username, displayName, role: 'user', provider: 'google' });
};
