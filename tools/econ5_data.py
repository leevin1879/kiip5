# -*- coding: utf-8 -*-
# Question set built from "5단계_5-경제_종합평가_기출문제_—_Giải_thích_chi_tiết.docx".
# Same clean-table format as geo8/hist7/law6: each question stored as label/
# content/correct-or-not/reason, so almost everything is direct from the
# source. Q18/Q19 (matching-type questions — source only gives the reference
# mapping, not 4 multiple-choice combos) and Q20 (fill-in-the-blank, no
# options at all) needed Claude to build the other options.

QUESTIONS = [
    dict(num=1, correct='C', options_source='docx',
         stem='한국 경제가 빠르게 성장할 수 있었던 요인에 해당하지 않는 것은?',
         options=[
             ('A', '풍부한 노동력'),
             ('B', '뜨거운 교육열'),
             ('C', '풍부한 자본과 기술'),
             ('D', '경제 위기를 극복하겠다는 의지'),
         ],
         explanation=(
             'Hàn Quốc sau chiến tranh (1950-1953) không có vốn và công nghệ — tăng trưởng kinh tế ban đầu dựa vào '
             'lao động giá rẻ và viện trợ nước ngoài, không phải vốn và công nghệ sẵn có — nên C là câu trả lời '
             'đúng cho câu hỏi "không phải yếu tố".\n'
             'A, B, D đều là yếu tố thật giúp Hàn Quốc tăng trưởng nhanh: lực lượng lao động cần cù, nhiệt huyết '
             'giáo dục cao, và ý chí vượt qua khủng hoảng (ví dụ phong trào gom vàng năm 1997).'
         )),
    dict(num=2, correct='C', options_source='docx',
         stem='1980년대 한국의 대표적인 수출 품목은?',
         options=[('A', '가발'), ('B', '반도체'), ('C', '자동차'), ('D', '휴대폰')],
         explanation=(
             'Thập niên 1980s, Hàn Quốc bắt đầu xuất khẩu ô tô mạnh mẽ ra thị trường quốc tế (Hyundai, Kia) — khớp '
             'với C.\n'
             'A tóc giả là mặt hàng xuất khẩu chủ lực của thập niên 1960s. B chất bán dẫn trở thành mặt hàng xuất '
             'khẩu lớn từ thập niên 1990s-2000s. D điện thoại di động là mặt hàng xuất khẩu lớn từ thập niên 2000s.'
         )),
    dict(num=3, correct='C', options_source='docx',
         stem="'한강의 기적'에 대한 설명으로 옳은 것은?",
         options=[
             ('A', '한강을 이용해 경제 성장을 이루었다.'),
             ('B', '한강이 없었다면 경제 성장을 할 수 없었다.'),
             ('C', '세계가 놀랄 정도로 빠르게 경제 성장이 이루어졌다.'),
             ('D', '다른 나라의 도움을 받아 빠른 경제 발전을 이루었다.'),
         ],
         explanation=(
             '"한강의 기적" (Kỳ tích sông Hàn) là cách gọi cho việc kinh tế Hàn Quốc tăng trưởng nhanh đến mức cả '
             'thế giới phải kinh ngạc — khớp với C.\n'
             'A, B đều hiểu sai — tên gọi chỉ mang tính biểu tượng (Seoul nằm bên sông Hàn), không phải sông Hàn '
             'trực tiếp tạo ra tăng trưởng. D không phải ý nghĩa chính của cụm từ này.'
         )),
    dict(num=4, correct='A', options_source='docx',
         stem='다음 중 상설 시장에 해당하지 않는 것은?',
         options=[('A', '5일장'), ('B', '백화점'), ('C', '전통 시장'), ('D', '대형 마트')],
         explanation=(
             'Chợ phiên 5 ngày (5일장) chỉ họp vào các ngày cố định trong tháng, không mở cửa hàng ngày — đây là '
             'chợ truyền thống định kỳ (정기 시장), không phải thường trực (상설 시장) — nên A là đáp án đúng.\n'
             'B, C, D đều mở cửa hàng ngày, là chợ/cửa hàng thường trực thật sự.'
         )),
    dict(num=5, correct='D', options_source='docx',
         stem='한국에서 화폐를 발행하는 은행은?',
         options=[('A', '국민은행'), ('B', '우리은행'), ('C', '농협은행'), ('D', '한국은행')],
         explanation=(
             'Ngân hàng Trung ương Hàn Quốc (한국은행/Bank of Korea) là cơ quan duy nhất có quyền phát hành tiền tệ '
             'tại Hàn Quốc — khớp với D.\n'
             'A, B, C đều là ngân hàng thương mại/nông nghiệp, không có quyền phát hành tiền.'
         )),
    dict(num=6, correct='B', options_source='docx',
         stem='24시간 문을 열며 식료품과 간단한 생활용품을 파는 곳은?',
         options=[('A', '3일장'), ('B', '편의점'), ('C', '백화점'), ('D', '슈퍼마켓')],
         explanation=(
             'Cửa hàng tiện lợi (편의점) như GS25, CU, 7-Eleven mở cửa 24/7, bán thực phẩm và đồ dùng thiết yếu — '
             'khớp với B.\n'
             'A chợ phiên họp định kỳ, không mở 24 giờ. C bách hóa không mở 24 giờ và không chuyên bán thực phẩm. '
             'D siêu thị nhỏ thường không mở 24 giờ.'
         )),
    dict(num=7, correct='A', options_source='docx',
         stem='은행에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '시중은행에는 신한은행, 국민은행, 제주은행이 있다.'),
             ('B', '은행이란 일반적으로 시중은행과 지방은행을 말한다.'),
             ('C', '대표적인 상품으로 보통예금 정기적금 정기예금이 있다.'),
             ('D', '인터넷, 스마트폰, 현금 인출기에서도 금융 거래를 할 수 있다.'),
         ],
         explanation=(
             'Ngân hàng Jeju (제주은행) là ngân hàng ĐỊA PHƯƠNG (지방은행), không phải ngân hàng thương mại toàn quốc '
             '(시중은행) — các ngân hàng thương mại lớn gồm Kookmin, Shinhan, Hana, Woori, SC제일은행... — nên A là '
             'câu SAI, đây là đáp án đúng.\n'
             'B, C, D đều là mô tả đúng về hệ thống ngân hàng Hàn Quốc.'
         )),
    dict(num=8, correct='D', options_source='docx',
         stem='최근 스마트폰 사용 증가와 함께 사용이 늘고 있는 결제 수단은?',
         options=[('A', '수표'), ('B', '신용카드'), ('C', '체크카드'), ('D', '모바일 간편 결제')],
         explanation=(
             'Thanh toán di động (모바일 간편 결제) như KakaoPay, Samsung Pay, Naver Pay đang tăng mạnh cùng với sự '
             'phổ biến của smartphone — khớp với D.\n'
             'A không liên quan đến thanh toán qua smartphone. B, C (thẻ tín dụng/ghi nợ) đã phổ biến trước khi '
             'smartphone ra đời, không đặc biệt gắn với sự tăng trưởng của smartphone.'
         )),
    dict(num=9, correct='C', options_source='docx',
         stem='한국에서는 금융 기관이 망해도 예금자 보호법에 따라 원금과 이자를 합쳐 1인당 최고 ( )까지는 보호받을 수 있다.',
         options=[('A', '3천만 원'), ('B', '4천만 원'), ('C', '5천만 원'), ('D', '1억 원')],
         explanation=(
             'Theo Luật Bảo vệ người gửi tiền (예금자 보호법) của Hàn Quốc, mỗi người được bảo vệ tối đa 50 triệu won '
             '(5천만 원), bao gồm cả gốc và lãi, tại một tổ chức tài chính — khớp với C.\n'
             'A, B đều thấp hơn mức bảo vệ thực tế. D vượt quá mức bảo vệ theo luật hiện hành.'
         )),
    dict(num=10, correct='C', options_source='docx',
         stem='일정한 금액을 정기적으로 입금하고 만기일에 원금과 이자를 한꺼번에 받는 상품은?',
         options=[('A', '주식'), ('B', '정기예금'), ('C', '정기적금'), ('D', '보통예금')],
         explanation=(
             'Tiết kiệm định kỳ (정기적금): gửi một khoản tiền cố định hàng tháng, đến ngày đáo hạn nhận cả gốc lẫn '
             'lãi một lần — sản phẩm phù hợp để tích lũy dần — khớp với C.\n'
             'A cổ phiếu là đầu tư, không phải sản phẩm tiết kiệm định kỳ. B tiền gửi có kỳ hạn là gửi MỘT LẦN số '
             'tiền lớn, không phải gửi định kỳ hàng tháng. D tiền gửi thông thường có thể rút bất cứ lúc nào, '
             'không có kỳ hạn cố định.'
         )),
    dict(num=11, correct='D', options_source='docx',
         stem='시대별로 주요 수출 품목이 바르게 연결된 것은?',
         options=[
             ('A', '1960년대 - 철강, 배'),
             ('B', '1970년대 - 가발, 신발'),
             ('C', '1980년대 - 자동차, 신발'),
             ('D', '2000년대 - 반도체, 휴대폰'),
         ],
         explanation=(
             'Thập niên 2000s, Hàn Quốc xuất khẩu mạnh chất bán dẫn (반도체) và điện thoại di động (휴대폰) — Samsung, '
             'LG trở thành thương hiệu toàn cầu — khớp với D.\n'
             'A sai: thập niên 1960s xuất khẩu chủ yếu là tóc giả, quần áo, giày dép — thép và tàu là thập niên '
             '1970s-80s.\n'
             'B sai: tóc giả và giày dép là thập niên 1960s — thập niên 1970s là thép, tàu, hóa chất.\n'
             'C sai: thập niên 1980s chủ yếu là ô tô và điện tử — giày dép đã giảm.'
         )),
    dict(num=12, correct='B', options_source='docx',
         stem='과거에는 국제사회의 원조를 받는 나라였다가 이제는 다른 나라를 원조하게 된 최초의 나라라고 평가를 받는 나라는?',
         options=[('A', '중국'), ('B', '한국'), ('C', '베트남'), ('D', '우즈베키스탄')],
         explanation=(
             'Hàn Quốc là quốc gia đầu tiên trên thế giới chuyển từ vị thế "nước nhận viện trợ" (수원국) sang "nước '
             'đi viện trợ" (공여국), trở thành thành viên DAC (Ủy ban Hỗ trợ Phát triển) của OECD — khớp với B.\n'
             'A, C, D đều không có lịch sử chuyển đổi vị thế tương tự Hàn Quốc.'
         )),
    dict(num=13, correct='B', options_source='docx',
         stem='물건을 구입하는 도중에나 그 후에 피해를 입은 소비자를 도와주는 전문기관은?',
         options=[('A', '금융실명제'), ('B', '한국소비자원'), ('C', '예금자 보호제도'), ('D', '외국인근로자지원센터')],
         explanation=(
             '한국소비자원 (Viện Người tiêu dùng Hàn Quốc) là cơ quan chuyên môn hỗ trợ người tiêu dùng bị thiệt hại '
             'khi mua sắm, giải quyết khiếu nại và bảo vệ quyền lợi người tiêu dùng — khớp với B.\n'
             'A là một chế độ tài chính, không phải cơ quan hỗ trợ người tiêu dùng. C là chế độ bảo vệ tiền gửi '
             'ngân hàng, không liên quan đến mua sắm. D hỗ trợ lao động nước ngoài, không phải người tiêu dùng '
             'nói chung.'
         )),
    dict(num=14, correct='A', options_source='docx',
         stem='수출이나 수입을 할 때 관세를 줄이거나 없애서 무역을 활발하게 하도록 하는 것은?',
         options=[('A', '자유무역협정'), ('B', '제조물 책임법'), ('C', '예금자 보호제도'), ('D', '경제협력개발기구')],
         explanation=(
             'FTA (자유무역협정, Hiệp định Thương mại Tự do) là hiệp định giữa các quốc gia nhằm giảm hoặc xóa bỏ '
             'thuế quan (관세), thúc đẩy thương mại tự do — khớp với A.\n'
             'B quy định trách nhiệm của nhà sản xuất đối với sản phẩm lỗi, không liên quan đến thương mại quốc '
             'tế. C là chế độ tài chính trong nước. D (OECD) là tổ chức hợp tác kinh tế, không phải hiệp định '
             'thương mại.'
         )),
    dict(num=15, correct='C', options_source='docx',
         stem='한국의 실업률이 미국이나 유럽에 비해서 낮은 이유는?',
         options=[
             ('A', '비정규직 노동자의 비율이 점점 낮아지고 있기 때문이다.'),
             ('B', '실업에 대한 사회보장제도가 잘 이루어져 있기 때문이다.'),
             ('C', '여성의 경제 활동 참여율이 적고 자영업자가 많기 때문이다.'),
             ('D', '예전에 비하여 근로 조건이 좋은 일자리가 늘어났기 때문이다.'),
         ],
         explanation=(
             'Tỷ lệ tham gia kinh tế của phụ nữ thấp và có nhiều người tự kinh doanh (자영업자) khiến tỷ lệ thất '
             'nghiệp CHÍNH THỨC (thống kê) của Hàn Quốc thấp hơn — khớp với C.\n'
             'A, B, D đều không phải lý do thực tế — tỷ lệ lao động không chính thức không giảm, chế độ an sinh '
             'thất nghiệp chưa hoàn thiện bằng phương Tây, và việc làm tốt không tăng đáng kể.'
         )),
    dict(num=16, correct='C', options_source='docx',
         stem='취업 준비를 하는 자세로 옳지 않은 것은?',
         options=[
             ('A', '전문성을 갖추기 위해 자격증을 취득한다.'),
             ('B', '구직이나 구인 정보에 많은 관심을 가진다.'),
             ('C', '구직 중 문제가 발생하면 출입국·외국인청과 상담한다.'),
             ('D', '원하는 직업을 찾고 필요한 능력을 갖추기 위해 노력한다.'),
         ],
         explanation=(
             'Khi gặp vấn đề trong quá trình tìm việc (như bị lừa đảo, vi phạm hợp đồng), nên liên hệ với Trung '
             'tâm Hỗ trợ Lao động Nước ngoài (외국인근로자지원센터) hoặc Bộ Lao động (고용노동부), không phải Cục Xuất '
             'nhập cảnh (출입국·외국인청) vốn chuyên về visa và cư trú — nên C là câu SAI, đây là đáp án đúng.\n'
             'A, B, D đều là thái độ chuẩn bị việc làm đúng đắn: lấy chứng chỉ nâng cao chuyên môn, theo dõi thông '
             'tin tuyển dụng, nỗ lực phát triển bản thân.'
         )),
    dict(num=17, correct='C', options_source='docx',
         stem='대표적인 저축 상품에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '자유롭게 돈을 넣고 빼서 쓸 수 있는 것은 보통예금이다.'),
             ('B', '매달 일정 금액을 일정 기간 동안 적립하는 것은 정기적금이다.'),
             ('C', '은행보다 안전하고 많은 이익을 얻을 수 있는 것은 보험예금이다.'),
             ('D', '일정 기간 동안 돌려받지 않을 것을 약속하고 돈을 맡기는 것은 정기예금이다.'),
         ],
         explanation=(
             'Không có sản phẩm nào gọi là "보험예금" (bảo hiểm tiền gửi) — bảo hiểm (보험) và tiền gửi (예금) là hai '
             'loại sản phẩm tài chính khác nhau. Hơn nữa, không sản phẩm nào "an toàn hơn ngân hàng và lợi nhuận '
             'cao hơn" cùng lúc — đây là mâu thuẫn với nguyên tắc tài chính cơ bản (rủi ro cao = lợi nhuận cao) — '
             'nên C là câu SAI, đây là đáp án đúng.\n'
             'A, B, D đều là mô tả đúng về tiền gửi thông thường, tiết kiệm định kỳ, và tiền gửi có kỳ hạn.'
         )),
    dict(num=18, correct='A', options_source='reconstructed',
         stem=(
             '<보기>\n(가) 리콜제도  (나) 의무표시제  (다) 제조물 책임법\n'
             'ㄱ. 상품에 대한 책임을 제조업체가 진다\nㄴ. 생산자가 소비자에게 상품의 문제를 알려주고 수리, 교환해 '
             '준다\nㄷ. 원산지 표시, 유통 기한, 영양 성분 표시 등 소비자의 안전에 중요한 표시를 반드시 하도록 한다\n'
             '<보기>의 제도와 설명을 알맞게 연결한 것은?'
         ),
         options=[
             ('A', '(가)-ㄴ, (나)-ㄷ, (다)-ㄱ'),
             ('B', '(가)-ㄱ, (나)-ㄴ, (다)-ㄷ'),
             ('C', '(가)-ㄷ, (나)-ㄱ, (다)-ㄴ'),
             ('D', '(가)-ㄴ, (나)-ㄱ, (다)-ㄷ'),
         ],
         explanation=(
             '리콜제도 (Chế độ thu hồi sản phẩm): khi phát hiện lỗi sản phẩm, nhà sản xuất phải chủ động thông báo '
             'và thu hồi/sửa chữa/đổi mới cho người tiêu dùng (ㄴ). 의무표시제 (Chế độ ghi nhãn bắt buộc): bắt buộc '
             'ghi xuất xứ, hạn sử dụng, thành phần dinh dưỡng... để bảo vệ người tiêu dùng (ㄷ). 제조물 책임법 (Luật '
             'Trách nhiệm sản phẩm): quy định nhà sản xuất phải bồi thường khi sản phẩm gây thiệt hại (ㄱ) — khớp '
             'với A.\n'
             'B, C, D đều ghép sai ít nhất một cặp chế độ-giải thích.\n'
             'Lưu ý: tài liệu nguồn chỉ cho bảng ghép đôi đúng (không có sẵn 4 phương án trắc nghiệm dạng câu hỏi '
             'thi) — B, C, D là do Claude tự dựng lại bằng cách hoán đổi các cặp trong bảng gốc.'
         )),
    dict(num=19, correct='A', options_source='reconstructed',
         stem=(
             '<보기>\n(가) 재화  (나) 물가  (다) 서비스\n'
             'ㄱ. 물건 배달, 의사의 진료 등과 같은 무형의 활동이다\nㄴ. 상품과 서비스의 가치를 종합하여 계산한 평균 '
             '가격이다\nㄷ. 스마트폰, 화장품처럼 눈에 보이고 만질 수 있는 상품이다\n'
             '<보기>의 용어와 설명을 알맞게 연결한 것은?'
         ),
         options=[
             ('A', '(가)-ㄷ, (나)-ㄴ, (다)-ㄱ'),
             ('B', '(가)-ㄱ, (나)-ㄷ, (다)-ㄴ'),
             ('C', '(가)-ㄴ, (나)-ㄱ, (다)-ㄷ'),
             ('D', '(가)-ㄷ, (나)-ㄱ, (다)-ㄴ'),
         ],
         explanation=(
             '재화 (Hàng hóa): sản phẩm hữu hình có thể chạm vào được như điện thoại, mỹ phẩm (ㄷ). 물가 (Mức giá): '
             'mức giá trung bình chung của hàng hóa và dịch vụ trong nền kinh tế (ㄴ). 서비스 (Dịch vụ): hoạt động '
             'vô hình tạo ra giá trị như vận chuyển, khám bệnh (ㄱ) — khớp với A.\n'
             'B, C, D đều ghép sai ít nhất một cặp thuật ngữ-giải thích.\n'
             'Lưu ý: tài liệu nguồn chỉ cho bảng ghép đôi đúng (không có sẵn 4 phương án trắc nghiệm dạng câu hỏi '
             'thi) — B, C, D là do Claude tự dựng lại bằng cách hoán đổi các cặp trong bảng gốc.'
         )),
    dict(num=20, correct='A', options_source='reconstructed',
         stem='은행 계좌를 만들 때 본인이 은행을 직접 방문해서 자신의 이름으로 금융 거래를 해야만 하는 제도는?',
         options=[('A', '금융실명제'), ('B', '예금자 보호제도'), ('C', '신용카드제도'), ('D', '전자상거래법')],
         explanation=(
             'Chế độ giao dịch tài chính bằng tên thật (금융실명제) yêu cầu tất cả các giao dịch tài chính phải được '
             'thực hiện bằng tên thật của người giao dịch — khi mở tài khoản, người dùng phải đến trực tiếp ngân '
             'hàng và xác minh danh tính — chế độ này áp dụng từ năm 1993 nhằm ngăn chặn tham nhũng, trốn thuế và '
             'rửa tiền — khớp với A.\n'
             'B là chế độ bảo vệ tiền gửi khi ngân hàng phá sản, không liên quan đến việc xác minh danh tính khi '
             'mở tài khoản. C, D là các chế độ tài chính/thương mại khác, không liên quan trực tiếp.\n'
             'Lưu ý: tài liệu nguồn chỉ cho đáp án đúng dạng điền từ, không có sẵn 4 phương án trắc nghiệm — B, C, '
             'D là do Claude tự dựng lại để tăng tính thử thách.'
         )),
]
