# -*- coding: utf-8 -*-
"""
세계 각지(아시아 일부·중동·아프리카·유럽·오세아니아·북미·중남미) 국제학교 디렉터리.
curricula 키는 ibdp / igcse / ap / alevel 네 가지만 사용하며, 확실한 경우에만 기재한다.
"""

SCHOOLS = [
    # ---------------- 인도 ----------------
    {"name": "아메리칸 엠버시 스쿨 (AES)", "name_en": "American Embassy School", "country": "인도", "city": "뉴델리", "curricula": ["ibdp"], "note": "미국식 커리큘럼"},
    {"name": "브리티시 스쿨 뉴델리", "name_en": "The British School, New Delhi", "country": "인도", "city": "뉴델리", "curricula": ["igcse", "ibdp"], "note": "영국식 커리큘럼"},
    {"name": "패스웨이즈 월드 스쿨 아라발리", "name_en": "Pathways World School, Aravali", "country": "인도", "city": "구르가온", "curricula": ["ibdp"], "note": "IB 연속과정 운영"},
    {"name": "GD 고엔카 월드 스쿨", "name_en": "GD Goenka World School", "country": "인도", "city": "구르가온", "curricula": ["ibdp", "igcse"], "note": ""},
    {"name": "랜서스 인터내셔널 스쿨", "name_en": "Lancers International School", "country": "인도", "city": "구르가온", "curricula": ["ibdp", "igcse"], "note": ""},
    {"name": "아메리칸 스쿨 오브 봄베이 (ASB)", "name_en": "American School of Bombay", "country": "인도", "city": "뭄바이", "curricula": ["ibdp"], "note": "미국식 커리큘럼"},
    {"name": "디루바이 암바니 인터내셔널 스쿨 (DAIS)", "name_en": "Dhirubhai Ambani International School", "country": "인도", "city": "뭄바이", "curricula": ["ibdp", "igcse"], "note": ""},
    {"name": "오베로이 인터내셔널 스쿨", "name_en": "Oberoi International School", "country": "인도", "city": "뭄바이", "curricula": ["ibdp"], "note": ""},
    {"name": "캐나디언 인터내셔널 스쿨 방갈로르 (CIS)", "name_en": "Canadian International School, Bangalore", "country": "인도", "city": "방갈로르", "curricula": ["ibdp", "igcse"], "note": ""},
    {"name": "스톤힐 인터내셔널 스쿨", "name_en": "Stonehill International School", "country": "인도", "city": "방갈로르", "curricula": ["ibdp"], "note": ""},
    {"name": "인더스 인터내셔널 스쿨 방갈로르", "name_en": "Indus International School, Bangalore", "country": "인도", "city": "방갈로르", "curricula": ["ibdp", "igcse"], "note": ""},
    {"name": "인터내셔널 스쿨 방갈로르 (TISB)", "name_en": "The International School Bangalore", "country": "인도", "city": "방갈로르", "curricula": ["ibdp", "igcse", "alevel"], "note": ""},
    {"name": "아메리칸 인터내셔널 스쿨 첸나이 (AISC)", "name_en": "American International School Chennai", "country": "인도", "city": "첸나이", "curricula": ["ibdp"], "note": "미국식 커리큘럼"},
    {"name": "인터내셔널 스쿨 오브 하이데라바드 (ISH)", "name_en": "International School of Hyderabad", "country": "인도", "city": "하이데라바드", "curricula": ["ibdp", "igcse"], "note": ""},
    {"name": "UWC 마힌드라 칼리지", "name_en": "UWC Mahindra College", "country": "인도", "city": "푸네", "curricula": ["ibdp"], "note": "UWC 보딩스쿨"},
    {"name": "메르세데스-벤츠 인터내셔널 스쿨 (MBIS)", "name_en": "Mercedes-Benz International School", "country": "인도", "city": "푸네", "curricula": ["ibdp"], "note": ""},
    {"name": "우드스톡 스쿨", "name_en": "Woodstock School", "country": "인도", "city": "무수리", "curricula": ["ibdp"], "note": "보딩스쿨"},

    # ---------------- 스리랑카 ----------------
    {"name": "오버시즈 스쿨 오브 콜롬보 (OSC)", "name_en": "The Overseas School of Colombo", "country": "스리랑카", "city": "콜롬보", "curricula": ["ibdp"], "note": ""},
    {"name": "브리티시 스쿨 인 콜롬보", "name_en": "The British School in Colombo", "country": "스리랑카", "city": "콜롬보", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "콜롬보 인터내셔널 스쿨 (CIS)", "name_en": "Colombo International School", "country": "스리랑카", "city": "콜롬보", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},

    # ---------------- 방글라데시 ----------------
    {"name": "아메리칸 인터내셔널 스쿨 다카 (AISD)", "name_en": "American International School Dhaka", "country": "방글라데시", "city": "다카", "curricula": ["ibdp"], "note": "미국식 커리큘럼"},
    {"name": "인터내셔널 스쿨 다카 (ISD)", "name_en": "International School Dhaka", "country": "방글라데시", "city": "다카", "curricula": ["ibdp"], "note": ""},

    # ---------------- 파키스탄 ----------------
    {"name": "인터내셔널 스쿨 오브 이슬라마바드 (ISOI)", "name_en": "International School of Islamabad", "country": "파키스탄", "city": "이슬라마바드", "curricula": [], "note": "미국식 커리큘럼"},
    {"name": "카라치 아메리칸 스쿨 (KAS)", "name_en": "Karachi American School", "country": "파키스탄", "city": "카라치", "curricula": [], "note": "미국식 커리큘럼"},
    {"name": "카라치 그래머 스쿨 (KGS)", "name_en": "Karachi Grammar School", "country": "파키스탄", "city": "카라치", "curricula": ["alevel"], "note": "영국식 커리큘럼"},

    # ---------------- 카자흐스탄 ----------------
    {"name": "알마티 인터내셔널 스쿨 (AIS)", "name_en": "Almaty International School", "country": "카자흐스탄", "city": "알마티", "curricula": [], "note": "QSI 계열 미국식 커리큘럼"},
    {"name": "헤일리베리 알마티", "name_en": "Haileybury Almaty", "country": "카자흐스탄", "city": "알마티", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "카자흐스탄 인터내셔널 스쿨 (KIS)", "name_en": "Kazakhstan International School", "country": "카자흐스탄", "city": "알마티", "curricula": ["ibdp"], "note": ""},
    {"name": "헤일리베리 아스타나", "name_en": "Haileybury Astana", "country": "카자흐스탄", "city": "아스타나", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},

    # ---------------- 우즈베키스탄 ----------------
    {"name": "타슈켄트 인터내셔널 스쿨 (TIS)", "name_en": "Tashkent International School", "country": "우즈베키스탄", "city": "타슈켄트", "curricula": ["ibdp"], "note": ""},
    {"name": "브리티시 스쿨 오브 타슈켄트", "name_en": "The British School of Tashkent", "country": "우즈베키스탄", "city": "타슈켄트", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},

    # ---------------- 아랍에미리트 ----------------
    {"name": "아메리칸 스쿨 오브 두바이 (ASD)", "name_en": "American School of Dubai", "country": "아랍에미리트", "city": "두바이", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "두바이 아메리칸 아카데미 (DAA)", "name_en": "GEMS Dubai American Academy", "country": "아랍에미리트", "city": "두바이", "curricula": ["ap", "ibdp"], "note": "미국식 커리큘럼"},
    {"name": "젬스 월드 아카데미 두바이 (GWA)", "name_en": "GEMS World Academy Dubai", "country": "아랍에미리트", "city": "두바이", "curricula": ["ibdp"], "note": ""},
    {"name": "젬스 웰링턴 인터내셔널 스쿨 (WIS)", "name_en": "GEMS Wellington International School", "country": "아랍에미리트", "city": "두바이", "curricula": ["igcse", "ibdp"], "note": "영국식 커리큘럼"},
    {"name": "두바이 칼리지", "name_en": "Dubai College", "country": "아랍에미리트", "city": "두바이", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "주메이라 칼리지", "name_en": "Jumeirah College", "country": "아랍에미리트", "city": "두바이", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "주메이라 잉글리시 스피킹 스쿨 (JESS)", "name_en": "Jumeirah English Speaking School", "country": "아랍에미리트", "city": "두바이", "curricula": ["igcse", "ibdp"], "note": "영국식 커리큘럼"},
    {"name": "두바이 잉글리시 스피킹 칼리지 (DESC)", "name_en": "Dubai English Speaking College", "country": "아랍에미리트", "city": "두바이", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "두바이 인터내셔널 아카데미 (DIA)", "name_en": "Dubai International Academy", "country": "아랍에미리트", "city": "두바이", "curricula": ["ibdp"], "note": ""},
    {"name": "렙튼 스쿨 두바이", "name_en": "Repton School Dubai", "country": "아랍에미리트", "city": "두바이", "curricula": ["igcse", "ibdp"], "note": "영국식 커리큘럼"},
    {"name": "브라이튼 칼리지 두바이", "name_en": "Brighton College Dubai", "country": "아랍에미리트", "city": "두바이", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "노스 런던 컬리지엇 스쿨 두바이 (NLCS 두바이)", "name_en": "North London Collegiate School Dubai", "country": "아랍에미리트", "city": "두바이", "curricula": ["ibdp"], "note": ""},
    {"name": "노드 앵글리아 인터내셔널 스쿨 두바이 (NAS 두바이)", "name_en": "Nord Anglia International School Dubai", "country": "아랍에미리트", "city": "두바이", "curricula": ["igcse", "ibdp"], "note": ""},
    {"name": "아메리칸 커뮤니티 스쿨 오브 아부다비 (ACS)", "name_en": "American Community School of Abu Dhabi", "country": "아랍에미리트", "city": "아부다비", "curricula": ["ibdp"], "note": "미국식 커리큘럼"},
    {"name": "브리티시 스쿨 알 쿠바이라트 (BSAK)", "name_en": "The British School Al Khubairat", "country": "아랍에미리트", "city": "아부다비", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "크랜리 아부다비", "name_en": "Cranleigh Abu Dhabi", "country": "아랍에미리트", "city": "아부다비", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "브라이튼 칼리지 아부다비", "name_en": "Brighton College Abu Dhabi", "country": "아랍에미리트", "city": "아부다비", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "라하 인터내셔널 스쿨", "name_en": "Raha International School", "country": "아랍에미리트", "city": "아부다비", "curricula": ["ibdp"], "note": ""},

    # ---------------- 카타르 ----------------
    {"name": "아메리칸 스쿨 오브 도하 (ASD)", "name_en": "American School of Doha", "country": "카타르", "city": "도하", "curricula": ["ibdp", "ap"], "note": "미국식 커리큘럼"},
    {"name": "도하 칼리지", "name_en": "Doha College", "country": "카타르", "city": "도하", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "카타르 아카데미 도하", "name_en": "Qatar Academy Doha", "country": "카타르", "city": "도하", "curricula": ["ibdp"], "note": ""},
    {"name": "도하 브리티시 스쿨 (DBS)", "name_en": "Doha British School", "country": "카타르", "city": "도하", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "인터내셔널 스쿨 오브 런던 카타르 (ISL 카타르)", "name_en": "International School of London Qatar", "country": "카타르", "city": "도하", "curricula": ["ibdp"], "note": ""},
    {"name": "ACS 도하 인터내셔널 스쿨", "name_en": "ACS Doha International School", "country": "카타르", "city": "도하", "curricula": ["ibdp"], "note": ""},
    {"name": "셔본 카타르", "name_en": "Sherborne Qatar", "country": "카타르", "city": "도하", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},

    # ---------------- 사우디아라비아 ----------------
    {"name": "아메리칸 인터내셔널 스쿨 리야드 (AIS-R)", "name_en": "American International School - Riyadh", "country": "사우디아라비아", "city": "리야드", "curricula": ["ibdp", "ap"], "note": "미국식 커리큘럼"},
    {"name": "브리티시 인터내셔널 스쿨 리야드 (BISR)", "name_en": "British International School Riyadh", "country": "사우디아라비아", "city": "리야드", "curricula": ["igcse"], "note": "영국식 커리큘럼"},
    {"name": "아메리칸 인터내셔널 스쿨 오브 제다 (AISJ)", "name_en": "American International School of Jeddah", "country": "사우디아라비아", "city": "제다", "curricula": [], "note": "미국식 커리큘럼"},
    {"name": "브리티시 인터내셔널 스쿨 오브 제다 (BISJ)", "name_en": "British International School of Jeddah", "country": "사우디아라비아", "city": "제다", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "ISG 아메리칸 스쿨 오브 다란", "name_en": "ISG American School of Dhahran", "country": "사우디아라비아", "city": "다란", "curricula": [], "note": "미국식 커리큘럼"},
    {"name": "ISG 브리티시 스쿨 오브 다란", "name_en": "ISG British School of Dhahran", "country": "사우디아라비아", "city": "다란", "curricula": ["igcse"], "note": "영국식 커리큘럼"},
    {"name": "KAUST 스쿨", "name_en": "The KAUST School", "country": "사우디아라비아", "city": "투왈", "curricula": ["ibdp"], "note": "KAUST 캠퍼스 내 학교"},

    # ---------------- 쿠웨이트 ----------------
    {"name": "아메리칸 스쿨 오브 쿠웨이트 (ASK)", "name_en": "American School of Kuwait", "country": "쿠웨이트", "city": "쿠웨이트시티", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "아메리칸 인터내셔널 스쿨 쿠웨이트 (AIS)", "name_en": "American International School Kuwait", "country": "쿠웨이트", "city": "쿠웨이트시티", "curricula": ["ibdp"], "note": "미국식 커리큘럼"},
    {"name": "브리티시 스쿨 오브 쿠웨이트 (BSK)", "name_en": "The British School of Kuwait", "country": "쿠웨이트", "city": "쿠웨이트시티", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},

    # ---------------- 바레인 ----------------
    {"name": "바레인 스쿨", "name_en": "Bahrain School", "country": "바레인", "city": "마나마", "curricula": ["ibdp"], "note": "미 국방부(DoDEA) 운영 학교"},
    {"name": "세인트 크리스토퍼스 스쿨 바레인", "name_en": "St Christopher's School, Bahrain", "country": "바레인", "city": "마나마", "curricula": ["igcse", "alevel", "ibdp"], "note": "영국식 커리큘럼"},
    {"name": "브리티시 스쿨 오브 바레인 (BSB)", "name_en": "The British School of Bahrain", "country": "바레인", "city": "마나마", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},

    # ---------------- 오만 ----------------
    {"name": "아메리칸 브리티시 아카데미 (ABA)", "name_en": "The American British Academy", "country": "오만", "city": "무스카트", "curricula": ["ibdp"], "note": ""},
    {"name": "브리티시 스쿨 무스카트 (BSM)", "name_en": "British School Muscat", "country": "오만", "city": "무스카트", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},

    # ---------------- 튀르키예 ----------------
    {"name": "이스탄불 인터내셔널 커뮤니티 스쿨 (IICS)", "name_en": "Istanbul International Community School", "country": "튀르키예", "city": "이스탄불", "curricula": ["ibdp"], "note": ""},
    {"name": "브리티시 인터내셔널 스쿨 이스탄불 (BISI)", "name_en": "The British International School Istanbul", "country": "튀르키예", "city": "이스탄불", "curricula": ["igcse", "ibdp"], "note": "영국식 커리큘럼"},
    {"name": "MEF 인터내셔널 스쿨 이스탄불", "name_en": "MEF International School Istanbul", "country": "튀르키예", "city": "이스탄불", "curricula": ["ibdp", "igcse"], "note": ""},
    {"name": "코치 스쿨", "name_en": "Koç School", "country": "튀르키예", "city": "이스탄불", "curricula": ["ibdp"], "note": ""},

    # ---------------- 이집트 ----------------
    {"name": "카이로 아메리칸 칼리지 (CAC)", "name_en": "Cairo American College", "country": "이집트", "city": "카이로", "curricula": ["ibdp", "ap"], "note": "미국식 커리큘럼"},
    {"name": "브리티시 인터내셔널 스쿨 카이로 (BISC)", "name_en": "British International School, Cairo", "country": "이집트", "city": "카이로", "curricula": ["igcse", "ibdp"], "note": "영국식 커리큘럼"},
    {"name": "뉴 카이로 브리티시 인터내셔널 스쿨 (NCBIS)", "name_en": "New Cairo British International School", "country": "이집트", "city": "카이로", "curricula": ["igcse", "ibdp"], "note": "영국식 커리큘럼"},
    {"name": "말번 칼리지 이집트", "name_en": "Malvern College Egypt", "country": "이집트", "city": "카이로", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},

    # ---------------- 케냐 ----------------
    {"name": "인터내셔널 스쿨 오브 케냐 (ISK)", "name_en": "International School of Kenya", "country": "케냐", "city": "나이로비", "curricula": ["ibdp"], "note": ""},
    {"name": "브레이번 스쿨 나이로비", "name_en": "Braeburn School", "country": "케냐", "city": "나이로비", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "브룩하우스 스쿨", "name_en": "Brookhouse School", "country": "케냐", "city": "나이로비", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "페포니 스쿨", "name_en": "Peponi School", "country": "케냐", "city": "나이로비", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},

    # ---------------- 남아프리카공화국 ----------------
    {"name": "아메리칸 인터내셔널 스쿨 오브 요하네스버그 (AISJ)", "name_en": "American International School of Johannesburg", "country": "남아프리카공화국", "city": "요하네스버그", "curricula": ["ibdp"], "note": "미국식 커리큘럼"},

    # ---------------- 나이지리아 ----------------
    {"name": "아메리칸 인터내셔널 스쿨 오브 라고스 (AISL)", "name_en": "American International School of Lagos", "country": "나이지리아", "city": "라고스", "curricula": [], "note": "미국식 커리큘럼"},
    {"name": "브리티시 인터내셔널 스쿨 라고스 (BIS)", "name_en": "British International School Lagos", "country": "나이지리아", "city": "라고스", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "레키 브리티시 인터내셔널 스쿨", "name_en": "Lekki British International School", "country": "나이지리아", "city": "라고스", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},

    # ---------------- 영국 ----------------
    {"name": "아메리칸 스쿨 인 런던 (ASL)", "name_en": "The American School in London", "country": "영국", "city": "런던", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "ACS 코브햄 인터내셔널 스쿨", "name_en": "ACS Cobham International School", "country": "영국", "city": "코브햄(서리)", "curricula": ["ibdp", "ap"], "note": "기숙 가능"},
    {"name": "ACS 에그햄 인터내셔널 스쿨", "name_en": "ACS Egham International School", "country": "영국", "city": "에그햄(서리)", "curricula": ["ibdp"], "note": "IB 연속과정 운영"},
    {"name": "ACS 힐링던 인터내셔널 스쿨", "name_en": "ACS Hillingdon International School", "country": "영국", "city": "런던", "curricula": ["ibdp", "ap"], "note": ""},
    {"name": "TASIS 잉글랜드", "name_en": "TASIS The American School in England", "country": "영국", "city": "소프(서리)", "curricula": ["ibdp", "ap"], "note": "미국식 커리큘럼, 보딩스쿨"},
    {"name": "사우스뱅크 인터내셔널 스쿨", "name_en": "Southbank International School", "country": "영국", "city": "런던", "curricula": ["ibdp"], "note": "IB 연속과정 운영"},
    {"name": "ICS 런던", "name_en": "International Community School London", "country": "영국", "city": "런던", "curricula": ["ibdp"], "note": ""},
    {"name": "드와이트 스쿨 런던", "name_en": "Dwight School London", "country": "영국", "city": "런던", "curricula": ["ibdp"], "note": "IB 연속과정 운영"},
    {"name": "인터내셔널 스쿨 오브 런던 (ISL)", "name_en": "International School of London", "country": "영국", "city": "런던", "curricula": ["ibdp"], "note": ""},
    {"name": "할시온 런던 인터내셔널 스쿨", "name_en": "Halcyon London International School", "country": "영국", "city": "런던", "curricula": ["ibdp"], "note": ""},
    {"name": "메리마운트 인터내셔널 스쿨 런던", "name_en": "Marymount International School London", "country": "영국", "city": "런던", "curricula": ["ibdp"], "note": "여학교, 기숙 가능"},

    # ---------------- 독일 ----------------
    {"name": "프랑크푸르트 인터내셔널 스쿨 (FIS)", "name_en": "Frankfurt International School", "country": "독일", "city": "프랑크푸르트", "curricula": ["ibdp"], "note": "오버우어젤 캠퍼스"},
    {"name": "메트로폴리탄 스쿨 프랑크푸르트", "name_en": "Metropolitan School Frankfurt", "country": "독일", "city": "프랑크푸르트", "curricula": ["ibdp"], "note": ""},
    {"name": "베를린 브란덴부르크 인터내셔널 스쿨 (BBIS)", "name_en": "Berlin Brandenburg International School", "country": "독일", "city": "베를린", "curricula": ["ibdp"], "note": "기숙 가능"},
    {"name": "베를린 인터내셔널 스쿨 (BIS)", "name_en": "Berlin International School", "country": "독일", "city": "베를린", "curricula": ["ibdp"], "note": ""},
    {"name": "베를린 메트로폴리탄 스쿨 (BMS)", "name_en": "Berlin Metropolitan School", "country": "독일", "city": "베를린", "curricula": ["ibdp"], "note": ""},
    {"name": "존 F. 케네디 스쿨 베를린 (JFKS)", "name_en": "John F. Kennedy School Berlin", "country": "독일", "city": "베를린", "curricula": [], "note": "독일-미국 이중언어 공립학교"},
    {"name": "뮌헨 인터내셔널 스쿨 (MIS)", "name_en": "Munich International School", "country": "독일", "city": "뮌헨", "curricula": ["ibdp"], "note": ""},
    {"name": "바바리안 인터내셔널 스쿨 (BIS)", "name_en": "Bavarian International School", "country": "독일", "city": "뮌헨", "curricula": ["ibdp"], "note": ""},
    {"name": "인터내셔널 스쿨 오브 뒤셀도르프 (ISD)", "name_en": "International School of Düsseldorf", "country": "독일", "city": "뒤셀도르프", "curricula": ["ibdp"], "note": ""},
    {"name": "인터내셔널 스쿨 함부르크 (ISH)", "name_en": "International School Hamburg", "country": "독일", "city": "함부르크", "curricula": ["ibdp"], "note": ""},

    # ---------------- 프랑스 ----------------
    {"name": "아메리칸 스쿨 오브 파리 (ASP)", "name_en": "American School of Paris", "country": "프랑스", "city": "파리", "curricula": ["ibdp", "ap"], "note": "미국식 커리큘럼, 생클루 캠퍼스"},
    {"name": "인터내셔널 스쿨 오브 파리 (ISP)", "name_en": "International School of Paris", "country": "프랑스", "city": "파리", "curricula": ["ibdp"], "note": "IB 연속과정 운영"},
    {"name": "브리티시 스쿨 오브 파리 (BSP)", "name_en": "The British School of Paris", "country": "프랑스", "city": "파리", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "에콜 자닌 마뉘엘", "name_en": "École Jeannine Manuel", "country": "프랑스", "city": "파리", "curricula": ["ibdp"], "note": "프랑스-영어 이중언어 학교"},
    {"name": "리세 앵테르나시오날 드 생제르맹앙레", "name_en": "Lycée International de Saint-Germain-en-Laye", "country": "프랑스", "city": "파리", "curricula": [], "note": "국제 섹션 운영 공립학교"},
    {"name": "에르미타주 인터내셔널 스쿨", "name_en": "Ermitage International School", "country": "프랑스", "city": "파리(메종라피트)", "curricula": ["ibdp"], "note": "기숙 가능"},

    # ---------------- 네덜란드 ----------------
    {"name": "인터내셔널 스쿨 오브 암스테르담 (ISA)", "name_en": "International School of Amsterdam", "country": "네덜란드", "city": "암스테르담", "curricula": ["ibdp"], "note": "IB 연속과정 운영"},
    {"name": "브리티시 스쿨 오브 암스테르담 (BSA)", "name_en": "The British School of Amsterdam", "country": "네덜란드", "city": "암스테르담", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "아메리칸 스쿨 오브 더 헤이그 (ASH)", "name_en": "American School of The Hague", "country": "네덜란드", "city": "헤이그", "curricula": ["ibdp"], "note": "미국식 커리큘럼"},
    {"name": "인터내셔널 스쿨 오브 더 헤이그 (ISH)", "name_en": "The International School of The Hague", "country": "네덜란드", "city": "헤이그", "curricula": ["ibdp"], "note": ""},
    {"name": "브리티시 스쿨 인 더 네덜란즈 (BSN)", "name_en": "The British School in the Netherlands", "country": "네덜란드", "city": "헤이그", "curricula": ["igcse", "alevel", "ibdp"], "note": "영국식 커리큘럼"},

    # ---------------- 벨기에 ----------------
    {"name": "인터내셔널 스쿨 오브 브뤼셀 (ISB)", "name_en": "International School of Brussels", "country": "벨기에", "city": "브뤼셀", "curricula": ["ibdp"], "note": ""},
    {"name": "브리티시 스쿨 오브 브뤼셀 (BSB)", "name_en": "The British School of Brussels", "country": "벨기에", "city": "브뤼셀", "curricula": ["igcse", "alevel", "ibdp"], "note": "영국식 커리큘럼"},
    {"name": "세인트 존스 인터내셔널 스쿨", "name_en": "St. John's International School", "country": "벨기에", "city": "브뤼셀(워털루)", "curricula": ["ibdp"], "note": ""},

    # ---------------- 스위스 ----------------
    {"name": "인터내셔널 스쿨 오브 제네바 (에콜린)", "name_en": "International School of Geneva (Ecolint)", "country": "스위스", "city": "제네바", "curricula": ["ibdp"], "note": "3개 캠퍼스 운영"},
    {"name": "콜레주 뒤 레망 (CDL)", "name_en": "Collège du Léman", "country": "스위스", "city": "제네바", "curricula": ["ibdp"], "note": "기숙 가능"},
    {"name": "르 로제", "name_en": "Institut Le Rosey", "country": "스위스", "city": "롤", "curricula": ["ibdp"], "note": "보딩스쿨"},
    {"name": "취리히 인터내셔널 스쿨 (ZIS)", "name_en": "Zurich International School", "country": "스위스", "city": "취리히", "curricula": ["ibdp"], "note": ""},
    {"name": "인터커뮤니티 스쿨 취리히 (ICS)", "name_en": "Inter-Community School Zurich", "country": "스위스", "city": "취리히", "curricula": ["ibdp"], "note": "IB 연속과정 운영"},
    {"name": "인터내셔널 스쿨 오브 로잔 (ISL)", "name_en": "International School of Lausanne", "country": "스위스", "city": "로잔", "curricula": ["ibdp"], "note": ""},
    {"name": "브리앙몽 인터내셔널 스쿨", "name_en": "Brillantmont International School", "country": "스위스", "city": "로잔", "curricula": ["igcse", "alevel"], "note": "보딩스쿨"},
    {"name": "에글롱 칼리지", "name_en": "Aiglon College", "country": "스위스", "city": "빌라르", "curricula": ["ibdp"], "note": "보딩스쿨"},
    {"name": "레장 아메리칸 스쿨 (LAS)", "name_en": "Leysin American School", "country": "스위스", "city": "레장", "curricula": ["ibdp", "ap"], "note": "미국식 커리큘럼, 보딩스쿨"},
    {"name": "TASIS 스위스", "name_en": "TASIS The American School in Switzerland", "country": "스위스", "city": "루가노", "curricula": ["ibdp", "ap"], "note": "미국식 커리큘럼, 보딩스쿨"},

    # ---------------- 스페인 ----------------
    {"name": "아메리칸 스쿨 오브 마드리드 (ASM)", "name_en": "American School of Madrid", "country": "스페인", "city": "마드리드", "curricula": ["ibdp", "ap"], "note": "미국식 커리큘럼"},
    {"name": "인터내셔널 칼리지 스페인 (ICS)", "name_en": "International College Spain", "country": "스페인", "city": "마드리드", "curricula": ["ibdp"], "note": "IB 연속과정 운영"},
    {"name": "킹스 칼리지 마드리드", "name_en": "King's College, The British School of Madrid", "country": "스페인", "city": "마드리드", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "아메리칸 스쿨 오브 바르셀로나 (ASB)", "name_en": "American School of Barcelona", "country": "스페인", "city": "바르셀로나", "curricula": ["ibdp"], "note": "미국식 커리큘럼"},
    {"name": "벤자민 프랭클린 인터내셔널 스쿨 (BFIS)", "name_en": "Benjamin Franklin International School", "country": "스페인", "city": "바르셀로나", "curricula": ["ibdp"], "note": "미국식 커리큘럼"},
    {"name": "브리티시 스쿨 오브 바르셀로나 (BSB)", "name_en": "The British School of Barcelona", "country": "스페인", "city": "바르셀로나", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},

    # ---------------- 이탈리아 ----------------
    {"name": "아메리칸 스쿨 오브 밀란 (ASM)", "name_en": "American School of Milan", "country": "이탈리아", "city": "밀라노", "curricula": ["ibdp"], "note": "미국식 커리큘럼"},
    {"name": "인터내셔널 스쿨 오브 밀란 (ISM)", "name_en": "International School of Milan", "country": "이탈리아", "city": "밀라노", "curricula": ["ibdp"], "note": ""},
    {"name": "브리티시 스쿨 오브 밀란", "name_en": "The British School of Milan", "country": "이탈리아", "city": "밀라노", "curricula": ["igcse"], "note": "영국식 커리큘럼"},
    {"name": "아메리칸 오버시즈 스쿨 오브 로마 (AOSR)", "name_en": "American Overseas School of Rome", "country": "이탈리아", "city": "로마", "curricula": ["ibdp", "ap"], "note": "미국식 커리큘럼"},
    {"name": "세인트 스티븐스 스쿨 로마", "name_en": "St. Stephen's School", "country": "이탈리아", "city": "로마", "curricula": ["ibdp"], "note": "기숙 가능"},
    {"name": "메리마운트 인터내셔널 스쿨 로마", "name_en": "Marymount International School Rome", "country": "이탈리아", "city": "로마", "curricula": ["ibdp"], "note": ""},
    {"name": "세인트 조지스 브리티시 인터내셔널 스쿨", "name_en": "St. George's British International School", "country": "이탈리아", "city": "로마", "curricula": ["igcse", "ibdp"], "note": "영국식 커리큘럼"},

    # ---------------- 오스트리아 ----------------
    {"name": "아메리칸 인터내셔널 스쿨 비엔나 (AIS)", "name_en": "American International School Vienna", "country": "오스트리아", "city": "빈", "curricula": ["ibdp"], "note": "미국식 커리큘럼"},
    {"name": "비엔나 인터내셔널 스쿨 (VIS)", "name_en": "Vienna International School", "country": "오스트리아", "city": "빈", "curricula": ["ibdp"], "note": "IB 연속과정 운영"},

    # ---------------- 체코 ----------------
    {"name": "인터내셔널 스쿨 오브 프라하 (ISP)", "name_en": "International School of Prague", "country": "체코", "city": "프라하", "curricula": ["ibdp"], "note": ""},
    {"name": "프라하 브리티시 인터내셔널 스쿨 (PBIS)", "name_en": "Prague British International School", "country": "체코", "city": "프라하", "curricula": ["igcse", "ibdp"], "note": "노드 앵글리아 계열"},

    # ---------------- 폴란드 ----------------
    {"name": "아메리칸 스쿨 오브 바르샤바 (ASW)", "name_en": "American School of Warsaw", "country": "폴란드", "city": "바르샤바", "curricula": ["ibdp"], "note": "미국식 커리큘럼"},
    {"name": "브리티시 스쿨 바르샤바", "name_en": "The British School Warsaw", "country": "폴란드", "city": "바르샤바", "curricula": ["igcse", "ibdp"], "note": "노드 앵글리아 계열"},

    # ---------------- 헝가리 ----------------
    {"name": "아메리칸 인터내셔널 스쿨 오브 부다페스트 (AISB)", "name_en": "American International School of Budapest", "country": "헝가리", "city": "부다페스트", "curricula": ["ibdp"], "note": "미국식 커리큘럼"},
    {"name": "브리티시 인터내셔널 스쿨 부다페스트 (BISB)", "name_en": "The British International School Budapest", "country": "헝가리", "city": "부다페스트", "curricula": ["igcse", "ibdp"], "note": "노드 앵글리아 계열"},

    # ---------------- 스웨덴 ----------------
    {"name": "스톡홀름 인터내셔널 스쿨 (SIS)", "name_en": "Stockholm International School", "country": "스웨덴", "city": "스톡홀름", "curricula": ["ibdp"], "note": ""},
    {"name": "인터내셔널 스쿨 오브 더 스톡홀름 리전 (ISSR)", "name_en": "International School of the Stockholm Region", "country": "스웨덴", "city": "스톡홀름", "curricula": ["ibdp"], "note": "시립 국제학교"},

    # ---------------- 덴마크 ----------------
    {"name": "코펜하겐 인터내셔널 스쿨 (CIS)", "name_en": "Copenhagen International School", "country": "덴마크", "city": "코펜하겐", "curricula": ["ibdp"], "note": "IB 연속과정 운영"},

    # ---------------- 핀란드 ----------------
    {"name": "인터내셔널 스쿨 오브 헬싱키 (ISH)", "name_en": "International School of Helsinki", "country": "핀란드", "city": "헬싱키", "curricula": ["ibdp"], "note": ""},

    # ---------------- 호주 ----------------
    {"name": "인터내셔널 그래머 스쿨 (IGS)", "name_en": "International Grammar School", "country": "호주", "city": "시드니", "curricula": [], "note": "이중언어 교육"},
    {"name": "레드랜즈 (시드니)", "name_en": "Redlands (Sydney Church of England Coeducational Grammar School)", "country": "호주", "city": "시드니", "curricula": ["ibdp"], "note": "HSC·IB 병행"},
    {"name": "크랜브룩 스쿨 시드니", "name_en": "Cranbrook School", "country": "호주", "city": "시드니", "curricula": ["ibdp"], "note": "HSC·IB 병행"},
    {"name": "MLC 스쿨 시드니", "name_en": "MLC School", "country": "호주", "city": "시드니", "curricula": ["ibdp"], "note": "여학교, HSC·IB 병행"},
    {"name": "트리니티 그래머 스쿨 시드니", "name_en": "Trinity Grammar School", "country": "호주", "city": "시드니", "curricula": ["ibdp"], "note": "HSC·IB 병행"},
    {"name": "뉴잉턴 칼리지", "name_en": "Newington College", "country": "호주", "city": "시드니", "curricula": ["ibdp"], "note": "HSC·IB 병행"},
    {"name": "웨슬리 칼리지 멜버른", "name_en": "Wesley College", "country": "호주", "city": "멜버른", "curricula": ["ibdp"], "note": "VCE·IB 병행"},
    {"name": "캐리 뱁티스트 그래머 스쿨", "name_en": "Carey Baptist Grammar School", "country": "호주", "city": "멜버른", "curricula": ["ibdp"], "note": "VCE·IB 병행"},
    {"name": "메소디스트 레이디스 칼리지 (MLC 멜버른)", "name_en": "Methodist Ladies' College", "country": "호주", "city": "멜버른", "curricula": ["ibdp"], "note": "여학교, VCE·IB 병행"},
    {"name": "퀸즐랜드 아카데미 과학수학기술 (QASMT)", "name_en": "Queensland Academy for Science, Mathematics and Technology", "country": "호주", "city": "브리즈번", "curricula": ["ibdp"], "note": "공립 IB 전문학교"},
    {"name": "인터내셔널 스쿨 오브 웨스턴 오스트레일리아 (ISWA)", "name_en": "International School of Western Australia", "country": "호주", "city": "퍼스", "curricula": ["ibdp"], "note": ""},
    {"name": "프레스비테리언 레이디스 칼리지 퍼스 (PLC)", "name_en": "Presbyterian Ladies' College", "country": "호주", "city": "퍼스", "curricula": ["ibdp"], "note": "여학교, WACE·IB 병행"},

    # ---------------- 뉴질랜드 ----------------
    {"name": "ACG 파넬 칼리지", "name_en": "ACG Parnell College", "country": "뉴질랜드", "city": "오클랜드", "curricula": ["igcse", "alevel"], "note": "케임브리지 과정"},
    {"name": "크리스틴 스쿨", "name_en": "Kristin School", "country": "뉴질랜드", "city": "오클랜드", "curricula": ["ibdp"], "note": "NCEA·IB 병행"},
    {"name": "오클랜드 인터내셔널 칼리지 (AIC)", "name_en": "Auckland International College", "country": "뉴질랜드", "city": "오클랜드", "curricula": ["ibdp"], "note": "IB DP 전문 고등학교"},
    {"name": "다이오시전 스쿨 포 걸스", "name_en": "Diocesan School for Girls", "country": "뉴질랜드", "city": "오클랜드", "curricula": ["ibdp"], "note": "여학교, NCEA·IB 병행"},
    {"name": "세인트 켄티건 칼리지", "name_en": "Saint Kentigern College", "country": "뉴질랜드", "city": "오클랜드", "curricula": ["ibdp"], "note": "NCEA·IB 병행"},

    # ---------------- 캐나다 ----------------
    {"name": "토론토 프렌치 스쿨 (TFS)", "name_en": "TFS - Canada's International School", "country": "캐나다", "city": "토론토", "curricula": ["ibdp"], "note": "영어-프랑스어 이중언어"},
    {"name": "어퍼 캐나다 칼리지 (UCC)", "name_en": "Upper Canada College", "country": "캐나다", "city": "토론토", "curricula": ["ibdp"], "note": "남학교, 기숙 가능"},
    {"name": "브랭섬 홀", "name_en": "Branksome Hall", "country": "캐나다", "city": "토론토", "curricula": ["ibdp"], "note": "여학교, IB 연속과정 운영"},
    {"name": "멀그레이브 스쿨", "name_en": "Mulgrave School", "country": "캐나다", "city": "밴쿠버", "curricula": ["ibdp"], "note": "IB 연속과정 운영"},
    {"name": "세인트 조지스 스쿨 밴쿠버", "name_en": "St. George's School", "country": "캐나다", "city": "밴쿠버", "curricula": ["ap"], "note": "남학교, 기숙 가능"},
    {"name": "스트랫퍼드 홀", "name_en": "Stratford Hall", "country": "캐나다", "city": "밴쿠버", "curricula": ["ibdp"], "note": "IB 연속과정 운영"},
    {"name": "메도우리지 스쿨", "name_en": "Meadowridge School", "country": "캐나다", "city": "밴쿠버(메이플리지)", "curricula": ["ibdp"], "note": "IB 연속과정 운영"},
    {"name": "웨스트 포인트 그레이 아카데미 (WPGA)", "name_en": "West Point Grey Academy", "country": "캐나다", "city": "밴쿠버", "curricula": ["ap"], "note": ""},

    # ---------------- 미국 (보딩스쿨) ----------------
    {"name": "필립스 엑서터 아카데미", "name_en": "Phillips Exeter Academy", "country": "미국", "city": "뉴햄프셔 엑서터", "curricula": [], "note": "보딩스쿨"},
    {"name": "필립스 아카데미 앤도버", "name_en": "Phillips Academy Andover", "country": "미국", "city": "매사추세츠 앤도버", "curricula": [], "note": "보딩스쿨"},
    {"name": "초트 로즈마리 홀", "name_en": "Choate Rosemary Hall", "country": "미국", "city": "코네티컷 월링퍼드", "curricula": [], "note": "보딩스쿨"},
    {"name": "디어필드 아카데미", "name_en": "Deerfield Academy", "country": "미국", "city": "매사추세츠 디어필드", "curricula": [], "note": "보딩스쿨"},
    {"name": "하치키스 스쿨", "name_en": "The Hotchkiss School", "country": "미국", "city": "코네티컷 레이크빌", "curricula": [], "note": "보딩스쿨"},
    {"name": "로렌스빌 스쿨", "name_en": "The Lawrenceville School", "country": "미국", "city": "뉴저지 로렌스빌", "curricula": [], "note": "보딩스쿨"},
    {"name": "세인트 폴스 스쿨", "name_en": "St. Paul's School", "country": "미국", "city": "뉴햄프셔 콩코드", "curricula": [], "note": "전원 기숙 보딩스쿨"},
    {"name": "그로턴 스쿨", "name_en": "Groton School", "country": "미국", "city": "매사추세츠 그로턴", "curricula": [], "note": "보딩스쿨"},
    {"name": "밀턴 아카데미", "name_en": "Milton Academy", "country": "미국", "city": "매사추세츠 밀턴", "curricula": [], "note": "보딩스쿨"},
    {"name": "태프트 스쿨", "name_en": "The Taft School", "country": "미국", "city": "코네티컷 워터타운", "curricula": ["ap"], "note": "보딩스쿨"},
    {"name": "루미스 채피 스쿨", "name_en": "The Loomis Chaffee School", "country": "미국", "city": "코네티컷 윈저", "curricula": ["ap"], "note": "보딩스쿨"},
    {"name": "케이트 스쿨", "name_en": "Cate School", "country": "미국", "city": "캘리포니아 카핀테리아", "curricula": [], "note": "보딩스쿨"},
    {"name": "대처 스쿨", "name_en": "The Thacher School", "country": "미국", "city": "캘리포니아 오하이", "curricula": [], "note": "보딩스쿨"},
    {"name": "페디 스쿨", "name_en": "The Peddie School", "country": "미국", "city": "뉴저지 하이츠타운", "curricula": ["ap"], "note": "보딩스쿨"},
    {"name": "블레어 아카데미", "name_en": "Blair Academy", "country": "미국", "city": "뉴저지 블레어스타운", "curricula": ["ap"], "note": "보딩스쿨"},
    {"name": "힐 스쿨", "name_en": "The Hill School", "country": "미국", "city": "펜실베이니아 포츠타운", "curricula": ["ap"], "note": "보딩스쿨"},
    {"name": "머서스버그 아카데미", "name_en": "Mercersburg Academy", "country": "미국", "city": "펜실베이니아 머서스버그", "curricula": ["ap"], "note": "보딩스쿨"},
    {"name": "노스필드 마운트 허먼 (NMH)", "name_en": "Northfield Mount Hermon School", "country": "미국", "city": "매사추세츠 길", "curricula": ["ap"], "note": "보딩스쿨"},
    {"name": "크랜브룩 스쿨", "name_en": "Cranbrook Schools", "country": "미국", "city": "미시간 블룸필드힐스", "curricula": ["ap"], "note": "보딩·통학 병행"},
    {"name": "웹 스쿨스", "name_en": "The Webb Schools", "country": "미국", "city": "캘리포니아 클레어몬트", "curricula": [], "note": "보딩스쿨"},
    {"name": "켄트 스쿨", "name_en": "Kent School", "country": "미국", "city": "코네티컷 켄트", "curricula": ["ap"], "note": "보딩스쿨"},
    {"name": "미들섹스 스쿨", "name_en": "Middlesex School", "country": "미국", "city": "매사추세츠 콩코드", "curricula": [], "note": "보딩스쿨"},
    {"name": "에피스코팔 하이스쿨", "name_en": "Episcopal High School", "country": "미국", "city": "버지니아 알렉산드리아", "curricula": [], "note": "전원 기숙 보딩스쿨"},
    {"name": "콩코드 아카데미", "name_en": "Concord Academy", "country": "미국", "city": "매사추세츠 콩코드", "curricula": [], "note": "보딩·통학 병행"},
    {"name": "헌 스쿨 오브 프린스턴", "name_en": "The Hun School of Princeton", "country": "미국", "city": "뉴저지 프린스턴", "curricula": ["ap"], "note": "보딩·통학 병행"},
    {"name": "체셔 아카데미", "name_en": "Cheshire Academy", "country": "미국", "city": "코네티컷 체셔", "curricula": ["ibdp"], "note": "보딩·통학 병행"},
    {"name": "웨스트민스터 스쿨 (코네티컷)", "name_en": "Westminster School", "country": "미국", "city": "코네티컷 심스버리", "curricula": ["ap"], "note": "보딩스쿨"},
    {"name": "엠마 윌라드 스쿨", "name_en": "Emma Willard School", "country": "미국", "city": "뉴욕 트로이", "curricula": [], "note": "여학교 보딩스쿨"},
    {"name": "미스 포터스 스쿨", "name_en": "Miss Porter's School", "country": "미국", "city": "코네티컷 파밍턴", "curricula": [], "note": "여학교 보딩스쿨"},
    {"name": "인터로켄 아츠 아카데미", "name_en": "Interlochen Arts Academy", "country": "미국", "city": "미시간 인터로켄", "curricula": ["ap"], "note": "예술 전문 보딩스쿨"},
    {"name": "컬버 아카데미", "name_en": "Culver Academies", "country": "미국", "city": "인디애나 컬버", "curricula": ["ap"], "note": "보딩스쿨"},

    # ---------------- 멕시코 ----------------
    {"name": "아메리칸 스쿨 파운데이션 (ASF)", "name_en": "The American School Foundation", "country": "멕시코", "city": "멕시코시티", "curricula": ["ibdp"], "note": "미국식 커리큘럼"},
    {"name": "그린게이츠 스쿨", "name_en": "Greengates School", "country": "멕시코", "city": "멕시코시티", "curricula": ["igcse", "ibdp"], "note": "영국식 커리큘럼"},

    # ---------------- 브라질 ----------------
    {"name": "그레이디드 스쿨 (상파울루 아메리칸 스쿨)", "name_en": "Graded - The American School of São Paulo", "country": "브라질", "city": "상파울루", "curricula": ["ibdp", "ap"], "note": "미국식 커리큘럼"},
    {"name": "세인트 폴스 스쿨 상파울루", "name_en": "St. Paul's School, São Paulo", "country": "브라질", "city": "상파울루", "curricula": ["igcse", "ibdp"], "note": "영국식 커리큘럼"},
    {"name": "채플 스쿨", "name_en": "Chapel School", "country": "브라질", "city": "상파울루", "curricula": [], "note": "미국식 커리큘럼"},
    {"name": "원 월드 국제학교 리야드 (OWIS Riyadh)", "name_en": "One World International School Riyadh", "country": "사우디아라비아", "city": "리야드", "curricula": [], "note": ""},
]
