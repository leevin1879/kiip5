function response(status, body) {
  return new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json; charset=utf-8' } });
}

export default async request => {
  if (request.method !== 'POST') return response(405, { error: 'Phương thức không được hỗ trợ.' });
  return response(410, { error: 'Đăng ký mới yêu cầu email xác nhận. Vui lòng đăng ký trên ứng dụng.' });
};
