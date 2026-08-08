# -*- coding: utf-8 -*-
# Question set built from "5단계_1-사회_종합평가_기출문제_—_Giải_thích_chi_tiết.docx".
# Same clean-table format as geo8/hist7/law6/econ5/pol4/edu2: each question
# stored as label/content/correct-or-not/reason, so almost everything is
# direct from the source (Vietnamese parenthetical translations stripped
# from Korean option text). This doc only has 11 questions total (no
# missing gaps, unlike edu2's câu 11).
# Câu 1, option ②: the source text is garbled/duplicated ("대한민국의 국가는
# 애국가 국가는 태극기이다.", likely an OCR/transcription artifact from the
# original screenshot). Rewritten as a clean, unambiguous false statement on
# the same topic (mixing up flag vs. anthem) instead of reproducing broken
# Korean — options_source marked 'reconstructed' for this question.
# Câu 1 also has a source-flagged ambiguity: option ④ is noted as "also
# true" even though ③ is the expected answer — kept the note, following
# the same pattern used for edu2 câu 12.
# Câu 6 is a matching-type question — source only gives the pairing, not 4
# multiple-choice combos, so Claude built the other 3 combos (same style as
# law6/edu2, no fabrication-disclaimer sentence).

QUESTIONS = [
    dict(num=1, correct='C', options_source='reconstructed',
         stem='대한민국에 대한 설명으로 옳은 것은?',
         options=[
             ('A', '대한민국을 상징하는 꽃은 벚꽃이다.'),
             ('B', '태극기는 대한민국의 국가(國歌)이다.'),
             ('C', '국기에 대한 경례를 할 때는 오른손을 왼쪽 가슴에 댄다.'),
             ('D', "대한민국을 줄여서 한국이라고 하며, 영어로는 'Korea'라고 한다."),
         ],
         explanation=(
             '국기에 대한 경례를 할 때는 오른손을 펴서 왼쪽 가슴에 대는 것이 예의이다 — 정답은 C.\n'
             'A 대한민국을 상징하는 꽃은 벚꽃이 아니라 무궁화이다. B 태극기는 국기(國旗)이며, 국가(國歌·나라를 '
             '상징하는 노래)는 애국가이다 — 둘을 혼동한 설명이다.\n'
             '참고: D "한국"과 "Korea"라는 설명도 사실이지만, 원 자료에서 기대하는 답은 C이다.'
         )),
    dict(num=2, correct='D', options_source='docx',
         stem='애국가와 태극기의 설명으로 옳은 것은?',
         options=[
             ('A', '애국가 1절에는 남산과 무궁화가 나온다.'),
             ('B', '태극기의 4괘는 밝음, 순수, 평화, 조화를 의미한다.'),
             ('C', '국경일이나 국가기념일에만 태극기를 집 안이나 창문에 단다.'),
             ('D', "애국가는 4절로 구성되어 있으며, '나라를 사랑하는 노래'라는 뜻이다."),
         ],
         explanation=(
             '애국가는 총 4절로 이루어져 있으며, 그 이름은 "나라를 사랑하는 노래"라는 뜻이다 — 정답은 D.\n'
             'A 남산과 무궁화는 애국가 1절이 아니라 후렴이나 다른 절에 나오는 내용이다. B 태극기의 4괘(건곤감리)는 '
             '하늘·땅·물·불을 의미하며, "밝음, 순수, 평화, 조화"는 태극기의 흰색 바탕이 상징하는 의미이다. C '
             '태극기는 국경일뿐 아니라 평상시에도 집 안이나 관공서 등에 게양할 수 있다.'
         )),
    dict(num=3, correct='D', options_source='docx',
         stem='한국의 가족에 대한 설명으로 옳은 것은?',
         options=[
             ('A', '부모와 미혼 자녀가 같이 사는 것을 확대가족이라고 한다.'),
             ('B', '산업화가 이루어지면서 부모와 함께 사는 가족이 늘고 있다.'),
             ('C', '1인 가구가 늘고 있으며 최근 결혼 연령이 점점 낮아지고 있다.'),
             ('D', '과거에는 결혼한 후에도 부모님을 모시고 함께 사는 경우가 많았다.'),
         ],
         explanation=(
             '정답은 D — 과거 한국에서는 결혼 후에도 부모를 모시고 함께 사는 확대가족 형태가 흔했다.\n'
             'A 부모와 미혼 자녀만 사는 가족은 확대가족이 아니라 핵가족이다. B 산업화 이후에는 오히려 부모와 '
             '따로 사는 핵가족이 늘어났다. C 1인 가구가 느는 것은 맞지만, 결혼 연령은 낮아지는 것이 아니라 '
             '점점 높아지고 있다.'
         )),
    dict(num=4, correct='D', options_source='docx',
         stem='한국의 일터에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '한국에서는 만 15세 이상부터 일을 하는 것이 가능하다.'),
             ('B', '현재 한국 사람들이 가장 많이 원하는 일자리는 공무원이다.'),
             ('C', '여성들은 출산, 양육 문제로 재취업이 쉽지 않은 경우가 많다.'),
             ('D', '개인적으로 회사나 가게를 만들어 사업을 하는 사람이 거의 없다.'),
         ],
         explanation=(
             '실제로는 자영업자 비율이 전체 노동 인구의 약 20~25%로, 다른 OECD 국가들에 비해 매우 높은 편이다 — '
             '옳지 않은 것은 D.\n'
             'A 근로 가능 최소 연령이 만 15세라는 것, B 공무원이 가장 선호되는 직업이라는 것, C 여성의 경력 단절 '
             '문제는 모두 옳은 설명이다.'
         )),
    dict(num=5, correct='C', options_source='docx',
         stem='한글에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '1443년 세종대왕이 만들었다.'),
             ('B', '한글을 만든 후 문맹이 많이 줄어들었다.'),
             ('C', '자음은 하늘, 땅, 사람을 결합하여 만들었다.'),
             ('D', '한글은 자음 14개와 모음 10개로 이루어져 있다.'),
         ],
         explanation=(
             '하늘·땅·사람(삼재)을 결합해 만든 것은 모음이며, 자음은 발음 기관(혀, 이, 목구멍 등)의 모양을 본떠 '
             '만들었다 — 옳지 않은 것은 C.\n'
             'A 세종대왕이 1443년에 창제한 것, B 문맹률이 크게 줄어든 것, D 기본 자음 14개와 모음 10개로 구성된 '
             '것은 모두 옳은 설명이다.'
         )),
    dict(num=6, correct='A', options_source='reconstructed',
         stem=(
             '<보기>\n(가) 부부가 모두 일하는 것  (나) 같은 직장 사람들의 저녁 식사 모임\n'
             '(다) 퇴근 시간 후에 밤늦게까지 일하는 것  (라) 월요일부터 금요일까지 5일만 일하는 것\n'
             'ㄱ. 맞벌이  ㄴ. 회식  ㄷ. 시간 외 근무  ㄹ. 주 5일제\n'
             '<보기>의 의미와 명칭을 알맞게 연결한 것은?'
         ),
         options=[
             ('A', '(가)-ㄱ, (나)-ㄴ, (다)-ㄷ, (라)-ㄹ'),
             ('B', '(가)-ㄴ, (나)-ㄱ, (다)-ㄹ, (라)-ㄷ'),
             ('C', '(가)-ㄷ, (나)-ㄹ, (다)-ㄱ, (라)-ㄴ'),
             ('D', '(가)-ㄹ, (나)-ㄷ, (다)-ㄴ, (라)-ㄱ'),
         ],
         explanation=(
             '부부가 모두 일하는 것(가)은 맞벌이이다(ㄱ). 같은 직장 사람들의 저녁 식사 모임(나)은 회식이다(ㄴ). '
             '퇴근 후 밤늦게까지 일하는 것(다)은 시간 외 근무이다(ㄷ). 월요일부터 금요일까지 5일만 일하는 것'
             '(라)은 주 5일제이다(ㄹ) — 정답은 A.\n'
             'B, C, D는 모두 최소 한 쌍 이상 잘못 연결되어 있다.'
         )),
    dict(num=7, correct='D', options_source='docx',
         stem='대중교통 이용을 장려하는 제도에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '환승 할인 제도'),
             ('B', '버스 전용차로제'),
             ('C', '버스 도착 알림 서비스'),
             ('D', '자전거 무인 대여 시스템'),
         ],
         explanation=(
             '무인 자전거 대여 시스템(예: 서울의 따릉이)은 개인용 이동 수단이며, 버스·지하철 같은 대중교통을 '
             '장려하는 제도가 아니다 — 옳지 않은 것은 D.\n'
             'A 환승 할인, B 버스 전용차로제, C 버스 도착 알림 서비스는 모두 대중교통 이용을 장려하는 실제 '
             '제도이다.'
         )),
    dict(num=8, correct='D', options_source='docx',
         stem='오늘날의 인구 분포에 대한 설명으로 옳은 것은?',
         options=[
             ('A', '농촌 지역에 인구가 많다.'),
             ('B', '도시 지역에 인구가 적다.'),
             ('C', '지역에 따른 인구 차이가 없어졌다.'),
             ('D', '서울을 중심으로 수도권에 집중되어 있다.'),
         ],
         explanation=(
             '정답은 D — 한국의 인구는 서울을 중심으로 한 수도권에 크게 집중되어 있다.\n'
             'A, B는 실제와 반대이며(도시에 인구가 많고 농촌은 적다), C 지역별 인구 차이는 오히려 더 뚜렷해지고 '
             '있다.'
         )),
    dict(num=9, correct='C', options_source='docx',
         stem='다음 중 도시 문제에 해당하지 않는 것은?',
         options=[
             ('A', '환경 오염이 심해진다.'),
             ('B', '교통 체증이 심해진다.'),
             ('C', '도시에 노동력이 부족해진다.'),
             ('D', '사람들이 살 집이 부족해진다.'),
         ],
         explanation=(
             '노동력 부족은 오히려 농촌의 문제이다. 젊은 인구가 도시로 이동하면서 농촌에 일할 사람이 부족해지는 '
             '반면, 도시는 오히려 인구 과밀·실업 문제가 나타난다 — 정답은 C.\n'
             'A 환경 오염, B 교통 체증, D 주택 부족은 모두 대표적인 도시 문제이다.'
         )),
    dict(num=10, correct='B', options_source='docx',
         stem='도시화 현상이 나타난 이유로 가장 적절한 것은?',
         options=[
             ('A', '주말농장'),
             ('B', '빠른 산업화'),
             ('C', '높은 교육열'),
             ('D', '신도시 개발'),
         ],
         explanation=(
             '빠른 산업화로 도시에 일자리가 많이 생기면서 농촌 인구가 도시로 이동한 것이 한국 도시화의 가장 큰 '
             '원인이다 — 정답은 B.\n'
             'A 주말농장은 오히려 도시민이 농촌을 찾는 최근 현상이다. C 교육열은 한국 사회의 특징이지만 '
             '도시화의 직접적인 원인은 아니다. D 신도시 개발은 도시화의 원인이 아니라 결과이다.'
         )),
    dict(num=11, correct='B', options_source='docx',
         stem='한국의 농촌에 대한 설명으로 옳지 않은 것은?',
         options=[
             ('A', '농촌 지역 특산물을 이용하여 지역 축제를 연다.'),
             ('B', '혼잡 통행료 등의 새로운 제도를 시행하고 있다.'),
             ('C', '1960년대에는 도시 인구보다 농촌 인구가 더 많았다.'),
             ('D', '고령화 현상은 농촌이 해결해야 할 대표적인 문제이다.'),
         ],
         explanation=(
             '혼잡 통행료는 교통 체증을 줄이기 위한 도시의 제도이며, 농촌과는 관련이 없다 — 옳지 않은 것은 B.\n'
             'A 특산물을 활용한 지역 축제, C 1960년대 농촌 인구가 더 많았다는 것, D 고령화가 농촌의 대표적인 '
             '문제라는 것은 모두 옳은 설명이다.'
         )),
]
