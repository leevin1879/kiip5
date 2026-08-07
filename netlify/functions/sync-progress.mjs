import { getStore } from '@netlify/blobs';
import { verifyToken } from './lib/auth.mjs';

function response(status, body) {
  return new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json; charset=utf-8' } });
}

function getToken(request) {
  const auth = request.headers.get('authorization') || '';
  return auth.startsWith('Bearer ') ? auth.slice(7) : '';
}

export default async request => {
  const secret = process.env.SESSION_SECRET;
  if (!secret) return response(503, { error: 'Chức năng đăng nhập chưa được cấu hình.' });

  const payload = verifyToken(getToken(request), secret);
  if (!payload) return response(401, { error: 'Phiên đăng nhập đã hết hạn. Vui lòng đăng nhập lại.' });

  const store = getStore('kiip5-progress');
  const key = `progress/${payload.u}`;

  if (request.method === 'GET') {
    const data = await store.get(key, { type: 'json' }).catch(() => null);
    return response(200, data || { stats: null, updatedAt: null });
  }

  if (request.method === 'POST') {
    const contentLength = Number(request.headers.get('content-length') || 0);
    if (contentLength > 200000) return response(413, { error: 'Dữ liệu quá lớn.' });
    let body;
    try {
      body = await request.json();
    } catch {
      return response(400, { error: 'Dữ liệu không hợp lệ.' });
    }
    const record = { stats: body.stats || {}, updatedAt: new Date().toISOString() };
    await store.setJSON(key, record);
    return response(200, { ok: true, updatedAt: record.updatedAt });
  }

  return response(405, { error: 'Phương thức không được hỗ trợ.' });
};
