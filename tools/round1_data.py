# -*- coding: utf-8 -*-
# Question set built from "한국어_모의고사_(5단계_1회)_—_Giải_thích_chi_tiết.docx".
# Same situation as round4/round2: the source only gives full 4-option text
# for some questions. Where it doesn't, Claude reconstructed plausible
# distractors from the reasoning already present in the source; those are
# flagged options_source="reconstructed" and noted in the explanation.

QUESTIONS = [
    dict(num=1, correct='B', options_source='docx',
         stem='우리 아이는 ( )이라서 혼자 조용히 있는 것을 좋아한다.',
         options=[('A', '긍정적'), ('B', '내성적'), ('C', '외향적'), ('D', '적극적')],
         explanation=(
             'Người thích ở một mình yên tĩnh là người có tính cách hướng nội (내성적) — khớp với B.\n'
             'A 긍정적(tích cực), C 외향적(hướng ngoại — trái nghĩa hoàn toàn), D 적극적(chủ động) đều không hợp với "thích '
             'ở một mình yên tĩnh".'
         )),
    dict(num=2, correct='B', options_source='docx',
         stem='싱크대가 ( ) 물이 안 내려가요.',
         options=[('A', '새서'), ('B', '막혀서'), ('C', '열려서'), ('D', '쌓여서')],
         explanation=(
             'Nước bồn rửa bát không chảy xuống được là do bị TẮC (막히다) — khớp với B.\n'
             'A 새서(vì bị rò rỉ) thì nước sẽ CHẢY RA ngoài chứ không phải không chảy xuống được. C 열려서(vì bị mở) và D '
             '쌓여서(vì bị tích tụ) đều không hợp nghĩa "nước không thoát được".'
         )),
    dict(num=3, correct='B', options_source='docx',
         stem='연말에는 한 해를 돌아보며 회사 동료들이나 가족들과 모여서 ( )를 한다.',
         options=[('A', '동창회'), ('B', '송년회'), ('C', '반상회'), ('D', '야유회')],
         explanation=(
             'Cuối năm (연말) nhìn lại một năm đã qua chính là ý nghĩa của tiệc tất niên (송년회) — khớp với B.\n'
             'A 동창회(họp lớp cũ), C 반상회(họp tổ dân phố), D 야유회(dã ngoại) đều không gắn với dịp cuối năm được nêu.'
         )),
    dict(num=4, correct='C', options_source='reconstructed',
         stem='나는 시간이 있으면 예쁜 풍경 사진을 찍어서 블로그에 ( ).',
         options=[('A', '내린다'), ('B', '지운다'), ('C', '올린다'), ('D', '숨긴다')],
         explanation=(
             '"블로그에 올리다" nghĩa là đăng bài/ảnh lên blog — khớp với C.\n'
             'A 내린다(tải xuống/hạ xuống) mang nghĩa ngược lại. B 지운다(xóa) và D 숨긴다(giấu đi) đều không hợp với hành '
             'động chụp ảnh đẹp rồi CHIA SẺ lên blog.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, B, D là do Claude tự dựng lại.'
         )),
    dict(num=5, correct='B', options_source='reconstructed',
         stem='가: 머리를 어떻게 해 드릴까요?\n나: 여름이니까 좀 ( ) 잘라 주세요.',
         options=[('A', '길게'), ('B', '짧게'), ('C', '예쁘게'), ('D', '이상하게')],
         explanation=(
             '"짧게 자르다" (cắt ngắn) hợp lý vì trời đang mùa hè nóng nực — khớp với B. "-게" ở đây tạo phó từ chỉ cách '
             'thức cắt tóc.\n'
             'A 길게(dài) mang nghĩa ngược lại với lý do "mùa hè". C 예쁘게(đẹp) và D 이상하게(kỳ lạ) không liên quan đến '
             'lý do thời tiết được nêu.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, C, D là do Claude tự dựng lại.'
         )),
    dict(num=6, correct='A', options_source='docx',
         stem='가: 어릴 때 어떤 음식을 좋아했어요?\n나: 초콜릿과 같은 단 음식을 자주 ( ).',
         options=[('A', '먹곤 했어요'), ('B', '먹기 마련이에요'), ('C', '먹으려던 참이에요'), ('D', '먹었을지도 몰라요')],
         explanation=(
             'Cấu trúc "-곤 하다" diễn tả một thói quen lặp lại trong quá khứ — "hồi nhỏ hay ăn đồ ngọt" — khớp với A.\n'
             'B 먹기 마련이에요(đương nhiên là ăn — quy luật chung, không phải hồi tưởng thói quen cá nhân), C 먹으려던 '
             '참이에요(vừa định ăn — thì không khớp), D 먹었을지도 몰라요(không biết chừng đã ăn — phỏng đoán, không hợp '
             'câu hỏi về thói quen đã biết rõ) đều sai.'
         )),
    dict(num=7, correct='D', options_source='reconstructed',
         stem='가: 의사 선생님께서 뭐라고 하셨어요?\n나: 감기가 심하니까 약을 먹고 푹 ( ) 하셨어요.',
         options=[('A', '쉰다고'), ('B', '쉬냐고'), ('C', '쉬었다고'), ('D', '쉬라고')],
         explanation=(
             'Câu trần thuật gián tiếp của câu MỆNH LỆNH: bác sĩ bảo "쉬세요" (hãy nghỉ ngơi) → "쉬라고 하셨다" — khớp với D.\n'
             'A 쉰다고(nói là sẽ nghỉ) và C 쉬었다고(nói là đã nghỉ) là câu gián tiếp của câu TRẦN THUẬT, không phải mệnh '
             'lệnh. B 쉬냐고(hỏi là có nghỉ không) là câu gián tiếp của câu HỎI — cả 3 đều sai vì bác sĩ đang RA CHỈ THỊ, '
             'không phải kể chuyện hay hỏi.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, B, C là do Claude tự dựng lại.'
         )),
    dict(num=8, correct='D', options_source='reconstructed',
         stem='가: 어제 본 영화는 어땠어요?\n나: 너무 재미있어서 배꼽이 ( ) 웃었어요.',
         options=[('A', '빠지지 않게'), ('B', '빠질까 봐'), ('C', '빠지는 대신'), ('D', '빠질 정도로')],
         explanation=(
             'Quán dụng ngữ "배꼽이 빠지다" chỉ việc cười rất to — "cười đến mức rớt rốn" dùng cấu trúc "-ㄹ 정도로" (đến '
             'mức...) — khớp với D.\n'
             'A 빠지지 않게(để không rớt), B 빠질까 봐(sợ sẽ rớt), C 빠지는 대신(thay vì rớt) đều không diễn tả đúng mức độ '
             'cười to mà câu cần.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, B, C là do Claude tự dựng lại.'
         )),
    dict(num=9, correct='B', options_source='reconstructed',
         stem='친구가 기다리고 있어서 수업이 끝나자마자 ( ).',
         options=[('A', '천천히 가도 돼요'), ('B', '빨리 가야 돼요'), ('C', '가지 않아도 돼요'), ('D', '가면 안 돼요')],
         explanation=(
             'Bạn đang đợi nên ngay khi tan học (끝나자마자) thì "phải" đi nhanh — khớp với B.\n'
             'A 천천히 가도 돼요(có thể đi từ từ) mang nghĩa ngược lại với việc bạn đang chờ. C 가지 않아도 돼요(không cần đi '
             'cũng được) và D 가면 안 돼요(không được đi) đều mâu thuẫn với lý do "bạn đang đợi".\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, C, D là do Claude tự dựng lại.'
         )),
    dict(num=10, correct='A', options_source='reconstructed',
         stem='극장 앞에 사람이 많은 걸 보니 ( ).',
         options=[
             ('A', '저 영화가 재미있나 봐요'),
             ('B', '저 영화가 재미없을 리가 없어요'),
             ('C', '저 영화를 꼭 봐야 해요'),
             ('D', '저 영화가 곧 끝날 거예요'),
         ],
         explanation=(
             'Cấu trúc "-나 보다" dùng để phỏng đoán dựa trên điều nhìn thấy — thấy rạp đông người nên suy đoán "có vẻ '
             'phim đó hay" — khớp với A.\n'
             'B "-ㄹ 리가 없다"(không thể nào) là cấu trúc khẳng định chắc chắn, không hợp với ngữ cảnh phỏng đoán nhẹ '
             'nhàng. C(nhất định phải xem) và D(sắp kết thúc) không diễn tả đúng ý suy đoán từ hiện tượng quan sát được.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — B, C, D là do Claude tự dựng lại.'
         )),
    dict(num=11, correct='A', options_source='reconstructed',
         stem='대기업에 지원하다 / 열심히 준비하고 있다',
         options=[
             ('A', '대기업에 지원하기 위해서 열심히 준비하고 있어요.'),
             ('B', '대기업에 지원하는 대신에 열심히 준비하고 있어요.'),
             ('C', '대기업에 지원하다가 열심히 준비하고 있어요.'),
             ('D', '대기업에 지원하도록 열심히 준비하고 있어요.'),
         ],
         explanation=(
             'Nối 2 vế bằng cấu trúc chỉ mục đích "-기 위해서" (để...) — "đang chuẩn bị chăm chỉ ĐỂ ứng tuyển vào công ty '
             'lớn" — khớp với A.\n'
             'B "-는 대신에"(thay vì) sai quan hệ mục đích. C "-다가"(đang làm thì bị ngắt) sai ngữ pháp/nghĩa. D "-도록"(để '
             'cho) không hợp chủ thể của câu.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — B, C, D là do Claude tự dựng lại.'
         )),
    dict(num=12, correct='C', options_source='reconstructed',
         stem='주말에 근무하다 / 평일에 쉬다 / 괜찮다',
         options=[
             ('A', '주말에 근무하기 위해서 평일에 쉬니까 괜찮다.'),
             ('B', '주말에 근무하지만 평일에 쉬어도 괜찮다.'),
             ('C', '주말에 근무하는 대신에 평일에 쉬니까 괜찮다.'),
             ('D', '주말에 근무하도록 평일에 쉬니까 괜찮다.'),
         ],
         explanation=(
             'Cấu trúc "-는 대신에" (thay vì, bù lại) — bù lại việc phải làm cuối tuần là được nghỉ ngày thường, nên ổn — '
             'khớp với C.\n'
             'A "-기 위해서"(để) sai quan hệ nhân quả/mục đích. B đổi cấu trúc thành "-지만"(nhưng) làm mất đi ý nghĩa "bù '
             'lại". D "-도록"(để cho) sai nghĩa.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, B, D là do Claude tự dựng lại.'
         )),
    dict(num=13, correct='B', options_source='reconstructed',
         stem=(
             '[Ngữ cảnh (tóm tắt, không phải nguyên văn — bài đọc gốc không có trong tài liệu nguồn): đoạn văn nói về '
             '"인맥 다이어트" (giảm bớt/sắp xếp lại mạng lưới quan hệ để tránh áp lực từ quá nhiều mối quan hệ)]\n'
             '( )에 알맞은 것을 고르시오.'
         ),
         options=[
             ('A', '새로운 친구를 많이 사귀는 것을 의미하는'),
             ('B', '관계를 정리하는 것을 의미하는'),
             ('C', '다른 사람과 연락을 완전히 끊는 것을 의미하는'),
             ('D', '인맥을 넓히기 위해 노력하는 것을 의미하는'),
         ],
         explanation=(
             'Đoạn văn nói về "인맥 다이어트" (diet mối quan hệ) — tức cắt giảm, sắp xếp lại các mối quan hệ không cần '
             'thiết để tránh áp lực — khớp với B "có ý nghĩa là sắp xếp lại các mối quan hệ".\n'
             'A(kết bạn mới nhiều) và D(nỗ lực mở rộng mối quan hệ) đều mang nghĩa ngược lại (mở rộng thay vì thu gọn). '
             'C(cắt đứt liên lạc hoàn toàn) đi quá xa so với ý "sắp xếp lại" — dọn dẹp có chọn lọc, không phải cắt đứt tất cả.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, C, D là do Claude tự dựng lại.'
         )),
    dict(num=14, correct='B', options_source='reconstructed',
         stem=(
             '[Quảng cáo tuyển dụng (구인 광고, tóm tắt): có ghi ngành nghề tuyển dụng, giờ làm việc, và cách thức nộp hồ '
             'sơ là "방문 접수" (đến nộp trực tiếp) — không có thông tin về việc nộp hồ sơ online]\n'
             '다음 구인 광고를 보고 알 수 없는 것은?'
         ),
         options=[('A', '채용 직종'), ('B', '온라인 접수 방법'), ('C', '근무 시간'), ('D', '접수 방법')],
         explanation=(
             'Quảng cáo ghi rõ cách thức nộp hồ sơ là "방문 접수" (đến nộp trực tiếp) — không hề đề cập đến việc nộp hồ '
             'sơ online, nên đây là thông tin KHÔNG thể biết được — khớp với B.\n'
             'A(ngành nghề tuyển), C(giờ làm việc), D(cách nộp hồ sơ trực tiếp) đều là thông tin CÓ trong quảng cáo.\n'
             'Lưu ý: nội dung chi tiết của quảng cáo không có trong tài liệu nguồn (chỉ có gợi ý qua giải thích) — Claude '
             'đã tóm tắt bối cảnh và dựng lại 4 phương án cho hợp lý.'
         )),
    dict(num=15, correct='B', options_source='reconstructed',
         stem=(
             '[Ngữ cảnh (tóm tắt, không phải nguyên văn): đoạn văn nói về các năng lực/thái độ cần thiết trong thời đại '
             'quốc tế hóa — ngoại ngữ, tôn trọng văn hóa khác, kiến thức nền]\n'
             '윗글의 제목으로 가장 알맞은 것을 고르시오.'
         ),
         options=[
             ('A', '외국어를 배우는 방법'),
             ('B', '국제화 시대에 필요한 능력'),
             ('C', '다른 나라 문화를 소개하는 방법'),
             ('D', '해외 여행을 준비하는 방법'),
         ],
         explanation=(
             'Đoạn văn bao quát nhiều năng lực cần thiết (ngoại ngữ, tôn trọng văn hóa, kiến thức nền) trong bối cảnh '
             'toàn cầu hóa — tiêu đề bao quát nhất là B.\n'
             'A chỉ nói về một phần (ngoại ngữ), C và D đều không khớp trọng tâm bài — cả hai đều là chủ đề hẹp/khác với '
             'nội dung chính.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, C, D là do Claude tự dựng lại.'
         )),
    dict(num=16, correct='C', options_source='reconstructed',
         stem=(
             '[Ngữ cảnh (tóm tắt, không phải nguyên văn): cùng bài đọc ở câu 15 — đoạn văn nói cần giáo dục trẻ em từ nhỏ '
             'để loại bỏ định kiến và tôn trọng văn hóa lẫn nhau]\n'
             '윗글의 ( )에 들어갈 내용으로 알맞은 것을 고르시오.'
         ),
         options=[
             ('A', '외국어를 유창하게 구사해야 한다'),
             ('B', '다른 나라 역사를 암기해야 한다'),
             ('C', '다양한 문화를 경험해야 한다'),
             ('D', '국제 기구에서 일해야 한다'),
         ],
         explanation=(
             'Để loại bỏ định kiến và tôn trọng văn hóa lẫn nhau, giáo dục từ nhỏ cần giúp trẻ "trải nghiệm văn hóa đa '
             'dạng" — khớp với C.\n'
             'A(nói ngoại ngữ trôi chảy), B(học thuộc lịch sử nước khác), D(làm việc ở tổ chức quốc tế) đều không trực '
             'tiếp giải quyết vấn đề "định kiến văn hóa" mà đoạn văn nhấn mạnh.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, B, D là do Claude tự dựng lại.'
         )),
    dict(num=17, correct='D', options_source='reconstructed',
         stem=(
             '한국 도시의 문제점으로 맞는 것을 <보기>에서 모두 고른 것은?\n'
             '<보기>\n'
             'ㄱ. 일할 사람이 부족하다.\n'
             'ㄴ. 의료 시설이 부족하다.\n'
             'ㄷ. 집값이 올라 주택이 부족하다.\n'
             'ㄹ. 환경 오염이 심각하다.'
         ),
         options=[('A', 'ㄱ, ㄴ'), ('B', 'ㄱ, ㄷ'), ('C', 'ㄴ, ㄹ'), ('D', 'ㄷ, ㄹ')],
         explanation=(
             'Vấn đề của ĐÔ THỊ là (ㄷ) giá nhà tăng, thiếu nhà ở và (ㄹ) ô nhiễm môi trường — khớp với D.\n'
             '(ㄱ) thiếu lao động và (ㄴ) thiếu cơ sở y tế thực ra là vấn đề của NÔNG THÔN, không phải đô thị.\n'
             'Lưu ý: tài liệu nguồn không liệt kê nguyên văn 4 câu ㄱㄴㄷㄹ và 4 phương án tổ hợp — nội dung trên do Claude '
             'dựng lại, chỉ đáp án đúng (D) là chắc chắn khớp nguồn.'
         )),
    dict(num=18, correct='B', options_source='reconstructed',
         stem='한국의 가족에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '산업화 이후 핵가족의 비율이 크게 늘어났다.'),
             ('B', '산업화가 진행되면서 부모와 함께 사는 가족이 늘고 있다.'),
             ('C', '1인 가구의 수가 계속 증가하는 추세이다.'),
             ('D', '맞벌이 부부가 늘어나면서 가족의 형태도 다양해지고 있다.'),
         ],
         explanation=(
             'Công nghiệp hóa làm tăng tỷ lệ "gia đình hạt nhân" (핵가족) và làm GIẢM số gia đình nhiều thế hệ sống chung '
             '(확대가족/gia đình mở rộng) — nên B ("gia đình sống chung với bố mẹ đang tăng") là câu SAI, đây là đáp án đúng.\n'
             'A, C, D đều là xu hướng thực tế đúng về sự thay đổi cấu trúc gia đình Hàn Quốc.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án đúng còn lại — A, C, D là do Claude tự dựng lại.'
         )),
    dict(num=19, correct='D', options_source='reconstructed',
         stem=(
             '한국에서 태극기를 달아야 하는 국경일에 해당하는 것을 <보기>에서 모두 고른 것은?\n'
             '<보기>\n'
             'ㄱ. 설날\n'
             'ㄴ. 어버이날\n'
             'ㄷ. 광복절\n'
             'ㄹ. 제헌절\n'
             'ㅁ. 한글날\n'
             'ㅂ. 크리스마스'
         ),
         options=[('A', 'ㄱ, ㄴ, ㅂ'), ('B', 'ㄷ, ㄹ, ㅂ'), ('C', 'ㄴ, ㄷ, ㅁ'), ('D', 'ㄷ, ㄹ, ㅁ')],
         explanation=(
             '5 ngày lễ quốc gia (국경일) bắt buộc treo quốc kỳ là: 3.1절, 제헌절(ㄹ), 광복절(ㄷ), 개천절, 한글날(ㅁ) — trong '
             '<보기> này có ㄷ, ㄹ, ㅁ thuộc nhóm đó — khớp với D.\n'
             'ㄱ 설날(Tết Nguyên đán), ㄴ 어버이날(Ngày Cha mẹ), ㅂ 크리스마스(Giáng sinh) đều là ngày lễ/kỷ niệm nhưng KHÔNG '
             'phải quốc khánh (국경일) yêu cầu treo cờ.\n'
             'Lưu ý: tài liệu nguồn không liệt kê nguyên văn 6 mục ㄱ-ㅂ và 4 phương án tổ hợp — nội dung trên do Claude '
             'dựng lại dựa theo đúng danh sách quốc khánh đã nêu trong giải thích, chỉ đáp án đúng (D) là chắc chắn khớp nguồn.'
         )),
    dict(num=20, correct='D', options_source='reconstructed',
         stem='한국의 보육제도에 대한 설명 중 옳은 것은?',
         options=[
             ('A', '유치원은 보건복지부 소속 기관이다.'),
             ('B', '아동수당은 만 5세 미만 아동만 받을 수 있다.'),
             ('C', '집에서 아이를 직접 키우면 보육 지원을 받을 수 없다.'),
             ('D', '어린이집은 만 0세부터 만 5세까지의 보육과 교육을 담당한다.'),
         ],
         explanation=(
             'Nhà trẻ (어린이집) nhận và chăm sóc/giáo dục trẻ từ 0 đến 5 tuổi — khớp với D.\n'
             'A sai: mẫu giáo (유치원) thuộc Bộ Giáo dục, không phải Bộ Y tế Phúc lợi.\n'
             'B sai: trợ cấp trẻ em (아동수당) dành cho trẻ dưới 8 tuổi, không phải chỉ dưới 5 tuổi.\n'
             'C sai: gia đình tự nuôi con tại nhà vẫn được nhận trợ cấp nuôi con tại nhà (가정양육수당).\n'
             'Lưu ý: tài liệu nguồn không nêu nguyên văn 3 phương án sai (chỉ có gợi ý ngắn gọn) — câu chữ đầy đủ do '
             'Claude viết lại giữ đúng ý.'
         )),
    dict(num=21, correct='A', options_source='reconstructed',
         stem='한국의 초·중등 교육기관에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '한국에서는 만 7세부터 초등학교에 입학할 수 있다.'),
             ('B', '초등학교와 중학교는 의무 교육에 해당한다.'),
             ('C', '중학교는 3년제로 운영된다.'),
             ('D', '고등학교부터는 의무 교육이 아니다.'),
         ],
         explanation=(
             'Ở Hàn Quốc, trẻ em nhập học tiểu học khi đủ 6 tuổi (만 6세), không phải 7 tuổi — nên A là câu SAI, đây là '
             'đáp án đúng.\n'
             'B, C, D đều là mô tả đúng về hệ thống giáo dục tiểu học/THCS/THPT Hàn Quốc.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án đúng còn lại — B, C, D là do Claude tự dựng lại.'
         )),
    dict(num=22, correct='C', options_source='reconstructed',
         stem=(
             '<보기>: chương trình hội nhập xã hội (사회통합프로그램) / hỗ trợ thích ứng sớm với đời sống Hàn Quốc\n'
             '<보기>의 내용을 통해 알 수 있는 것으로 가장 적절한 것은?'
         ),
         options=[
             ('A', '외국인 근로자의 취업을 알선하기 위한 제도이다.'),
             ('B', '다문화 가정의 자녀 교육만을 위한 제도이다.'),
             ('C', '이주민들의 적응과 정착을 지원하기 위한 프로그램이다.'),
             ('D', '귀화 시험에 합격한 사람에게 주는 혜택이다.'),
         ],
         explanation=(
             'Đây là chương trình nhằm hỗ trợ sự thích ứng và định cư của người di trú/nhập cư tại Hàn Quốc — khớp với C.\n'
             'A(giới thiệu việc làm) chỉ là một khía cạnh hẹp; B(chỉ dành cho giáo dục con em gia đình đa văn hóa) và '
             'D(chỉ dành cho người đã đỗ thi nhập tịch) đều thu hẹp phạm vi sai so với mục đích thực tế của chương trình.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, B, D là do Claude tự dựng lại.'
         )),
    dict(num=23, correct='C', options_source='reconstructed',
         stem=(
             '<보기>: Tết Nguyên đán (설날)\n'
             '<보기>에 해당하는 한국의 명절에 대한 설명으로 옳지 않은 것은?'
         ),
         options=[
             ('A', '세배를 하고 어른들께 새해 인사를 드린다.'),
             ('B', '떡국을 먹으면서 나이를 한 살 더 먹는다고 생각한다.'),
             ('C', '일반적으로 이날 전에 미리 조상의 묘지를 벌초한다.'),
             ('D', '윷놀이와 같은 전통 놀이를 즐긴다.'),
         ],
         explanation=(
             'Việc cắt cỏ mộ (벌초) thường được thực hiện trước dịp Chuseok (Trung thu), không phải trước Seollal (Tết '
             'Nguyên đán) — nên C là câu SAI, đây là đáp án đúng.\n'
             'A, B, D đều là phong tục đúng của Tết Nguyên đán: làm lễ chào năm mới (세배), ăn tteokguk (được coi là thêm '
             '1 tuổi), và chơi trò chơi truyền thống như Yutnori.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án đúng còn lại — A, B, D là do Claude tự dựng lại.'
         )),
    dict(num=24, correct='B', options_source='reconstructed',
         stem='한옥에 대한 설명으로 옳은 것은?',
         options=[
             ('A', '온돌은 여름에 시원하게 지내기 위한 장치였다.'),
             ('B', '햇볕이 잘 들어오도록 남쪽으로 바라보고 지은 집을 선호했다.'),
             ('C', '풍수지리상 좋은 집터는 물을 등지고 산을 바라보는 곳이다.'),
             ('D', '신분에 관계없이 누구나 기와집에서 살 수 있었다.'),
         ],
         explanation=(
             'Người Hàn xưa thích xây nhà hướng Nam (남향) để đón nhiều ánh nắng — khớp với B.\n'
             'A sai: Ondol (온돌) là hệ thống SƯỞI cho mùa đông, còn Daecheongmaru (대청마루) mới là nơi làm mát mùa hè — '
             'câu này bị đảo ngược vai trò.\n'
             'C sai: theo phong thủy, đất tốt là "lưng tựa núi, mặt hướng sông/nước" (배산임수) — câu này mô tả ngược lại.\n'
             'D sai: chỉ quý tộc mới ở nhà ngói (기와집), thường dân ở nhà mái rạ (초가집), không phải ai cũng ở được nhà '
             'ngói.\n'
             'Lưu ý: tài liệu nguồn không nêu nguyên văn 3 phương án sai (chỉ có gợi ý ngắn gọn) — câu chữ đầy đủ do '
             'Claude viết lại giữ đúng ý.'
         )),
    dict(num=25, correct='B', options_source='reconstructed',
         stem='한국인이 가장 많이 참여하는 여가 활동인 휴식 활동에 해당하지 않는 것은?',
         options=[('A', '텔레비전 시청'), ('B', '쇼핑'), ('C', '낮잠 자기'), ('D', '산책하기')],
         explanation=(
             'Theo khảo sát KIIP, các hoạt động "nghỉ ngơi" phổ biến nhất là xem TV, ngủ trưa, đi dạo — mua sắm (쇼핑) '
             'thuộc nhóm hoạt động khác (mua sắm/tiêu dùng), không thuộc nhóm "nghỉ ngơi thư giãn" — khớp với B.\n'
             'A, C, D đều là các hoạt động nghỉ ngơi phổ biến nhất theo khảo sát.\n'
             'Lưu ý: tài liệu nguồn không liệt kê nguyên văn 3 phương án còn lại như một danh sách lựa chọn — Claude đã '
             'dùng đúng 3 hoạt động được nêu trong giải thích (xem TV, ngủ trưa, đi dạo) để dựng lại các phương án.'
         )),
    dict(num=26, correct='A', options_source='reconstructed',
         stem=(
             '<보기>: Chủ quyền thuộc về..., mọi quyền lực xuất phát từ...\n'
             '<보기>의 ( )에 공통으로 들어갈 말은?'
         ),
         options=[('A', '국민'), ('B', '대통령'), ('C', '국회'), ('D', '법원')],
         explanation=(
             'Điều 1 Hiến pháp Hàn Quốc quy định: chủ quyền quốc gia thuộc về nhân dân (국민), mọi quyền lực nhà nước '
             'xuất phát từ nhân dân — khớp với A.\n'
             'B 대통령(Tổng thống), C 국회(Quốc hội), D 법원(Tòa án) đều là các CƠ QUAN thực thi quyền lực do nhân dân trao '
             'cho, không phải nguồn gốc của chủ quyền.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — B, C, D là do Claude tự dựng lại.'
         )),
    dict(num=27, correct='D', options_source='reconstructed',
         stem='다음 중 입법부에 대한 설명으로 옳은 것은?',
         options=[
             ('A', '법에 따라 재판을 진행한다.'),
             ('B', '국가의 정책을 집행하고 행정 업무를 담당한다.'),
             ('C', '대통령을 선출하고 국무총리를 임명한다.'),
             ('D', '국정 감사를 실시하여 행정부를 견제하고 감시한다.'),
         ],
         explanation=(
             'Quốc hội (nhánh Lập pháp) có quyền giám sát Chính phủ (nhánh Hành pháp) thông qua hoạt động Thanh tra Quốc '
             'chính (국정 감사) — khớp với D.\n'
             'A(xét xử theo pháp luật) là vai trò của Tư pháp. B(thực thi chính sách, hành chính) là vai trò của Hành '
             'pháp. C(bầu tổng thống, bổ nhiệm thủ tướng) không đúng với cách thức hoạt động thực tế của Quốc hội Hàn Quốc.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, B, C là do Claude tự dựng lại.'
         )),
    dict(num=28, correct='B', options_source='reconstructed',
         stem=(
             '한국의 일자리 상황에 대한 설명으로 옳은 것을 <보기>에서 모두 고른 것은?\n'
             '<보기>\n'
             'ㄱ. 한국의 실업률은 미국이나 유럽보다 높은 편이다.\n'
             'ㄴ. 비정규직 근로자의 비율이 늘어나고 있다.\n'
             'ㄷ. 여성의 경제 활동 참가율은 선진국에 비해 낮은 편이다.\n'
             'ㄹ. 사회 보장 제도가 선진국 수준으로 잘 갖춰져 있다.'
         ),
         options=[('A', 'ㄱ, ㄴ'), ('B', 'ㄴ, ㄷ'), ('C', 'ㄴ, ㄹ'), ('D', 'ㄷ, ㄹ')],
         explanation=(
             'ㄴ đúng: tỷ trọng lao động không chính thức (비정규직) đang tăng. ㄷ đúng: tỷ lệ tham gia kinh tế của phụ nữ '
             'Hàn Quốc thấp hơn các nước phát triển — khớp với B.\n'
             'ㄱ sai: tỷ lệ thất nghiệp thực tế của Hàn Quốc thấp hơn Mỹ/châu Âu, không phải cao hơn.\n'
             'ㄹ sai: chế độ an sinh xã hội của Hàn Quốc chưa đạt trình độ các nước phát triển.\n'
             'Lưu ý: tài liệu nguồn không liệt kê nguyên văn 4 câu ㄱㄴㄷㄹ và 4 phương án tổ hợp — nội dung trên do Claude '
             'dựng lại, chỉ đáp án đúng (B) là chắc chắn khớp nguồn.'
         )),
    dict(num=29, correct='A', options_source='reconstructed',
         stem='개발원조위원회 회원국이면서 다른 나라로부터 원조를 받던 나라에서 원조를 주는 나라로 바뀐 첫 번째 사례로 꼽히는 나라는?',
         options=[('A', '한국'), ('B', '미국'), ('C', '일본'), ('D', '중국')],
         explanation=(
             'Hàn Quốc là quốc gia đầu tiên trên thế giới chuyển từ vị thế "nước nhận viện trợ" (sau chiến tranh) sang '
             '"nước đi viện trợ" khi trở thành thành viên Ủy ban Hỗ trợ Phát triển (DAC) — khớp với A.\n'
             'B, C, D đều không phải là ví dụ điển hình được nêu trong tài liệu KIIP cho trường hợp chuyển đổi này.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — B, C, D là do Claude tự dựng lại (đơn giản là tên '
             'các nước khác để làm phương án nhiễu).'
         )),
    dict(num=30, correct='C', options_source='reconstructed',
         stem='대한민국에서 외국인의 기본적인 지위와 권리를 보장해 주는 기준이 되는 것은?',
         options=[('A', '관습법'), ('B', '헌법'), ('C', '국제법'), ('D', '민법')],
         explanation=(
             '⚠️ Bản thân tài liệu nguồn cũng ghi chú thêm: trên thực tế Hiến pháp (헌법) cũng bảo đảm quyền cơ bản của '
             'người nước ngoài, nhưng trong khuôn khổ nội dung KIIP về "quyền của người nước ngoài", các điều ước quốc tế '
             '(국제법) mà Hàn Quốc đã ký kết có hiệu lực như luật trong nước, nên đáp án được chọn là C.\n'
             'A 관습법(luật tập quán) và D 민법(luật dân sự) không phải là căn cứ pháp lý chính cho vấn đề này.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, B, D là do Claude tự dựng lại (B lại chính là đáp '
             'án mà tài liệu nguồn tự thừa nhận cũng hợp lý, nên bạn có thể gặp cách ra đề khác đề cao 헌법 thay vì 국제법).'
         )),
    dict(num=31, correct='A', options_source='reconstructed',
         stem=(
             '<보기>: Khi cho vay tiền nên nhận (가) từ người vay. Khi trả tiền nên nhận (나) để chứng minh đã trả.\n'
             '<보기>의 (가), (나)에 들어갈 말로 알맞은 것은?'
         ),
         options=[
             ('A', '차용증 - 영수증'),
             ('B', '영수증 - 차용증'),
             ('C', '차용증 - 계약서'),
             ('D', '청구서 - 영수증'),
         ],
         explanation=(
             '(가) Giấy vay nợ (차용증) — nhận từ người vay khi cho vay tiền, để chứng minh khoản vay. (나) Biên lai/giấy '
             'biên nhận (영수증) — nhận khi trả tiền, để chứng minh đã thanh toán — khớp với A.\n'
             'B đảo ngược vị trí (가)(나). C, D thay một vị trí bằng giấy tờ khác không đúng vai trò được mô tả.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — B, C, D là do Claude tự dựng lại.'
         )),
    dict(num=32, correct='D', options_source='docx',
         stem='고려의 왕건에 대한 설명으로 옳은 것은?',
         options=[
             ('A', '궁예와 함께 나라 이름을 고려로 바꾸었다.'),
             ('B', '고조선을 계승하여 나라를 세웠다.'),
             ('C', '후백제를 먼저 공격한 후 신라를 통일했다.'),
             ('D', '백성의 생활을 안정시키려고 세금을 10% 이상 거두지 못하게 했다.'),
         ],
         explanation=(
             'Vua Taejo Wang Geon (Thái Tổ Vương Kiến) đã ban hành chính sách giảm thuế xuống còn khoảng 1/10 để ổn định '
             'đời sống bách tính — khớp với D.\n'
             'A sai: Wang Geon LẬT ĐỔ Gung Ye rồi mới đổi tên nước thành Goryeo, không phải "cùng" Gung Ye đổi tên.\n'
             'B sai: Goryeo kế thừa tinh thần Goguryeo, không phải Gojoseon.\n'
             'C sai: thực tế Silla tự nguyện đầu hàng trước, sau đó Goryeo mới tấn công và diệt Hậu Baekje — không phải '
             'tấn công Hậu Baekje rồi mới thống nhất Silla.'
         )),
    dict(num=33, correct='B', options_source='reconstructed',
         stem=(
             '<보기>의 내용 중 세종대왕에 대한 설명으로 옳은 것을 모두 고른 것은?\n'
             '<보기>\n'
             'ㄱ. 한글을 창제하였다.\n'
             'ㄴ. 거북선을 만들어 일본군을 물리쳤다.\n'
             'ㄷ. 경국대전을 편찬하였다.\n'
             'ㄹ. 측우기 등 과학 기술을 발전시켜 농업을 도왔다.'
         ),
         options=[('A', 'ㄱ, ㄴ'), ('B', 'ㄱ, ㄹ'), ('C', 'ㄴ, ㄷ'), ('D', 'ㄷ, ㄹ')],
         explanation=(
             'ㄱ đúng: vua Sejong sáng tạo ra chữ Hangeul. ㄹ đúng: ông phát triển khoa học kỹ thuật (như máy đo lượng '
             'mưa 측우기) giúp ích cho nông nghiệp — khớp với B.\n'
             'ㄴ sai: thuyền rùa (거북선) là phát minh của tướng Yi Sun-sin (thời Joseon sau này), không phải vua Sejong.\n'
             'ㄷ sai: Bộ luật Gyeongguk Daejeon (경국대전) được biên soạn dưới thời vua Seongjong, không phải vua Sejong.\n'
             'Lưu ý: tài liệu nguồn không liệt kê nguyên văn 4 câu ㄱㄴㄷㄹ và 4 phương án tổ hợp — nội dung trên do Claude '
             'dựng lại, chỉ đáp án đúng (B) là chắc chắn khớp nguồn.'
         )),
    dict(num=34, correct='C', options_source='docx',
         stem=(
             '<보기>: chùa Buseoksa / Seokguram và Bulguksa / Đài Dosan Seowon và làng Hahoe → đây là vùng Gyeongsang '
             '(경상도).\n'
             '<보기>에 해당하는 지역에 대한 설명으로 옳지 않은 것은?'
         ),
         options=[
             ('A', '창녕에 우포늪이라는 습지가 있다.'),
             ('B', '대구, 울산, 부산과 같은 도시를 포함한다.'),
             ('C', '이 지역은 한국의 중앙부 동쪽에 위치하고 있으며 눈이 많이 온다.'),
             ('D', '충무공 이순신을 기리는 한산대첩 축제가 통영에서 열린다.'),
         ],
         explanation=(
             'Vùng nằm ở phía Đông miền Trung và có nhiều tuyết thực ra là Gangwon (강원도), không phải Gyeongsang (nằm '
             'ở phía Đông NAM) — nên C là câu SAI, đây là đáp án đúng.\n'
             'A, B, D đều là đặc điểm có thật của vùng Gyeongsang: có đầm lầy Upo ở Changnyeong, bao gồm các thành phố '
             'lớn như Daegu/Ulsan/Busan, và có lễ hội Hansan Daecheop tại Tongyeong kỷ niệm tướng Yi Sun-sin.'
         )),
    dict(num=35, correct='B', options_source='reconstructed',
         stem=(
             '<보기>: (가) từng là cảng nhỏ, nay là thành phố cảng lớn giao thương quốc tế. Sân bay (나) là sân bay quốc '
             'tế lớn nhất Hàn Quốc.\n'
             '<보기>의 (가), (나)에 들어갈 말로 알맞은 것은?'
         ),
         options=[
             ('A', '제물포 - 김포국제공항'),
             ('B', '제물포 - 인천국제공항'),
             ('C', '부산포 - 인천국제공항'),
             ('D', '목포 - 김해국제공항'),
         ],
         explanation=(
             'Cảng Incheon ngày xưa có tên là Jemulpo (제물포), nay đã phát triển thành thành phố cảng lớn. Sân bay lớn '
             'nhất Hàn Quốc là Sân bay Quốc tế Incheon (인천국제공항) — khớp với B.\n'
             'A thay sân bay bằng Gimpo (sân bay nội địa/khu vực Seoul, không phải lớn nhất). C, D thay cả tên cảng bằng '
             'địa danh khác không đúng.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, C, D là do Claude tự dựng lại.'
         )),
    dict(num=36, correct='D', options_source='docx',
         stem='충청지역에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '단양팔경이라는 8개의 명소가 있다.'),
             ('B', '대전에서는 과학과 문화가 결합된 사이언스 페스티벌이 열린다.'),
             ('C', '보령 머드 축제가 유명하다.'),
             ('D', '백제 문화제는 청주와 충주에서 매년 개최되는 역사·문화 축제이다.'),
         ],
         explanation=(
             'Lễ hội Văn hóa Baekje (백제 문화제) thực ra được tổ chức tại Buyeo (부여) và Gongju (공주) — vốn là cố đô của '
             'Baekje — không phải Cheongju và Chungju — nên D là câu SAI, đây là đáp án đúng.\n'
             'A, B, C đều là đặc điểm có thật của vùng Chungcheong: Danyang Palgyeong (8 danh thắng ở Danyang), Lễ hội '
             'Khoa học Daejeon, và Lễ hội Bùn Boryeong nổi tiếng.'
         )),
]
