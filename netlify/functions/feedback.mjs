const attempts = new Map();
const WINDOW_MS = 10 * 60 * 1000;
const MAX_ATTEMPTS = 5;

function response(statusCode, body) {
  return new Response(JSON.stringify(body), {
    status: statusCode,
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
}

function clean(value, maxLength) {
  return String(value || '').replace(/[\u0000-\u001f\u007f]/g, ' ').trim().slice(0, maxLength);
}

export default async request => {
  if (request.method !== 'POST') return response(405, { error: 'Phương thức không được hỗ trợ.' });

  const botToken = process.env.TELEGRAM_TOKEN_membership || process.env.TELEGRAM_BOT_TOKEN_membership;
  const chatId = process.env.TELEGRAM_CHAT_ID_membership;
  if (!botToken || !chatId) {
    console.error('Missing Telegram environment variables.');
    return response(503, { error: 'Chức năng góp ý chưa được cấu hình.' });
  }

  const contentLength = Number(request.headers.get('content-length') || 0);
  if (contentLength > 10000) return response(413, { error: 'Nội dung quá lớn.' });

  const ip = request.headers.get('x-nf-client-connection-ip') || 'unknown';
  const now = Date.now();
  const recent = (attempts.get(ip) || []).filter(time => now - time < WINDOW_MS);
  if (recent.length >= MAX_ATTEMPTS) return response(429, { error: 'Bạn đã gửi quá nhiều lần. Vui lòng thử lại sau.' });

  let body;
  try {
    body = await request.json();
  } catch {
    return response(400, { error: 'Dữ liệu không hợp lệ.' });
  }
  if (body.website) return response(200, { ok: true });

  const name = clean(body.name, 80) || 'Ẩn danh';
  const message = clean(body.message, 1500);
  const page = clean(body.page, 300);
  if (message.length < 5) return response(400, { error: 'Nội dung góp ý quá ngắn.' });

  const text = [
    '💬 GÓP Ý KIIP5 APP',
    '',
    `👤 Người gửi: ${name}`,
    `📝 Nội dung:\n${message}`,
    page ? `🔗 Trang: ${page}` : '',
    `🕐 Thời gian: ${new Date().toISOString()}`,
  ].filter(Boolean).join('\n');

  try {
    const telegramResponse = await fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ chat_id: chatId, text, disable_web_page_preview: true }),
    });
    const telegramResult = await telegramResponse.json();
    if (!telegramResponse.ok || !telegramResult.ok) {
      console.error('Telegram API error:', telegramResult.description || telegramResponse.status);
      return response(502, { error: 'Chưa gửi được góp ý. Vui lòng thử lại.' });
    }
    recent.push(now);
    attempts.set(ip, recent);
    return response(200, { ok: true });
  } catch (error) {
    console.error('Telegram request failed:', error.message);
    return response(502, { error: 'Không thể kết nối dịch vụ nhận góp ý.' });
  }
};
