# -*- coding: utf-8 -*-
# Question set built from "5단계_6-법_종합평가_기출문제_—_Giải_thích_chi_tiết.docx".
# Same clean-table format as geo8/hist7: each question stored as label/content/
# correct-or-not/reason, so almost everything is direct from the source.
# Q12/Q13 (matching-type questions — source only gives the reference mapping,
# not 4 multiple-choice combos) and Q19-20 (fill-in-the-blank, no options at
# all) needed Claude to build the other options.

QUESTIONS = [
    dict(num=1, correct='A', options_source='docx',
         stem='개인 간에 발생하는 문제를 해결하기 위한 재판은?',
         options=[('A', '민사 재판'), ('B', '형사 재판'), ('C', '가사 재판'), ('D', '행정 재판')],
         explanation=(
             'Tòa dân sự (민사 재판) giải quyết các tranh chấp giữa cá nhân với cá nhân, như tranh chấp tài sản, hợp '
             'đồng, bồi thường thiệt hại — khớp với A.\n'
             'B Tòa hình sự xử lý các vụ phạm tội hình sự. C Tòa gia đình xử lý các vụ liên quan đến hôn nhân, ly '
             'hôn, nuôi con. D Tòa hành chính xử lý tranh chấp giữa cá nhân và cơ quan nhà nước.'
         )),
    dict(num=2, correct='A', options_source='docx',
         stem='검찰과 경찰의 공통점에 해당하는 것은?',
         options=[
             ('A', '범죄에 대한 수사를 한다.'),
             ('B', '재판 과정에 직접 참여한다.'),
             ('C', '범죄자에 대한 재판을 청구한다.'),
             ('D', '범죄자에 대한 처벌을 요구한다.'),
         ],
         explanation=(
             'Cả Cảnh sát (경찰) và Viện Kiểm sát (검찰) đều có quyền điều tra tội phạm — đây là điểm chung duy nhất '
             '— khớp với A.\n'
             'B chỉ Viện Kiểm sát mới trực tiếp tham gia phiên tòa với tư cách công tố viên. C chỉ Viện Kiểm sát '
             'mới có quyền đề nghị truy tố (기소). D là chức năng của Viện Kiểm sát tại phiên tòa, không phải của '
             'Cảnh sát.'
         )),
    dict(num=3, correct='D', options_source='docx',
         stem='대한민국 국적법에서 국적 취득의 중요한 기준이 되는 것은?',
         options=[('A', '태어난 곳'), ('B', '재산 정도'), ('C', '출생증명서'), ('D', '부모의 국적')],
         explanation=(
             'Hàn Quốc áp dụng nguyên tắc "Quyền theo huyết thống" (혈통주의/속인주의) — quốc tịch của đứa trẻ được '
             'xác định dựa trên quốc tịch của cha hoặc mẹ — khớp với D.\n'
             'A là nguyên tắc "quyền theo nơi sinh" (출생지주의), không phải nguyên tắc chính của Hàn Quốc. B tài sản '
             'không phải tiêu chí xác định quốc tịch. C giấy khai sinh chỉ là tài liệu, không phải tiêu chí.'
         )),
    dict(num=4, correct='C', options_source='docx',
         stem='학생을 대상으로 학교 안팎에서 신체적, 정신적, 재산상의 피해를 주는 행위는?',
         options=[('A', '음주 운전자'), ('B', '가정 폭력'), ('C', '학교 폭력'), ('D', '무단 투기')],
         explanation=(
             'Bạo lực học đường (학교 폭력) là hành vi gây tổn hại về thể chất, tinh thần hoặc tài sản cho học sinh '
             'trong và ngoài phạm vi trường học — khớp với C.\n'
             'A không liên quan đến hành vi gây hại cho học sinh tại trường. B bạo lực gia đình xảy ra trong phạm '
             'vi gia đình, không phải tại trường. D là hành vi vi phạm môi trường, không liên quan.'
         )),
    dict(num=5, correct='B', options_source='reconstructed',
         stem=(
             '<보기>\n· 한국에 3년 이상 계속 주소가 있고 부모 중 한 사람이 한국인이었던 사람\n· 한국인과 결혼하여 '
             '한국에서 2년 이상 계속 거주하고 있는 사람\n이러한 사람들이 신청할 수 있는 것은?'
         ),
         options=[('A', '특별귀화'), ('B', '간이귀화'), ('C', '일반귀화'), ('D', '보통귀화')],
         explanation=(
             'Nhập tịch giản lược (간이귀화) áp dụng cho người có liên hệ với Hàn Quốc qua huyết thống hoặc hôn nhân, '
             'yêu cầu thời gian cư trú ngắn hơn (2-3 năm) so với nhập tịch thông thường (5 năm) — khớp với B.\n'
             'A đặc biệt dành cho người có công lao đặc biệt với Hàn Quốc. C yêu cầu cư trú liên tục 5 năm. D không '
             'phải thuật ngữ chính thức trong luật quốc tịch Hàn Quốc.\n'
             'Lưu ý: tài liệu nguồn không liệt kê nguyên văn <보기> — nội dung trên do Claude viết lại theo đúng ý '
             'đã nêu trong giải thích.'
         )),
    dict(num=6, correct='C', options_source='reconstructed',
         stem=(
             '<보기>\n돈을 빌려줄 때는 ( )을/를 작성하는 것이 좋다. 여기에는 빌려주는 사람과 빌리는 사람의 이름, '
             '주소, 전화번호, 원금, 이자율, 거래 날짜, 서명 등을 반드시 적어야 한다.\n다음 빈칸에 공통으로 들어갈 '
             '단어는?'
         ),
         options=[('A', '사증'), ('B', '영수증'), ('C', '차용증'), ('D', '보증서')],
         explanation=(
             'Giấy vay nợ (차용증) là văn bản ghi rõ thông tin người vay, người cho vay, số tiền, lãi suất, ngày '
             'giao dịch và chữ ký — tài liệu pháp lý quan trọng khi cho vay tiền — khớp với C.\n'
             'A Visa là giấy phép nhập cảnh, không liên quan. B biên lai dùng để xác nhận đã nhận tiền/hàng, không '
             'phải giấy vay nợ. D giấy bảo lãnh là văn bản của người thứ ba cam kết trả nợ thay.'
         )),
    dict(num=7, correct='C', options_source='docx',
         stem='부동산에 대한 권리 관계를 보여주는 문서는?',
         options=[('A', '계약서'), ('B', '확인설명서'), ('C', '등기부 등본'), ('D', '주민등록 등본')],
         explanation=(
             'Sổ đăng ký bất động sản (등기부 등본) là tài liệu pháp lý chính thức ghi rõ quyền sở hữu, thế chấp và '
             'các quyền liên quan đến bất động sản — khớp với C.\n'
             'A hợp đồng ghi lại thỏa thuận, không phải tài liệu chứng minh quyền sở hữu. B là tài liệu môi giới '
             'cung cấp thông tin, không phải tài liệu quyền sở hữu. D chỉ ghi thông tin nơi cư trú.'
         )),
    dict(num=8, correct='D', options_source='docx',
         stem='부부가 각자 자신의 재산을 가질 수 있고 자신의 뜻에 따라 그 재산을 처분할 수 있는 권리는?',
         options=[('A', '협의 이혼'), ('B', '재산 분할'), ('C', '면접 교섭권'), ('D', '부부 별산제')],
         explanation=(
             'Chế độ tài sản riêng (부부 별산제) là nguyên tắc mỗi vợ/chồng có quyền sở hữu và tự do định đoạt tài '
             'sản riêng của mình trong hôn nhân — khớp với D.\n'
             'A là hình thức ly hôn, không phải quyền về tài sản. B là quyền khi ly hôn, không phải quyền sở hữu '
             'tài sản riêng trong hôn nhân. C là quyền của cha/mẹ không nuôi con được thăm con sau ly hôn.'
         )),
    dict(num=9, correct='D', options_source='docx',
         stem='외국인이 한국에 체류하려고 할 때 옳지 않은 것은?',
         options=[
             ('A', '체류지를 변경했을 때는 반드시 체류지 변경 신고를 해야 한다.'),
             ('B', '외국인등록과 체류지 변경 신고는 출입국·외국인청에서 할 수 있다.'),
             ('C', '한국에 머무르는 기간에 따라 단기체류자와 장기체류자로 나눌 수 있다.'),
             ('D', '90일을 초과하여 한국에 체류하려면 입국하자마자 외국인등록을 해야 한다.'),
         ],
         explanation=(
             'Người nước ngoài dự định lưu trú trên 90 ngày phải đăng ký ngoại kiều TRONG VÒNG 90 ngày kể từ ngày '
             'nhập cảnh, không phải "ngay khi vừa nhập cảnh" (입국하자마자) — nên D là câu SAI, đây là đáp án đúng.\n'
             'A, B, C đều là mô tả đúng: phải khai báo khi thay đổi nơi cư trú, cơ quan có thẩm quyền là Cục Xuất '
             'nhập cảnh và Người nước ngoài, và có thể phân loại theo thời gian lưu trú.'
         )),
    dict(num=10, correct='A', options_source='docx',
         stem='이혼에 대한 설명으로 옳은 것은?',
         options=[
             ('A', '이혼에는 협의 이혼과 재판상 이혼이 있다.'),
             ('B', '부부 간의 합의가 없을 경우에는 이혼할 수 없다.'),
             ('C', '원인을 제공하고 잘못이 있는 배우자는 자녀를 만날 수 없다.'),
             ('D', '부부 모두 이혼을 원하면 고등법원이나 대법원에서 이혼할 수 있다.'),
         ],
         explanation=(
             'Hàn Quốc có 2 hình thức ly hôn: Ly hôn thuận tình (협의 이혼) khi cả hai đồng ý, và Ly hôn theo phán '
             'quyết tòa án (재판상 이혼) khi một bên không đồng ý — khớp với A.\n'
             'B sai: khi không có sự đồng ý của cả hai bên, vẫn có thể ly hôn qua tòa án nếu có lý do chính đáng.\n'
             'C sai: ngay cả người có lỗi trong hôn nhân vẫn có quyền thăm con (면접 교섭권) sau ly hôn.\n'
             'D sai: khi cả hai đồng ý ly hôn, thủ tục được thực hiện tại Tòa án gia đình (가정법원), không phải '
             'Tòa cấp cao hay Tòa tối cao.'
         )),
    dict(num=11, correct='A', options_source='docx',
         stem='법을 통해 권리를 보장받는 소송에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '모든 분쟁을 재판으로 해결하는 것이 가장 바람직하다.'),
             ('B', '법원의 판사는 법률에 따라 공정하게 판결을 내려 분쟁을 해결한다.'),
             ('C', '개인 간의 재산문제, 가족문제, 세금문제 등을 소송으로 해결할 수 있다.'),
             ('D', '재판 과정에서는 변호사나 대한법률구조공단의 도움을 받는 것이 바람직하다.'),
         ],
         explanation=(
             'Không phải mọi tranh chấp đều cần giải quyết bằng tòa án. Trên thực tế, các phương thức giải quyết '
             'thay thế (ADR) như hòa giải (조정), thương lượng (협상), trọng tài (중재) thường được khuyến khích vì '
             'nhanh hơn, ít tốn kém hơn và ít căng thẳng hơn — nên A là câu SAI, đây là đáp án đúng.\n'
             'B, C, D đều là mô tả đúng về chức năng của tòa án và quyền được tư vấn pháp lý.'
         )),
    dict(num=12, correct='A', options_source='reconstructed',
         stem=(
             '<보기>\n(가) 국가인권위원회  (나) 국민권익위원회  (다) 외국인지원센터\n'
             'ㄱ. 기본적인 인권을 위한 국가기관이다\nㄴ. 국가기관으로 인한 피해를 구제한다\n'
             'ㄷ. 이민자나 외국인의 권리 보호를 돕는다\n'
             '<보기>의 기관과 설명을 알맞게 연결한 것은?'
         ),
         options=[
             ('A', '(가)-ㄱ, (나)-ㄴ, (다)-ㄷ'),
             ('B', '(가)-ㄴ, (나)-ㄱ, (다)-ㄷ'),
             ('C', '(가)-ㄱ, (나)-ㄷ, (다)-ㄴ'),
             ('D', '(가)-ㄷ, (나)-ㄴ, (다)-ㄱ'),
         ],
         explanation=(
             '국가인권위원회 (Ủy ban Nhân quyền Quốc gia) là cơ quan nhà nước độc lập bảo vệ nhân quyền cơ bản (ㄱ). '
             '국민권익위원회 (Ủy ban Quyền lợi Nhân dân) giải quyết khiếu nại, tố cáo về hành vi sai trái của cơ quan '
             'nhà nước, tức "cứu trợ thiệt hại do cơ quan nhà nước gây ra" (ㄴ). 외국인지원센터 (Trung tâm Hỗ trợ '
             'Người nước ngoài) cung cấp thông tin, bảo vệ quyền lợi người nhập cư/người nước ngoài (ㄷ) — khớp với A.\n'
             'B, C, D đều ghép sai ít nhất một cặp cơ quan-chức năng.\n'
             'Lưu ý: tài liệu nguồn chỉ cho bảng ghép đôi đúng (không có sẵn 4 phương án trắc nghiệm dạng câu hỏi '
             'thi) — B, C, D là do Claude tự dựng lại bằng cách hoán đổi các cặp trong bảng gốc.'
         )),
    dict(num=13, correct='A', options_source='reconstructed',
         stem=(
             '<보기>\n(가) 협상  (나) 조정  (다) 중재\n'
             'ㄱ. 제3자가 모든 권한을 부여받아 강제로 해결한다\nㄴ. 자발적으로 합의하고 대화로 해결한다\n'
             'ㄷ. 제3자가 참여해서 조언이나 자문을 제공한다\n'
             '<보기>의 용어와 의미를 알맞게 연결한 것은?'
         ),
         options=[
             ('A', '(가)-ㄴ, (나)-ㄷ, (다)-ㄱ'),
             ('B', '(가)-ㄱ, (나)-ㄴ, (다)-ㄷ'),
             ('C', '(가)-ㄷ, (나)-ㄱ, (다)-ㄴ'),
             ('D', '(가)-ㄴ, (나)-ㄱ, (다)-ㄷ'),
         ],
         explanation=(
             '협상 (Thương lượng): hai bên tự nguyện đàm phán trực tiếp để đạt thỏa thuận, không cần bên thứ ba (ㄴ). '
             '조정 (Hòa giải): bên thứ ba tham gia hỗ trợ, đưa ra gợi ý/tư vấn nhưng không quyết định thay (ㄷ). '
             '중재 (Trọng tài): bên thứ ba được trao quyền đưa ra phán quyết có tính ràng buộc, bắt buộc các bên '
             'phải tuân theo (ㄱ) — khớp với A.\n'
             'B, C, D đều ghép sai ít nhất một cặp thuật ngữ-ý nghĩa.\n'
             'Lưu ý: tài liệu nguồn chỉ cho bảng ghép đôi đúng (không có sẵn 4 phương án trắc nghiệm dạng câu hỏi '
             'thi) — B, C, D là do Claude tự dựng lại bằng cách hoán đổi các cặp trong bảng gốc.'
         )),
    dict(num=14, correct='B', options_source='docx',
         stem='태어난 아이의 국적을 결정할 때 부모가 가진 국적을 기준으로 아이의 국적을 결정하는 것은?',
         options=[('A', '속지주의'), ('B', '혈통주의'), ('C', '출생지주의'), ('D', '죄형법정주의')],
         explanation=(
             'Nguyên tắc huyết thống (혈통주의/속인주의): quốc tịch của đứa trẻ được xác định dựa trên quốc tịch của '
             'cha hoặc mẹ — Hàn Quốc áp dụng nguyên tắc này — khớp với B.\n'
             'A, C đều là nguyên tắc xác định quốc tịch theo NƠI SINH, ngược lại với nguyên tắc huyết thống. D '
             '(nguyên tắc pháp định hình sự — "không có tội nếu không có luật") thuộc lĩnh vực luật hình sự, không '
             'liên quan đến quốc tịch.'
         )),
    dict(num=15, correct='D', options_source='docx',
         stem='다음 중 가정 폭력의 예로 옳지 않은 것은?',
         options=[
             ('A', '가족에게 물건을 던지거나 때리는 것'),
             ('B', '가족에게 욕설을 하거나 협박하는 것'),
             ('C', '어린이나 노인을 제대로 돌보지 않는 것'),
             ('D', '청소, 빨래, 요리 등 가사노동을 하지 않는 것'),
         ],
         explanation=(
             'Không làm việc nhà (가사노동 거부) không được pháp luật Hàn Quốc định nghĩa là bạo lực gia đình — bạo '
             'lực gia đình phải là hành vi CHỦ ĐỘNG gây hại, không phải hành vi thụ động không làm việc — nên D là '
             'đáp án đúng cho câu hỏi "không phải bạo lực".\n'
             'A là bạo lực thể chất (신체적 폭력). B là bạo lực tinh thần/ngôn ngữ (정신적/언어적 폭력). C (bỏ bê, sao '
             'nhãng — 방임) cũng là một hình thức bạo lực gia đình.'
         )),
    dict(num=16, correct='B', options_source='docx',
         stem='법의식에 대한 설명으로 옳은 것은?',
         options=[
             ('A', '안전한 사회가 되면 법을 잘 지키게 된다.'),
             ('B', '법을 잘 지키는 정신을 준법정신이라고 한다.'),
             ('C', '법은 지키는 것보다 잘 만드는 것이 더 중요하다.'),
             ('D', '외국인은 한국의 법을 잘 모르므로 안 지켜도 된다.'),
         ],
         explanation=(
             'Tinh thần tuân thủ pháp luật gọi là "준법정신" (tinh thần tuân pháp) — đây là khái niệm cơ bản trong '
             'giáo dục pháp luật — khớp với B.\n'
             'A sai: thực ra ngược lại — chính việc mọi người tuân thủ pháp luật mới tạo ra xã hội an toàn.\n'
             'C sai: cả việc làm luật tốt lẫn tuân thủ luật đều quan trọng như nhau, luật tốt mà không ai tuân thủ '
             'thì vô nghĩa.\n'
             'D sai: nguyên tắc pháp lý cơ bản là "không biết luật không được miễn trách nhiệm" — người nước ngoài '
             'sống tại Hàn Quốc vẫn phải tuân thủ luật pháp Hàn Quốc.'
         )),
    dict(num=17, correct='D', options_source='docx',
         stem='정의로운 법을 만들도록 노력해야 하는 이유는?',
         options=[
             ('A', '외국인은 헌법소원을 청구할 수 없기 때문이다.'),
             ('B', '국회에서 국민의 뜻에 따라 법을 만들기 때문이다.'),
             ('C', '국민의 기본권이나 인권이 자주 침해되기 때문이다.'),
             ('D', '정의로운 법을 통해 정의로운 사회가 될 수 있기 때문이다.'),
         ],
         explanation=(
             'Mục đích cốt lõi của việc nỗ lực làm ra pháp luật công bằng là để xây dựng một xã hội công bằng — '
             'khớp trực tiếp với D.\n'
             'A không đúng thực tế (người nước ngoài có những quyền khiếu nại nhất định tùy trường hợp) và không '
             'phải lý do cần làm luật công bằng. B mô tả QUY TRÌNH lập pháp, không phải LÝ DO cần luật công bằng. '
             'C là một vấn đề cần giải quyết chứ không phải lý do/mục đích của việc làm luật công bằng.'
         )),
    dict(num=18, correct='A', options_source='docx',
         stem='다음 중 일반귀화의 조건이 아닌 것은?',
         options=[
             ('A', '한국에서 3년 이상 생활할 것'),
             ('B', '영주(F-5) 자격을 가지고 있는 외국인'),
             ('C', '한국에 주소가 있는 만 19세 이상의 외국인'),
             ('D', '품행이 단정하고 생계유지능력이 있는 외국인'),
         ],
         explanation=(
             'Nhập tịch thông thường (일반귀화) yêu cầu cư trú liên tục tại Hàn Quốc ít nhất 5 NĂM, không phải 3 năm '
             '— điều kiện 3 năm là của nhập tịch giản lược (간이귀화) — nên A là câu SAI, đây là đáp án đúng.\n'
             'B, C, D đều là điều kiện thật của nhập tịch thông thường: có tư cách thường trú F-5, có địa chỉ tại '
             'Hàn Quốc và đủ 19 tuổi, phẩm hạnh tốt và có khả năng tự nuôi sống bản thân.'
         )),
    dict(num=19, correct='A', options_source='reconstructed',
         stem=(
             '한국에서는 외국인들이 한국 생활에 잘 적응하고 행복하게 생활할 수 있도록 2007년에 이 법을 제정하였다. '
             '한국에 살고 있는 외국인들이 한국에서 불합리한 차별을 받지 않고 인권을 보장받도록 돕기 위해 제정한 이 '
             '법의 이름은?'
         ),
         options=[('A', '재한외국인 처우 기본법'), ('B', '다문화가족지원법'), ('C', '출입국관리법'), ('D', '국적법')],
         explanation=(
             'Đạo luật "재한외국인 처우 기본법" (Luật cơ bản về đãi ngộ người nước ngoài tại Hàn Quốc) được ban hành '
             'năm 2007 nhằm hỗ trợ người nước ngoài hội nhập vào xã hội Hàn Quốc, bảo đảm họ không bị phân biệt đối '
             'xử và được bảo vệ nhân quyền cơ bản — khớp với A.\n'
             'B chuyên hỗ trợ gia đình đa văn hóa (không bao quát mọi người nước ngoài). C quy định thủ tục xuất '
             'nhập cảnh. D quy định điều kiện quốc tịch — cả 3 đều là luật liên quan nhưng không phải luật được mô '
             'tả trong câu hỏi.\n'
             'Lưu ý: tài liệu nguồn chỉ cho đáp án đúng dạng điền từ, không có sẵn 4 phương án trắc nghiệm — B, C, '
             'D là do Claude tự dựng lại bằng các luật liên quan thật để tăng tính thử thách.'
         )),
    dict(num=20, correct='A', options_source='reconstructed',
         stem=(
             '2018년 12월 20일부터 국적법 개정에 따라 귀화나 국적 회복 허가를 받은 사람이 한국 국적을 가지기 위해서 '
             '국적증서 수여식에 참석하여 해야 하는 것은?'
         ),
         options=[('A', '국민선서'), ('B', '시민권 신청'), ('C', '외국인등록'), ('D', '주민등록')],
         explanation=(
             'Từ ngày 20/12/2018, theo Luật Quốc tịch sửa đổi, người được cấp phép nhập tịch hoặc khôi phục quốc '
             'tịch phải tham dự Lễ trao Giấy chứng nhận quốc tịch (국적증서 수여식) và thực hiện Tuyên thệ quốc dân '
             '(국민선서) — cam kết tuân thủ Hiến pháp và pháp luật Hàn Quốc — để chính thức trở thành công dân Hàn '
             'Quốc — khớp với A.\n'
             'B không phải thủ tục của Hàn Quốc. C, D là các thủ tục đăng ký cư trú khác, không liên quan đến lễ '
             'nhập tịch.\n'
             'Lưu ý: tài liệu nguồn chỉ cho đáp án đúng dạng điền từ, không có sẵn 4 phương án trắc nghiệm — B, C, '
             'D là do Claude tự dựng lại để tăng tính thử thách.'
         )),
]
