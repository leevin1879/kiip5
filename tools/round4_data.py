# -*- coding: utf-8 -*-
# Question set built from "한국어_모의고사_(5단계_4회)_—_Giải_thích_chi_tiết.docx".
# That source file only gives the correct answer + prose explanation for many
# questions (no clean list of the other 3 options, and no original Korean
# reading passages for Q13-16). Where the source doesn't give the real
# option text, Claude reconstructed plausible distractors from the reasoning
# already present in the source; those questions are flagged
# options_source="reconstructed" and noted in the explanation.

QUESTIONS = [
    dict(num=1, correct='C', options_source='docx',
         stem='머리가 아플 때는 ( )을/를 먹으면 돼요.',
         options=[('A', '감기약'), ('B', '소화제'), ('C', '두통약'), ('D', '해열제')],
         explanation=(
             '"머리가 아플 때" (khi đau đầu) thì cần uống thuốc đau đầu — 두통약.\n'
             'A 감기약(thuốc cảm) dùng khi bị cảm cúm.\n'
             'B 소화제(thuốc tiêu hóa) dùng khi khó tiêu.\n'
             'D 해열제(thuốc hạ sốt) dùng khi sốt, không phải chỉ đau đầu đơn thuần.'
         )),
    dict(num=2, correct='C', options_source='docx',
         stem='저는 스트레스가 ( ) 조용한 음악을 들으면서 산책을 합니다. 그러면 머리가 맑아집니다.',
         options=[('A', '걸리면'), ('B', '받으면'), ('C', '쌓이면'), ('D', '풀리면')],
         explanation=(
             'Cụm từ cố định đi với "스트레스가" (trợ từ 가) là "스트레스가 쌓이다" (căng thẳng tích tụ) — khớp với C.\n'
             'A 걸리면(nếu mắc bệnh) không hợp nghĩa.\n'
             'B 받으면(nếu nhận) phải đi với trợ từ "를" (스트레스를 받다), không hợp với trợ từ "가" trong câu.\n'
             'D 풀리면(nếu được giải tỏa) sai logic — người này đang MÔ TẢ hành động để giải tỏa (nghe nhạc, đi dạo), '
             'nên trước đó phải là lúc căng thẳng TÍCH TỤ chứ chưa được giải tỏa.'
         )),
    dict(num=3, correct='A', options_source='docx',
         stem='우리 회사에서는 한국어와 중국어에 ( ) 직원을 구하고 있다.',
         options=[('A', '능통한'), ('B', '대단한'), ('C', '불편한'), ('D', '지나친')],
         explanation=(
             '"언어에 능통하다" = thành thạo một ngôn ngữ nào đó — khớp với ngữ cảnh tuyển nhân viên giỏi tiếng Hàn/Trung.\n'
             'B 대단한(tuyệt vời), C 불편한(bất tiện), D 지나친(quá mức) đều không phải cụm từ đi kèm "언어에".'
         )),
    dict(num=4, correct='D', options_source='docx',
         stem='휴대폰을 물에 빠뜨렸을 때 ( ) 전원을 켜면 안 됩니다.',
         options=[('A', '아마'), ('B', '온통'), ('C', '저절로'), ('D', '절대로')],
         explanation=(
             '"절대로 ... (으)면 안 되다" là cấu trúc cố định mang nghĩa "tuyệt đối không được làm gì" — khớp với D.\n'
             'A 아마(có lẽ) diễn tả phỏng đoán, B 온통(toàn bộ) và C 저절로(tự động) không hợp nghĩa câu cảnh báo này.'
         )),
    dict(num=5, correct='C', options_source='docx',
         stem='가: 왜 이렇게 작은 가방을 샀어요?\n나: 인터넷에서 사진만 보고 큰 ( ).',
         options=[('A', '가방이 아니에요'), ('B', '가방이면 좋겠어요'), ('C', '가방인 줄 알았어요'), ('D', '가방이기 때문이에요')],
         explanation=(
             'Cấu trúc "-(으)ㄴ 줄 알다" thể hiện sự lầm tưởng về một việc gì đó — "chỉ xem ảnh trên mạng nên đã tưởng là túi to" — khớp với C.\n'
             'A, B, D đều không diễn tả đúng sắc thái "lầm tưởng" mà câu cần.'
         )),
    dict(num=6, correct='B', options_source='docx',
         stem='가: 이번 주말에 같이 등산을 할까요?\n나: 미안해요. 친구와 경복궁에 ( ).',
         options=[('A', '가라고 했어요'), ('B', '가기로 했어요'), ('C', '가는 편이에요'), ('D', '가는 법이에요')],
         explanation=(
             'Cấu trúc "-기로 하다" thể hiện một quyết định/kế hoạch/lời hẹn đã định trước — "đã hẹn đi Gyeongbokgung với bạn" — khớp với B.\n'
             'A 가라고 했어요(đã bảo đi đi — câu gián tiếp mệnh lệnh), C 가는 편이에요(thường hay đi), D 가는 법이에요(hiển nhiên là đi) '
             'đều không hợp ngữ cảnh từ chối lời rủ vì đã có hẹn khác.'
         )),
    dict(num=7, correct='C', options_source='docx',
         stem='가: 공항에 도착하면 바로 연락주세요.\n나: 네, ( ) 연락할게요.',
         options=[('A', '도착해야'), ('B', '도착하면서'), ('C', '도착하자마자'), ('D', '도착하고 해서')],
         explanation=(
             'Người A dùng từ "바로" (ngay lập tức); người B đáp lại đồng tình bằng cấu trúc "-자마자" (ngay khi vừa...) — khớp với C.\n'
             'A 도착해야(phải đến thì mới...), B 도착하면서(vừa đến vừa...), D 도착하고 해서(vì đến và...) đều không diễn tả đúng ý "ngay khi".'
         )),
    dict(num=8, correct='D', options_source='docx',
         stem='가: 취직 준비를 한다면서요? 월급은 얼마나 받고 싶어요?\n나: 당연히 많이 ( ) 좋지요.',
         options=[('A', '받도록'), ('B', '받든지'), ('C', '받으려면'), ('D', '받을수록')],
         explanation=(
             'Cấu trúc "-(으)면 -(으)ㄹ수록" (càng... càng...) được rút gọn thành "-ㄹ수록" — "nhận càng nhiều lương càng tốt" — khớp với D.\n'
             'A 받도록(để nhận được), B 받든지(nhận hay không), C 받으려면(nếu muốn nhận) đều không hợp cấu trúc "càng...càng" này.'
         )),
    dict(num=9, correct='C', options_source='docx',
         stem='밖이 시끄러워서 책을 ( ).',
         options=[('A', '읽을 정도이다'), ('B', '읽으려고 한다'), ('C', '읽을 수 없었다'), ('D', '읽으려던 참이다')],
         explanation=(
             'Bên ngoài ồn ào (nguyên nhân) dẫn đến kết quả không thể đọc sách. "-ㄹ 수 없다" diễn tả sự không có khả năng — khớp với C.\n'
             'A 읽을 정도이다(đến mức đọc được), B 읽으려고 한다(định đọc), D 읽으려던 참이다(vừa định đọc) đều không hợp với nguyên nhân "ồn ào".'
         )),
    dict(num=10, correct='D', options_source='docx',
         stem='버스가 끊겨서 택시를 ( ).',
         options=[('A', '탈 뻔했어요'), ('B', '타 있었어요'), ('C', '타지 마세요'), ('D', '탈 수밖에 없었어요')],
         explanation=(
             'Cấu trúc "-(으)ㄹ 수밖에 없다" diễn tả tình huống không còn lựa chọn nào khác — "xe buýt hết chuyến nên chỉ còn cách bắt taxi" — khớp với D.\n'
             'A 탈 뻔했어요(suýt đi — nghĩa là cuối cùng KHÔNG đi, sai logic), B 타 있었어요(sai ngữ pháp), C 타지 마세요(đừng đi — mệnh lệnh, sai ngữ cảnh).'
         )),
    dict(num=11, correct='B', options_source='docx',
         stem='몸이 아프다 / 부모님 생각이 나다',
         options=[
             ('A', '아파서 부모님 생각이 나는 척했다.'),
             ('B', '몸이 아프면 부모님 생각이 나기 마련이다.'),
             ('C', '아플수록 부모님 생각이 나면 좋겠다.'),
             ('D', '아프다시피 부모님 생각이 나려던 참이다.'),
         ],
         explanation=(
             'Cấu trúc "-기 마련이다" diễn tả một quy luật tự nhiên, điều hiển nhiên sẽ xảy ra — "hễ ốm đau thì đương nhiên sẽ nhớ bố mẹ" — khớp với B.\n'
             'A(giả vờ nhớ), C(càng ốm càng ước gì nhớ), D(cấu trúc/nghĩa không hợp) đều sai.'
         )),
    dict(num=12, correct='A', options_source='docx',
         stem='버스를 타다 / 무단횡단을 하다 / 오토바이에 부딪히다',
         options=[
             ('A', '버스를 타려고 무단횡단을 하다가 오토바이에 부딪힐 뻔했다.'),
             ('B', '버스를 타려면 무단횡단을 하곤 했다.'),
             ('C', '버스를 탈 텐데 무단횡단을 하다가 부딪힌 줄 알았다.'),
             ('D', '버스를 타면서 무단횡단을 하다가 부딪힐 정도이다.'),
         ],
         explanation=(
             'Kết hợp "-려고"(mục đích: để bắt xe buýt), "-다가"(hành động đang làm thì bị ngắt quãng: đang băng qua đường trái phép), '
             'và "-ㄹ 뻔하다"(suýt nữa thì xảy ra: suýt bị xe máy tông) — khớp với A.\n'
             'B, C, D đều sai ngữ pháp hoặc sai nghĩa so với 3 vế cho trước.'
         )),
    dict(num=13, correct='B', options_source='reconstructed',
         stem=(
             '[Ngữ cảnh (tóm tắt từ tài liệu, không phải nguyên văn tiếng Hàn — bài đọc gốc không có trong tài liệu nguồn): '
             'đoạn văn nói về bệnh trầm cảm — nếu không thoát khỏi tâm trạng u uất]\n'
             '다음 ( )에 알맞은 것을 고르시오.'
         ),
         options=[
             ('A', '기분이 좋아진다면'),
             ('B', '우울한 기분이 지속된다면'),
             ('C', '운동을 많이 한다면'),
             ('D', '친구를 많이 만난다면'),
         ],
         explanation=(
             'Theo tài liệu gốc: câu trước nói về việc "không thoát khỏi tâm trạng u uất", câu sau nêu mốc thời gian "2주 이상" '
             '(trên 2 tuần) — nên chỗ trống cần điền điều kiện "nếu tâm trạng u uất đó kéo dài" — khớp với B.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, C, D là do Claude tự dựng lại cho hợp lý với chủ đề, '
             'không phải nguyên văn đề thi.'
         )),
    dict(num=14, correct='B', options_source='reconstructed',
         stem=(
             '[Bảng thông tin 문화유산 아카데미 (tóm tắt): phí tham gia miễn phí (chỉ tự túc vé vào cửa + phí đi lại); '
             'diễn ra vào thứ Bảy; dành cho người lớn, giới hạn 20 người; phải tham gia đầy đủ các buổi mới được cấp giấy chứng nhận]\n'
             '다음 문화유산 아카데미에 대한 설명으로 옳은 것은?'
         ),
         options=[
             ('A', '매주 평일 저녁에 진행된다.'),
             ('B', '입장료와 교통비는 개인이 각자 준비해야 한다.'),
             ('C', '신청한 사람 모두에게 수료증을 발급해 준다.'),
             ('D', '관심 있는 사람은 누구나 신청할 수 있다.'),
         ],
         explanation=(
             'Bảng thông tin ghi rõ "비용: 무료 (단, 입장료와 교통비는 개인 부담)" — khớp với B.\n'
             'A sai: chương trình học vào thứ Bảy chứ không phải các buổi tối ngày thường.\n'
             'C sai: phải tham gia đầy đủ các buổi mới được cấp giấy chứng nhận, không phải cứ đăng ký là có.\n'
             'D sai: chương trình chỉ dành cho người lớn và giới hạn 20 người, không phải ai cũng đăng ký được.\n'
             'Lưu ý: câu chữ chính xác của A/C/D trong tài liệu gốc bị rút gọn — Claude đã viết lại thành câu hoàn chỉnh giữ đúng ý nghĩa.'
         )),
    dict(num=15, correct='D', options_source='reconstructed',
         stem=(
             '[Ngữ cảnh (tóm tắt, không phải nguyên văn): đoạn văn nói về bệnh người lớn (성인병) xuất phát từ thói quen xấu, '
             'và cách phòng ngừa bằng thói quen sinh hoạt lành mạnh (vận động, ăn uống)]\n'
             '윗글의 제목으로 가장 알맞은 것을 고르시오.'
         ),
         options=[
             ('A', '성인병의 종류와 증상'),
             ('B', '규칙적인 운동의 중요성'),
             ('C', '건강 검진을 받는 방법'),
             ('D', '성인병 예방을 위한 건강한 생활 습관'),
         ],
         explanation=(
             'Đoạn văn nói về việc bệnh người lớn xuất phát từ thói quen xấu, và cách phòng ngừa là xây dựng thói quen sinh hoạt '
             'lành mạnh — tiêu đề bao quát nhất là D.\n'
             'A chỉ nói về loại bệnh/triệu chứng, B chỉ là một phần nhỏ (vận động), C không phải nội dung chính của bài — đều hẹp hơn D.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, B, C là do Claude tự dựng lại.'
         )),
    dict(num=16, correct='B', options_source='reconstructed',
         stem=(
             '[Ngữ cảnh (tóm tắt, không phải nguyên văn): cùng bài đọc về bệnh người lớn (성인병) ở câu 15 — bệnh này còn được '
             'gọi là "생활습관병" (bệnh thói quen sinh hoạt), gây ra bởi các thói quen xấu như ăn mặn, thiếu vận động, căng thẳng]\n'
             '윗글의 (ㄱ)에 들어갈 내용으로 알맞은 것을 고르시오.'
         ),
         options=[
             ('A', '유전적인 요인'),
             ('B', '잘못된 생활 습관'),
             ('C', '다른 병의 합병증'),
             ('D', '노화로 인한 자연스러운 현상'),
         ],
         explanation=(
             'Bệnh người lớn được gọi là "생활 습관병" (bệnh thói quen sinh hoạt), và bài liệt kê các thói quen xấu (ăn mặn, thiếu '
             'vận động, stress...) là nguyên nhân — nên (ㄱ) cần điền là "thói quen sinh hoạt sai lầm" — khớp với B.\n'
             'A(yếu tố di truyền), C(biến chứng của bệnh khác), D(hiện tượng tự nhiên do lão hóa) đều không phải nguyên nhân được '
             'bài nhấn mạnh.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, C, D là do Claude tự dựng lại.'
         )),
    dict(num=17, correct='A', options_source='docx',
         stem=(
             '<보기>: đảm bảo mức sống cơ bản cho người dân / hỗ trợ chi phí sinh hoạt cho người thu nhập thấp\n'
             '<보기>의 내용에 공통적으로 해당되는 것은?'
         ),
         options=[('A', '공공부조'), ('B', '사회보험'), ('C', '건강보험'), ('D', '사회복지서비스')],
         explanation=(
             '공공부조 (trợ cấp công) là chế độ phúc lợi mà nhà nước hỗ trợ trực tiếp chi phí sinh hoạt cho người không có khả năng '
             'tự trang trải cuộc sống — khớp với A.\n'
             'B 사회보험(bảo hiểm xã hội) và C 건강보험(bảo hiểm y tế) là các hình thức bảo hiểm cần đóng phí trước, không phải trợ '
             'cấp trực tiếp; D 사회복지서비스(dịch vụ phúc lợi xã hội) là khái niệm rộng hơn, không khớp riêng với 2 đặc điểm nêu.'
         )),
    dict(num=18, correct='D', options_source='reconstructed',
         stem=(
             '한국 농촌의 문제점을 해결하기 위한 방법으로 맞는 것을 <보기>에서 모두 고른 것은?\n'
             '<보기>\n'
             'ㄱ. 농촌 지역은 인구가 부족해서 살 집이 부족하다.\n'
             'ㄴ. 젊은 사람들이 도시로 떠나면서 농촌에 일손이 부족해졌다.\n'
             'ㄷ. 편의 시설을 늘리고 정보화 교육을 실시한다.\n'
             'ㄹ. 새로운 기술을 도입하여 생산성을 높인다.'
         ),
         options=[('A', 'ㄱ, ㄴ'), ('B', 'ㄱ, ㄷ'), ('C', 'ㄴ, ㄹ'), ('D', 'ㄷ, ㄹ')],
         explanation=(
             'Giải pháp thực sự cho vấn đề nông thôn là ㄷ (tăng cường cơ sở tiện ích và giáo dục tin học) và ㄹ (nâng cao năng '
             'suất bằng công nghệ mới) — khớp với D.\n'
             'ㄱ sai vì nông thôn đang GIẢM dân số (không phải thiếu nhà vì thiếu dân).\n'
             'ㄴ là một NGUYÊN NHÂN gây ra vấn đề (thiếu lao động trẻ), không phải một GIẢI PHÁP.\n'
             'Lưu ý: tài liệu nguồn không liệt kê nguyên văn 4 câu ㄱㄴㄷㄹ và 4 phương án tổ hợp — nội dung trên do Claude dựng '
             'lại dựa theo đúng lý luận đúng/sai đã có trong tài liệu, chỉ đáp án đúng (D) là chắc chắn khớp nguồn.'
         )),
    dict(num=19, correct='A', options_source='reconstructed',
         stem='한국의 고등 교육기관에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '한국의 고등 교육기관에는 고등학교, 대학교, 대학원이 있다.'),
             ('B', '대학교는 4년제와 2~3년제 전문대학으로 나뉜다.'),
             ('C', '대학원은 석사 과정과 박사 과정으로 구성된다.'),
             ('D', '고등 교육기관에 진학하려면 고등학교를 졸업해야 한다.'),
         ],
         explanation=(
             '"고등 교육기관" (giáo dục bậc cao) ở Hàn Quốc chỉ gồm Đại học (대학교) và Cao học (대학원) — trường cấp 3 '
             '(고등학교) thuộc "중등 교육기관" (giáo dục trung học), không phải giáo dục bậc cao — nên A là câu SAI, đây là đáp án đúng.\n'
             'B, C, D đều là mô tả đúng về hệ thống giáo dục đại học/sau đại học Hàn Quốc.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — B, C, D là do Claude tự dựng lại.'
         )),
    dict(num=20, correct='D', options_source='reconstructed',
         stem=(
             '<보기>: 포크(nĩa) / 휴지(giấy vệ sinh) / 찹쌀떡(bánh nếp)\n'
             '<보기>에 제시된 용어로 설명할 수 있는 한국의 사회 현상으로 가장 적절한 것은?'
         ),
         options=[
             ('A', '명절에 조상들께 감사의 의미로 드리는 선물이다.'),
             ('B', '결혼식에서 신랑 신부에게 주는 전통 선물이다.'),
             ('C', '이사할 때 이웃에게 인사로 주는 선물이다.'),
             ('D', '대학수학능력시험이 중요하므로 시험을 잘 보라는 의미로 선물한다.'),
         ],
         explanation=(
             'Đây là những món quà truyền thống tặng cho sĩ tử trước kỳ thi đại học (수능), mang ý nghĩa chơi chữ: 포크(nĩa) '
             'liên tưởng "찍다" (đâm/chọn trúng đáp án), 휴지(giấy vệ sinh) liên tưởng "풀다" (gỡ/giải bài trôi chảy), 찹쌀떡(bánh '
             'nếp) liên tưởng "붙다" (dính/thi đậu) — khớp với D.\n'
             'A, B, C là các dịp tặng quà khác không liên quan đến 3 món quà chơi chữ này.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, B, C là do Claude tự dựng lại.'
         )),
    dict(num=21, correct='D', options_source='reconstructed',
         stem='평생교육에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '평생교육은 정규 학교 교육 이외의 다양한 교육 활동을 말한다.'),
             ('B', '평생학습관, 도서관 등에서 다양한 평생교육 프로그램을 운영한다.'),
             ('C', '나이나 학력에 관계없이 누구나 참여할 수 있다.'),
             ('D', '최근에는 인터넷 등 미디어를 이용한 평생교육은 감소하고 있다.'),
         ],
         explanation=(
             'Thực tế hoàn toàn ngược lại — nhờ công nghệ, việc học tập suốt đời qua internet/media đang TĂNG rất mạnh, không '
             'phải giảm — nên D là câu SAI, đây là đáp án đúng.\n'
             'A, B, C đều là mô tả đúng về giáo dục suốt đời (평생교육) ở Hàn Quốc.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án đúng còn lại — A, B, C là do Claude tự dựng lại.'
         )),
    dict(num=22, correct='B', options_source='reconstructed',
         stem=(
             '한국 음식에 대한 설명으로 옳은 것을 <보기>에서 모두 고른 것은?\n'
             '<보기>\n'
             'ㄱ. 숟가락과 젓가락을 이용해서 밥과 국을 먹는다.\n'
             'ㄴ. 불고기는 대표적인 발효 음식이다.\n'
             'ㄷ. 생일이나 명절에 떡을 먹는 풍습이 있다.\n'
             'ㄹ. 국은 재료를 굽는 방식으로 만든 음식이다.'
         ),
         options=[('A', 'ㄱ, ㄴ'), ('B', 'ㄱ, ㄷ'), ('C', 'ㄴ, ㄹ'), ('D', 'ㄷ, ㄹ')],
         explanation=(
             'ㄱ đúng: người Hàn dùng thìa và đũa để ăn cơm, canh. ㄷ đúng: có phong tục ăn bánh tteok vào dịp sinh nhật, lễ Tết '
             '— khớp với B.\n'
             'ㄴ sai: 불고기 (thịt nướng) không phải món ăn lên men.\n'
             'ㄹ sai: 국 (canh) là món nấu bằng nước, không phải chế biến bằng cách nướng.\n'
             'Lưu ý: tài liệu nguồn không liệt kê nguyên văn 4 câu ㄱㄴㄷㄹ và 4 phương án tổ hợp — nội dung trên do Claude dựng '
             'lại, chỉ đáp án đúng (B) là chắc chắn khớp nguồn.'
         )),
    dict(num=23, correct='B', options_source='reconstructed',
         stem=(
             '<보기>: văn hóa được đông đảo người dân yêu thích trong đời sống hàng ngày (phim ảnh, âm nhạc, thời trang)\n'
             '<보기>의 ( )에 공통으로 들어갈 말은?'
         ),
         options=[('A', '전통문화'), ('B', '대중문화'), ('C', '지역문화'), ('D', '다문화')],
         explanation=(
             'Văn hóa được đông đảo người dân yêu thích trong đời sống hàng ngày (phim, nhạc, thời trang) gọi là "대중문화" '
             '(văn hóa đại chúng) — khớp với B.\n'
             'A 전통문화(văn hóa truyền thống), C 지역문화(văn hóa địa phương), D 다문화(đa văn hóa) đều là khái niệm khác, không '
             'khớp với đặc điểm "được đông đảo yêu thích trong đời sống hàng ngày".\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, C, D là do Claude tự dựng lại.'
         )),
    dict(num=24, correct='A', options_source='reconstructed',
         stem='선거에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '보통선거는 만 20세가 된 국민은 누구나 선거에 참여할 수 있다는 것이다.'),
             ('B', '평등선거는 모든 유권자가 한 표씩 동등하게 행사하는 것이다.'),
             ('C', '직접선거는 유권자가 대리인 없이 직접 투표하는 것이다.'),
             ('D', '비밀선거는 누구에게 투표했는지 다른 사람이 알 수 없게 하는 것이다.'),
         ],
         explanation=(
             'Ở Hàn Quốc, độ tuổi có quyền bầu cử hiện tại là đủ 18 tuổi (만 18세), không phải 20 tuổi như A nêu — nên A là câu '
             'SAI, đây là đáp án đúng.\n'
             'B, C, D là mô tả đúng về 3 nguyên tắc còn lại trong 4 nguyên tắc bầu cử cơ bản (bình đẳng, trực tiếp, bí mật).\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án đúng còn lại — B, C, D là do Claude tự dựng lại.'
         )),
    dict(num=25, correct='B', options_source='reconstructed',
         stem=(
             '<보기>: người nước ngoài có thẻ cư trú vĩnh viễn (F-5) trên 3 năm\n'
             '<보기>의 내용에 해당하는 사람이 할 수 있는 것은?'
         ),
         options=[('A', '대통령 선거'), ('B', '지방 선거'), ('C', '국회의원 선거'), ('D', '국민투표')],
         explanation=(
             'Người nước ngoài có thẻ vĩnh trú (F-5) trên 3 năm được quyền tham gia bỏ phiếu trong Bầu cử ĐỊA PHƯƠNG (지방 선거) '
             'để bầu thị trưởng, hội đồng địa phương — khớp với B.\n'
             'A(bầu Tổng thống), C(bầu Quốc hội), D(trưng cầu dân ý toàn quốc) đều chỉ dành cho công dân Hàn Quốc.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, C, D là do Claude tự dựng lại.'
         )),
    dict(num=26, correct='C', options_source='reconstructed',
         stem=(
             '<보기>: cơ quan giải quyết tranh chấp bằng pháp luật / Tòa án tối cao, Tòa án địa phương...\n'
             '<보기>의 내용에 공통적으로 해당되는 것은?'
         ),
         options=[('A', '입법부'), ('B', '행정부'), ('C', '사법부'), ('D', '헌법재판소')],
         explanation=(
             'Hệ thống tòa án (법원) — nơi giải quyết tranh chấp theo pháp luật — chính là nhánh Tư pháp (사법부) — khớp với C.\n'
             'A 입법부(lập pháp — Quốc hội), B 행정부(hành pháp — Chính phủ) là 2 nhánh quyền lực khác; D 헌법재판소(Tòa án Hiến '
             'pháp) là một cơ quan cụ thể, không bao quát toàn bộ hệ thống tòa án được mô tả.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án sai — A, B, D là do Claude tự dựng lại.'
         )),
    dict(num=27, correct='A', options_source='reconstructed',
         stem='한국이 빠르게 경제 성장을 이룰 수 있었던 요인이 아닌 것은?',
         options=[
             ('A', '자본과 자원'),
             ('B', '높은 교육열과 우수한 인적 자원'),
             ('C', '정부 주도의 수출 중심 경제 정책'),
             ('D', '근면하고 성실한 노동력'),
         ],
         explanation=(
             'Sau chiến tranh, Hàn Quốc là một nước rất nghèo, gần như không có vốn (자본) và cực kỳ khan hiếm tài nguyên '
             '(자원) — nên "vốn và tài nguyên" KHÔNG phải là yếu tố giúp tăng trưởng, mà ngược lại là điểm bất lợi — nên A là '
             'câu trả lời đúng cho câu hỏi "yếu tố KHÔNG phải".\n'
             'B, C, D đều là những yếu tố thực sự đã giúp Hàn Quốc tăng trưởng nhanh: tinh thần hiếu học/nguồn nhân lực tốt, '
             'chính sách kinh tế hướng xuất khẩu do chính phủ chủ trì, và lực lượng lao động cần cù.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án đúng còn lại — B, C, D là do Claude tự dựng lại.'
         )),
    dict(num=28, correct='B', options_source='reconstructed',
         stem=(
             '금융 기관에 대한 설명으로 옳은 것을 <보기>에서 모두 고른 것은?\n'
             '<보기>\n'
             'ㄱ. 농협이나 우체국은 안전하고 이용하기 편리하다.\n'
             'ㄴ. 지방은행은 이자가 높지만 규모가 작다.\n'
             'ㄷ. 인터넷전문은행은 절차가 간단하고 수수료가 낮다.\n'
             'ㄹ. 한국은행은 개인과 직접 예금 거래를 한다.'
         ),
         options=[('A', 'ㄱ, ㄴ, ㄷ'), ('B', 'ㄱ, ㄷ'), ('C', 'ㄴ, ㄹ'), ('D', 'ㄴ, ㄷ, ㄹ')],
         explanation=(
             '⚠️ Câu này ngay trong tài liệu nguồn cũng tự ghi chú không chắc chắn ("Trong đề không có lựa chọn ㄱ, ㄴ, ㄷ"). '
             'Theo lý luận của tài liệu: ㄱ (Nonghyup/bưu điện an toàn, tiện lợi) ĐÚNG, ㄴ (ngân hàng địa phương lãi cao nhưng '
             'quy mô nhỏ) ĐÚNG, ㄷ (ngân hàng internet thủ tục đơn giản, phí thấp) ĐÚNG, chỉ ㄹ (Ngân hàng Trung ương giao dịch '
             'trực tiếp với cá nhân) là SAI — nhưng đáp án được chọn chỉ là "ㄱ, ㄷ" (bỏ ㄴ dù ㄴ được coi là đúng), tài liệu '
             'nguồn không giải thích rõ vì sao. Mình giữ theo đáp án B như tài liệu gốc ghi nhưng bạn nên lưu ý sự thiếu nhất '
             'quán này khi ôn tập.\n'
             'Lưu ý: các phương án tổ hợp và nguyên văn 4 câu ㄱㄴㄷㄹ là do Claude dựng lại.'
         )),
    dict(num=29, correct='A', options_source='reconstructed',
         stem=(
             '전통 시장에 대한 설명으로 옳은 것을 <보기>에서 모두 고른 것은?\n'
             '<보기>\n'
             'ㄱ. 전통 시장은 매일 상시로 운영되는 시장이다.\n'
             'ㄴ. 물건 값을 흥정할 수 있다.\n'
             'ㄷ. 24시간 언제나 이용할 수 있다.\n'
             'ㄹ. 대형 마트처럼 모든 물건을 대규모로 판매한다.'
         ),
         options=[('A', 'ㄱ, ㄴ'), ('B', 'ㄱ, ㄷ'), ('C', 'ㄴ, ㄹ'), ('D', 'ㄷ, ㄹ')],
         explanation=(
             '⚠️ Câu này ngay trong tài liệu nguồn cũng tự ghi chú nghi ngờ có lỗi thiết kế đề. Theo lý luận: ㄴ (có thể mặc cả '
             'giá) chắc chắn ĐÚNG; ㄷ (mở 24/24) SAI vì đó là đặc điểm của cửa hàng tiện lợi; ㄹ (bán mọi thứ quy mô lớn) SAI vì '
             'đó là đặc điểm của siêu thị lớn. Riêng ㄱ ("là chợ thường trực mở mỗi ngày") tài liệu nguồn cũng chỉ nói "có thể '
             'coi là đúng trong ngữ cảnh hẹp" chứ không khẳng định chắc chắn. Mình giữ theo đáp án A như tài liệu gốc ghi '
             'nhưng đây là câu có độ tin cậy thấp nhất trong toàn bộ đề — bạn nên kiểm tra lại nếu có nguồn khác.\n'
             'Lưu ý: các phương án tổ hợp và nguyên văn 4 câu ㄱㄴㄷㄹ là do Claude dựng lại.'
         )),
    dict(num=30, correct='D', options_source='reconstructed',
         stem='국적을 결정하는 방법에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '한국은 혈통주의를 원칙으로 국적을 결정한다.'),
             ('B', '부모 중 한 명이라도 한국인이면 자녀는 한국 국적을 가질 수 있다.'),
             ('C', '외국인은 일정 요건을 갖추면 귀화를 통해 한국 국적을 취득할 수 있다.'),
             ('D', '부모가 모두 외국인이라도 한국에서 태어난 자녀는 대한민국 국민이 될 수 있다.'),
         ],
         explanation=(
             'Hàn Quốc áp dụng nguyên tắc Huyết thống (혈통주의), không phải nguyên tắc Nơi sinh — nếu cả cha lẫn mẹ đều là '
             'người nước ngoài, đứa trẻ sinh ra ở Hàn Quốc vẫn KHÔNG tự động trở thành công dân Hàn Quốc — nên D là câu SAI, '
             'đây là đáp án đúng.\n'
             'A, B, C đều là mô tả đúng về nguyên tắc quốc tịch huyết thống và điều kiện nhập tịch của Hàn Quốc.\n'
             'Lưu ý: tài liệu nguồn không liệt kê 3 phương án đúng còn lại — A, B, C là do Claude tự dựng lại.'
         )),
    dict(num=31, correct='B', options_source='reconstructed',
         stem=(
             '한국의 법 집행기관에 대한 설명으로 옳은 것을 <보기>에서 모두 고른 것은?\n'
             '<보기>\n'
             'ㄱ. 검찰은 범죄를 수사하고 기소하는 역할을 한다.\n'
             'ㄴ. 검찰은 도로에서 교통 단속을 담당한다.\n'
             'ㄷ. 경찰은 국민의 생명과 재산을 보호하는 역할을 한다.\n'
             'ㄹ. 경찰은 법정에서 형량을 결정한다.'
         ),
         options=[('A', 'ㄱ, ㄴ'), ('B', 'ㄱ, ㄷ'), ('C', 'ㄴ, ㄹ'), ('D', 'ㄷ, ㄹ')],
         explanation=(
             'ㄱ đúng: Viện kiểm sát (검찰) điều tra và khởi tố tội phạm. ㄷ đúng: Cảnh sát (경찰) bảo vệ tính mạng/tài sản của '
             'người dân — khớp với B.\n'
             'ㄴ sai: việc tuần tra giao thông là của Cảnh sát, không phải Viện kiểm sát.\n'
             'ㄹ sai: việc quyết định hình phạt tại tòa là của Thẩm phán, không phải Cảnh sát.\n'
             'Lưu ý: tài liệu nguồn không liệt kê nguyên văn 4 câu ㄱㄴㄷㄹ và 4 phương án tổ hợp — nội dung trên do Claude dựng '
             'lại, chỉ đáp án đúng (B) là chắc chắn khớp nguồn.'
         )),
    dict(num=32, correct='B', options_source='reconstructed',
         stem=(
             '고조선과 관련된 것을 <보기>에서 모두 고른 것은?\n'
             '<보기>\n'
             'ㄱ. 불교를 받아들여 국교로 삼았다.\n'
             'ㄴ. 8조법으로 사회 질서를 유지했다.\n'
             'ㄷ. 청동기 문화를 배경으로 성립되었다.\n'
             'ㄹ. 한글을 창제하여 사용하였다.\n'
             'ㅁ. 단군왕검이 세운 나라이다.'
         ),
         options=[('A', 'ㄱ, ㄴ, ㄷ'), ('B', 'ㄴ, ㄷ, ㅁ'), ('C', 'ㄷ, ㄹ, ㅁ'), ('D', 'ㄱ, ㄹ, ㅁ')],
         explanation=(
             'Gojoseon (고조선) do Dangun Wanggeom lập ra (ㅁ đúng), hình thành trên nền tảng văn hóa đồ đồng (ㄷ đúng), và xã '
             'hội được duy trì trật tự bằng Luật 8 điều — 8조법 (ㄴ đúng) — khớp với B.\n'
             'ㄱ sai: việc tiếp nhận Phật giáo làm quốc giáo là của các vương triều sau này (như Silla, Goguryeo), không phải '
             'Gojoseon.\n'
             'ㄹ sai: chữ Hangeul được vua Sejong triều Joseon sáng tạo, cách Gojoseon hàng nghìn năm.\n'
             'Lưu ý: tài liệu nguồn không liệt kê nguyên văn 5 câu ㄱㄴㄷㄹㅁ và 4 phương án tổ hợp — nội dung trên do Claude '
             'dựng lại, chỉ đáp án đúng (B) là chắc chắn khớp nguồn.'
         )),
    dict(num=33, correct='C', options_source='reconstructed',
         stem=(
             '<보기>\n'
             '(가) 3·1 운동 (1919년)\n'
             '(나) 8·15 광복 (1945년)\n'
             '(다) 대한제국 수립 (1897년)\n'
             '(라) 대한민국 임시정부 수립 (1919년, 3·1 운동 이후)\n'
             '<보기>를 시간 순서대로 배열한 것은?'
         ),
         options=[
             ('A', '(가)-(다)-(나)-(라)'),
             ('B', '(다)-(라)-(가)-(나)'),
             ('C', '(다)-(가)-(라)-(나)'),
             ('D', '(라)-(다)-(가)-(나)'),
         ],
         explanation=(
             'Thứ tự thời gian chính xác: Thành lập Đại Hàn Đế Quốc (1897) → Phong trào 3·1 (1/3/1919) → Thành lập Chính phủ '
             'lâm thời (11/4/1919, ngay sau phong trào 3·1) → Quang phục (15/8/1945) — khớp với C.\n'
             'A, B, D đều sắp xếp sai thứ tự thời gian giữa các sự kiện.'
         )),
    dict(num=34, correct='A', options_source='docx',
         stem='조선 시대의 과학 기술에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '백성들에게 세금을 많이 받기 위해 과학 기술을 중요하게 생각했다.'),
             ('B', '세종대왕은 해시계와 물시계를 만들었다.'),
             ('C', '세계 최초로 측우기를 발명했다.'),
             ('D', '거중기를 이용해 수원 화성 건설 기간을 단축했다.'),
         ],
         explanation=(
             'Thời Joseon (đặc biệt thời vua Sejong), khoa học công nghệ được phát triển nhằm mục đích hỗ trợ nông nghiệp và '
             'đời sống bách tính (ví dụ: máy đo lượng mưa để biết thời điểm gieo trồng), chứ không phải để thu nhiều thuế hơn '
             '— nên A là câu SAI, đây là đáp án đúng.\n'
             'B, C, D đều là thành tựu khoa học kỹ thuật có thật thời Joseon: đồng hồ mặt trời/nước do vua Sejong cho chế tạo, '
             'máy đo lượng mưa (측우기) đầu tiên trên thế giới, và cần cẩu (거중기) giúp rút ngắn thời gian xây thành Suwon '
             'Hwaseong.'
         )),
    dict(num=35, correct='C', options_source='docx',
         stem=(
             '<보기>: Bờ biển phía Tây và phía Nam Hàn Quốc có mực nước nông và chênh lệch thủy triều lớn nên ( ) rất phát '
             'triển. Đặc biệt ( ) ở bờ biển phía Tây là một trong 5 ( ) lớn nhất thế giới.\n'
             '<보기>의 ( )에 공통으로 들어갈 말은?'
         ),
         options=[('A', '산지'), ('B', '평야'), ('C', '갯벌'), ('D', '하천')],
         explanation=(
             'Bờ biển phía Tây Hàn Quốc nổi tiếng thế giới với các bãi bùn/bãi triều (갯벌) rộng lớn, hình thành do chênh lệch '
             'thủy triều (밀물과 썰물) rất lớn — khớp với C.\n'
             'A 산지(vùng núi), B 평야(đồng bằng), D 하천(sông ngòi) đều không liên quan đến hiện tượng thủy triều ven biển '
             'được mô tả.'
         )),
    dict(num=36, correct='C', options_source='docx',
         stem=(
             '<보기>: văn hóa ẩm thực phát triển / văn hóa truyền thống được bảo tồn tốt / gần đây giao lưu với Trung Quốc '
             'đang tăng lên\n'
             '<보기>의 내용과 가장 관계가 깊은 지역은?'
         ),
         options=[('A', '경기지역'), ('B', '강원지역'), ('C', '전라지역'), ('D', '경상지역')],
         explanation=(
             'Vùng Jeolla (전라지역, Tây Nam Hàn Quốc) nổi tiếng nhất cả nước về văn hóa ẩm thực phong phú, còn bảo tồn nhiều '
             'văn hóa truyền thống (như làng Hanok Jeonju, nghệ thuật Pansori), và gần đây tăng cường giao lưu thương mại với '
             'Trung Quốc qua các cảng như Gunsan — khớp với C.\n'
             'A(vùng Gyeonggi), B(vùng Gangwon), D(vùng Gyeongsang) đều không khớp với cả 3 đặc điểm nêu trên.'
         )),
]
