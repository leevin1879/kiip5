# -*- coding: utf-8 -*-
# Question set built from "5단계_7-역사_종합평가_기출문제_—_Giải_thích_chi_tiết.docx".
# Same clean-table format as geo8: each question stored as label/content/
# correct-or-not/reason, so almost everything is direct from the source.
# Only Q6 (matching question — source only gives the reference mapping, not
# 4 multiple-choice combos) and Q19-20 (fill-in-the-blank, no options at all)
# needed Claude to build the other options.

QUESTIONS = [
    dict(num=1, correct='D', options_source='docx',
         stem='한국 역사에서 처음으로 등장한 나라는?',
         options=[('A', '고려'), ('B', '신라'), ('C', '조선'), ('D', '고조선')],
         explanation=(
             'Gojoseon (고조선, Cổ Triều Tiên) là nhà nước đầu tiên trong lịch sử Hàn Quốc, do Dangun Wanggeom lập ra — '
             'khớp với D.\n'
             'A Goryeo thành lập năm 918, B Silla là một trong Tam Quốc (xuất hiện sau Gojoseon), C Joseon thành lập '
             'năm 1392 — cả 3 đều muộn hơn Gojoseon rất nhiều.'
         )),
    dict(num=2, correct='C', options_source='docx',
         stem='삼국 중에 가장 늦게 발전하였으나 꾸준히 성장해서 삼국을 통일한 국가는?',
         options=[('A', '고려'), ('B', '백제'), ('C', '신라'), ('D', '고구려')],
         explanation=(
             'Silla phát triển muộn nhất trong Tam Quốc nhưng liên minh với nhà Đường (Trung Quốc) để thống nhất Tam '
             'Quốc vào năm 676 — khớp với C.\n'
             'A Goryeo không thuộc Tam Quốc (xuất hiện sau khi Silla suy yếu). B Baekje phát triển sớm nhưng bị diệt '
             'trước. D Goguryeo hùng mạnh nhất nhưng bị diệt trước Baekje.'
         )),
    dict(num=3, correct='B', options_source='docx',
         stem="'나라의 교육과 역사가 없어지지 아니하면 그 나라는 망하지 않는다'라고 말한 사람은?",
         options=[('A', '김대중'), ('B', '박은식'), ('C', '유관순'), ('D', '허난설헌')],
         explanation=(
             'Nhà sử học và nhà hoạt động độc lập Park Eun-sik đã nói câu này, nhấn mạnh tầm quan trọng của giáo dục '
             'và lịch sử trong việc bảo tồn dân tộc dưới thời Nhật thuộc — khớp với B.\n'
             'A Kim Dae-jung là Tổng thống Hàn Quốc (thời hiện đại, không liên quan). C Yu Gwan-sun là nữ anh hùng '
             'phong trào 1/3. D Heo Nanseolheon là nữ thi sĩ thời Joseon — cả 2 đều không phải người nói câu này.'
         )),
    dict(num=4, correct='D', options_source='docx',
         stem='나라 이름과 건국한 사람의 이름을 연결한 것으로 옳지 않은 것은?',
         options=[
             ('A', '고려 - 왕건'),
             ('B', '고조선 - 단군'),
             ('C', '조선 - 이성계'),
             ('D', '고구려 - 대조영'),
         ],
         explanation=(
             'Goguryeo được lập bởi Jumong (주몽), không phải Dae Joyeong — Dae Joyeong là người lập ra Balhae (발해) — '
             'nên D là câu SAI, đây là đáp án đúng.\n'
             'A, B, C đều là ghép đôi đúng: Wang Geon lập Goryeo (918), Dangun Wanggeom lập Gojoseon, Yi Seonggye lập '
             'Joseon (1392).'
         )),
    dict(num=5, correct='D', options_source='docx',
         stem='세계 최초의 금속활자로 찍은 책의 이름은?',
         options=[('A', '경국대전'), ('B', '삼강행실도'), ('C', '팔만대장경'), ('D', '직지심체요절')],
         explanation=(
             'Jikji (직지심체요절) in năm 1377 thời Goryeo là cuốn sách được in bằng chữ kim loại (금속활자) sớm nhất thế '
             'giới còn tồn tại đến nay, được UNESCO công nhận — khớp với D.\n'
             'A Gyeongguk Daejeon là bộ luật triều Joseon. B Samgang Haengsildo là sách đạo đức thời Joseon. C Tripitaka '
             'Koreana (Bát Vạn Đại Tạng Kinh) được khắc trên gỗ (목판), không phải chữ kim loại.'
         )),
    dict(num=6, correct='A', options_source='reconstructed',
         stem='한국의 지폐와 관련된 인물의 이름과 특징을 알맞게 연결하시오.',
         options=[
             ('A', '1.000원-이황, 5.000원-이이, 10.000원-세종대왕, 50.000원-신사임당'),
             ('B', '1.000원-이이, 5.000원-이황, 10.000원-세종대왕, 50.000원-신사임당'),
             ('C', '1.000원-이황, 5.000원-이이, 10.000원-신사임당, 50.000원-세종대왕'),
             ('D', '1.000원-세종대왕, 5.000원-이이, 10.000원-이황, 50.000원-신사임당'),
         ],
         explanation=(
             'Ghép đôi đúng: tờ 1.000 won in hình Yi Hwang (퇴계 이황), tờ 5.000 won in hình Yi I (율곡 이이), tờ 10.000 '
             'won in hình vua Sejong, tờ 50.000 won in hình Shin Saimdang (mẹ của Yi I) — khớp với A.\n'
             'B đảo ngược cặp 1.000/5.000. C đảo ngược cặp 10.000/50.000. D đảo ngược cặp 1.000/10.000 — đều là các '
             'hoán vị sai của cùng 4 mệnh giá.\n'
             'Lưu ý: tài liệu nguồn chỉ cho bảng ghép đôi đúng (không có sẵn 4 phương án trắc nghiệm dạng câu hỏi thi) '
             '— B, C, D là do Claude tự dựng lại bằng cách hoán đổi các cặp trong bảng gốc.'
         )),
    dict(num=7, correct='A', options_source='docx',
         stem='조선 시대 제주도에 심한 흉년이 들어 사람들이 굶어 죽게 되었을 때 자신의 돈으로 쌀을 사서 사람들에게 나누어 주어 백성을 구한 사람은?',
         options=[('A', '김만덕'), ('B', '유관순'), ('C', '신사임당'), ('D', '허난설헌')],
         explanation=(
             'Kim Man-deok là nữ thương gia thời Joseon ở Jeju. Khi đảo Jeju bị nạn đói, bà đã dùng toàn bộ tài sản '
             'tích lũy được để mua gạo từ đất liền về phát cho dân cứu đói — khớp với A.\n'
             'B Yu Gwan-sun là nữ anh hùng phong trào 1/3 năm 1919. C Shin Saimdang là nghệ sĩ và người mẹ mẫu mực, '
             'không liên quan cứu đói. D Heo Nanseolheon là nữ thi sĩ thời Joseon — cả 3 đều không liên quan.'
         )),
    dict(num=8, correct='B', options_source='docx',
         stem='불교의 문화유산이 아닌 것은?',
         options=[
             ('A', '불국사'),
             ('B', '삼강행실도'),
             ('C', '팔만대장경'),
             ('D', '정림사지 5층 석탑'),
         ],
         explanation=(
             'Samgang Haengsildo (삼강행실도, Tam Cương Hành Thực Đồ) là sách giáo dục đạo đức NHO GIÁO thời Joseon, '
             'không phải di sản Phật giáo — nên B là đáp án đúng cho câu hỏi "không phải".\n'
             'A Bulguksa là ngôi chùa Phật giáo nổi tiếng ở Gyeongju. C Tripitaka Koreana là bộ kinh Phật giáo khắc '
             'trên 81.258 tấm gỗ. D Tháp đá 5 tầng ở Jeongnimsaji là di tích Phật giáo thời Baekje — cả 3 đều là di '
             'sản Phật giáo thật sự.'
         )),
    dict(num=9, correct='A', options_source='docx',
         stem='외교를 통해 선란과위 전쟁을 막아낸 고려의 장군은?',
         options=[('A', '서희 (Seo Hui)'), ('B', '김만덕'), ('C', '이순신'), ('D', '을지문덕')],
         explanation=(
             'Tướng Seo Hui của Goryeo đã dùng ngoại giao (외교 담판) để đàm phán với tướng Khiết Đan (거란), không chỉ '
             'ngăn chiến tranh mà còn giành lại vùng đất Gangdong 6 châu (강동 6주) — khớp với A.\n'
             'B Kim Man-deok là nữ thương gia, không phải tướng quân. C Yi Sun-sin là đô đốc thời Joseon (chiến tranh '
             'Nhật Bản). D Eulji Mundeok là tướng Goguryeo, đánh bại quân Tùy tại Salsu — cả 2 đều liên quan chiến '
             'tranh khác, không phải Khiết Đan bằng ngoại giao.'
         )),
    dict(num=10, correct='D', options_source='docx',
         stem='허난설헌에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '홍길동전을 지은 허균의 누나이다.'),
             ('B', '어렸을 때부터 글재주가 훌륭해서 시를 잘 지었다.'),
             ('C', '허난설헌의 시는 중국과 일본에서 높은 평가를 받았다.'),
             ('D', '허난설헌은 그림에 재능이 있었고 아들을 훌륭하게 키웠다.'),
         ],
         explanation=(
             'Heo Nanseolheon nổi tiếng về THƠ CA, không phải hội họa. Ngoài ra bà không có con trai sống sót (mất '
             'sớm ở tuổi 27) — người nổi tiếng vì nuôi dạy con trai xuất sắc (Yi I) là Shin Saimdang, không phải Heo '
             'Nanseolheon — nên D là câu SAI, đây là đáp án đúng.\n'
             'A, B, C đều là mô tả đúng: bà là chị gái của Heo Gyun (tác giả Hong Gil-dong jeon), có tài thơ văn từ '
             'nhỏ, và thơ của bà được đánh giá cao ở cả Trung Quốc và Nhật Bản.'
         )),
    dict(num=11, correct='A', options_source='docx',
         stem='3·1운동 이후 중국 상하이에 대한민국 임시정부를 세우고 독립운동을 이끌었던 인물은?',
         options=[('A', '김구 (Kim Gu)'), ('B', '유관순'), ('C', '안중근'), ('D', '윤봉길')],
         explanation=(
             'Kim Gu là nhà lãnh đạo phong trào độc lập, Chủ tịch Chính phủ lâm thời Đại Hàn Dân Quốc tại Thượng Hải, '
             'là biểu tượng của phong trào kháng Nhật — khớp với A.\n'
             'B Yu Gwan-sun lãnh đạo biểu tình 1/3 ở Cheonan, không phải người lập Chính phủ lâm thời. C Ahn Jung-geun '
             'ám sát Ito Hirobumi năm 1909 (trước khi có Chính phủ lâm thời). D Yun Bong-gil ném bom vào quan chức '
             'Nhật tại Thượng Hải năm 1932, là THÀNH VIÊN của phong trào do Kim Gu lãnh đạo, không phải người lập ra nó.'
         )),
    dict(num=12, correct='B', options_source='docx',
         stem='백제에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '삼국 중 가장 먼저 발전하였다.'),
             ('B', '중국에 한자와 유교를 전하였다.'),
             ('C', '중국과 일본까지 활발하게 무역을 하였다.'),
             ('D', '대표적인 유적으로 부여 정림사지 5층 석탑이 있다.'),
         ],
         explanation=(
             'Baekje truyền bá Phật giáo, chữ Hán và văn hóa sang NHẬT BẢN (일본), không phải truyền cho Trung Quốc — '
             'bản thân chữ Hán và Nho giáo vốn có nguồn gốc từ Trung Quốc nên Baekje không thể "truyền" ngược lại cho '
             'Trung Quốc — nên B là câu SAI, đây là đáp án đúng.\n'
             'A, C, D đều là mô tả đúng: Baekje phát triển sớm nhất trong Tam Quốc, có quan hệ thương mại sôi động với '
             'cả Trung Quốc và Nhật Bản, và có di tích tiêu biểu là tháp đá 5 tầng ở Jeongnimsaji (Buyeo).'
         )),
    dict(num=13, correct='B', options_source='docx',
         stem='신라에 대한 설명으로 옳은 것은?',
         options=[
             ('A', '5세기에 영토를 크게 넓혔다.'),
             ('B', '한국 최초로 통일 국가를 이루었다.'),
             ('C', '동양에서 가장 오래된 천문대인 혼천의를 만들었다.'),
             ('D', '유교를 국가 이념으로 삼고 유교 문화를 발전시켰다.'),
         ],
         explanation=(
             'Silla thống nhất Tam Quốc vào năm 676, trở thành nhà nước thống nhất đầu tiên trong lịch sử Hàn Quốc — '
             'khớp với B.\n'
             'A sai: Goguryeo mới là nước mở rộng lãnh thổ lớn nhất vào thế kỷ 5 (thời vua Gwanggaeto).\n'
             'C sai: đài thiên văn cổ nhất châu Á là Cheomseongdae (첨성대), không phải Honcheonui (혼천의 — dụng cụ đo '
             'thiên văn khác, thuộc thời Joseon).\n'
             'D sai: Silla sùng bái Phật giáo (불교), không phải Nho giáo — Nho giáo mới là quốc giáo của Joseon.'
         )),
    dict(num=14, correct='C', options_source='docx',
         stem='발해에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '대조영이 고구려 유민들과 함께 세웠다.'),
             ('B', "통일 신라와 함께 '남북국 시대'라고 한다."),
             ('C', '5세기에 가장 발전하여 영토를 크게 넓혔다.'),
             ('D', '고구려인들이 옛 고구려 땅인 만주에 세운 나라이다.'),
         ],
         explanation=(
             'Balhae phát triển cực thịnh vào THẾ KỶ 9 (thời vua Seon - 선왕), không phải thế kỷ 5 — thế kỷ 5 là thời '
             'kỳ của Goguryeo — nên C là câu SAI, đây là đáp án đúng.\n'
             'A, B, D đều là mô tả đúng: Dae Joyeong lập Balhae năm 698 cùng người Goguryeo di tản, thời kỳ Balhae + '
             'Silla thống nhất gọi là "Thời đại Nam Bắc Quốc", và Balhae được lập ở vùng Mãn Châu (đất cũ Goguryeo).'
         )),
    dict(num=15, correct='D', options_source='docx',
         stem='고려에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '벽란도로 아라비아 상인들도 들어와 무역하였다.'),
             ('B', '왕건은 발해 사람들까지 받아들여 고려를 건국했다.'),
             ('C', '고구려의 영토를 회복하겠다는 뜻으로 고려라고 지었다.'),
             ('D', '유교 이념으로 나라를 건국했으나 불교 행사도 많이 열었다.'),
         ],
         explanation=(
             'Goryeo lấy PHẬT GIÁO (불교) làm quốc giáo, không phải Nho giáo — Joseon mới lấy Nho giáo làm quốc giáo — '
             'Goryeo tổ chức nhiều lễ hội Phật giáo như Yeondeunghoe (연등회) và Palguanhoe (팔관회) — nên D là câu SAI, '
             'đây là đáp án đúng.\n'
             'A, B, C đều là mô tả đúng: cảng Byeokrando đón cả thương nhân Ả Rập, Wang Geon chào đón người Balhae di '
             'tản, và tên "Goryeo" lấy từ "Goguryeo" thể hiện ý chí khôi phục lãnh thổ.'
         )),
    dict(num=16, correct='D', options_source='docx',
         stem='조선 후기에 대한 설명으로 옳은 것은?',
         options=[
             ('A', '서양의 여러 나라와 적극적으로 교류하였다.'),
             ('B', '조선의 발달된 문물을 서양으로 수출하였다.'),
             ('C', '쇄국정책을 실시하여 나라가 더욱 발전하였다.'),
             ('D', '정약용이 거중기를 만들어 수원 화성을 완성했다.'),
         ],
         explanation=(
             'Jeong Yak-yong (Dasan) đã phát minh ra cần cẩu (거중기) giúp xây dựng thành Hwaseong ở Suwon dưới thời '
             'vua Jeongjo — khớp với D.\n'
             'A, B sai: Joseon hậu kỳ theo chính sách bế quan tỏa cảng (쇄국정책), không tích cực giao lưu hay xuất '
             'khẩu văn hóa sang phương Tây.\n'
             'C sai: chính sách bế quan tỏa cảng thực ra làm Joseon CHẬM phát triển và dễ bị xâm lược hơn, không phải '
             'giúp phát triển hơn.'
         )),
    dict(num=17, correct='D', options_source='docx',
         stem='세종대왕에 대한 설명으로 옳은 것은?',
         options=[
             ('A', '한글이라는 명칭은 세종대왕이 만들었다.'),
             ('B', '조선 시대의 법전인 경국대전을 완성하였다.'),
             ('C', '훈민정음이란 널리 인간을 이롭게 한다는 뜻이다.'),
             ('D', '조선의 네 번째 왕으로 과학 기술에 관심이 많았다.'),
         ],
         explanation=(
             'Vua Sejong là vị vua thứ 4 của Joseon và rất quan tâm đến khoa học kỹ thuật, đã cho chế tạo nhiều dụng '
             'cụ đo lường như 측우기 (đồng hồ mưa), 앙부일구 (đồng hồ mặt trời) — khớp với D.\n'
             'A sai: tên gọi "한글 (Hangeul)" được đặt bởi học giả Ju Si-gyeong (주시경) vào thế kỷ 20 — vua Sejong gọi '
             'chữ viết do ông sáng tạo là "훈민정음 (Hunminjeongeum)".\n'
             'B sai: Gyeongguk Daejeon được hoàn thành dưới thời vua Seongjong (성종), không phải Sejong.\n'
             'C sai: "널리 인간을 이롭게 한다" là ý nghĩa của Hongik Ingan (홍익인간) — lý tưởng lập quốc của Dangun, không '
             'phải nghĩa của Hunminjeongeum (nghĩa đúng là "âm thanh đúng đắn để dạy dân").'
         )),
    dict(num=18, correct='A', options_source='docx',
         stem='신사임당에 대한 설명으로 옳은 것은?',
         options=[
             ('A', '이이를 훌륭하게 키운 어머니이다.'),
             ('B', '한국 지폐에 있는 유일한 여성이다.'),
             ('C', '고려 시대를 대표하는 훌륭한 여성이다.'),
             ('D', '신사임당의 시가 중국과 일본에서 칭찬을 받았다.'),
         ],
         explanation=(
             '⚠️ Bản thân tài liệu nguồn cũng ghi chú thêm về câu này: Shin Saimdang là mẹ của học giả Nho giáo Yi I '
             '(율곡 이이), được tôn kính là người mẹ mẫu mực của Hàn Quốc — khớp với A.\n'
             'Lưu ý: B ("phụ nữ duy nhất trên tiền Hàn Quốc") THỰC RA cũng là một phát biểu đúng về nội dung (Shin '
             'Saimdang trên tờ 50.000 won đúng là gương mặt nữ duy nhất trên tiền giấy Hàn Quốc hiện hành) — tài liệu '
             'nguồn tự nhận xét rằng A "cụ thể và chính xác hơn" nên được chọn làm đáp án chính, nhưng về mặt logic thi '
             'trắc nghiệm thì đây có thể coi là một câu hỏi có 2 đáp án đúng.\n'
             'C sai: Shin Saimdang sống vào thời Joseon, không phải Goryeo.\n'
             'D sai: người nổi tiếng với thơ ca được đánh giá cao ở Trung Quốc và Nhật Bản là Heo Nanseolheon, không '
             'phải Shin Saimdang (bà nổi tiếng về hội họa và thư pháp).'
         )),
    dict(num=19, correct='D', options_source='reconstructed',
         stem='수나라가 큰 군대를 이끌고 쳐들어 왔을 때 평양 가까이 살수에서 크게 승리한 고구려의 장군은?',
         options=[('A', '서희'), ('B', '이순신'), ('C', '김유신'), ('D', '을지문덕')],
         explanation=(
             'Tướng Eulji Mundeok của Goguryeo đã đánh bại đại quân nhà Tùy (Trung Quốc) tại trận Salsu (살수대첩, năm '
             '612) — một trong những chiến thắng vĩ đại nhất trong lịch sử Hàn Quốc, tiêu diệt hơn 300.000 quân Tùy — '
             'khớp với D.\n'
             'A Seo Hui dùng ngoại giao chống Khiết Đan (thời Goryeo, không phải chiến trận với nhà Tùy). B Yi Sun-sin '
             'là đô đốc thời Joseon chống Nhật Bản. C Kim Yu-sin là tướng thời Silla, liên quan việc thống nhất Tam '
             'Quốc, không liên quan trận Salsu.\n'
             'Lưu ý: tài liệu nguồn chỉ cho biết đáp án đúng dạng điền từ, không có sẵn 4 phương án trắc nghiệm — A, '
             'B, C là do Claude tự dựng lại bằng các danh tướng lịch sử khác để tăng tính thử thách.'
         )),
    dict(num=20, correct='C', options_source='reconstructed',
         stem='임진왜란 때 거북선을 만들어 일본과의 전쟁을 승리로 이끌었던 인물은?',
         options=[('A', '김구'), ('B', '을지문덕'), ('C', '이순신 (Yi Sun-sin)'), ('D', '서희')],
         explanation=(
             'Đô đốc Yi Sun-sin là người phát minh ra thuyền rùa (거북선) và lãnh đạo hải quân Joseon đánh bại quân '
             'Nhật trong chiến tranh Imjin (임진왜란, 1592-1598) — ông là anh hùng dân tộc vĩ đại nhất của Hàn Quốc — '
             'khớp với C.\n'
             'A Kim Gu là nhà lãnh đạo phong trào độc lập đầu thế kỷ 20, không liên quan chiến tranh Imjin. B Eulji '
             'Mundeok đánh quân Tùy thời Goguryeo. D Seo Hui dùng ngoại giao chống Khiết Đan thời Goryeo — cả 3 đều là '
             'nhân vật lịch sử khác thời kỳ.\n'
             'Lưu ý: tài liệu nguồn chỉ cho biết đáp án đúng dạng điền từ, không có sẵn 4 phương án trắc nghiệm — A, '
             'B, D là do Claude tự dựng lại bằng các danh nhân lịch sử khác để tăng tính thử thách.'
         )),
]
