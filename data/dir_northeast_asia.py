# -*- coding: utf-8 -*-
# 동북아시아(중국·홍콩·마카오·대만·일본·몽골) 국제학교 디렉터리
# curricula 키: "ibdp", "igcse", "ap", "alevel" — 고등 과정에서 실제 운영이 확실한 것만 기재, 불확실하면 []

SCHOOLS = [
    # ---------------- 중국 / 상하이 ----------------
    {"name": "상하이 아메리칸 스쿨 (SAS)", "name_en": "Shanghai American School", "country": "중국", "city": "상하이", "curricula": ["ap", "ibdp"], "note": "미국식 커리큘럼, 푸시·푸동 캠퍼스"},
    {"name": "콩코디아 인터내셔널 스쿨 상하이", "name_en": "Concordia International School Shanghai", "country": "중국", "city": "상하이", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "덜위치 칼리지 상하이 푸동", "name_en": "Dulwich College Shanghai Pudong", "country": "중국", "city": "상하이", "curricula": ["igcse", "ibdp"], "note": "영국식 커리큘럼"},
    {"name": "덜위치 칼리지 상하이 푸시", "name_en": "Dulwich College Shanghai Puxi", "country": "중국", "city": "상하이", "curricula": ["igcse", "ibdp"], "note": "영국식 커리큘럼"},
    {"name": "웰링턴 칼리지 인터내셔널 상하이", "name_en": "Wellington College International Shanghai", "country": "중국", "city": "상하이", "curricula": ["igcse", "ibdp"], "note": "영국식 커리큘럼"},
    {"name": "상하이 커뮤니티 인터내셔널 스쿨 (SCIS)", "name_en": "Shanghai Community International School", "country": "중국", "city": "상하이", "curricula": ["ibdp"], "note": "IB 연속과정"},
    {"name": "웨스턴 인터내셔널 스쿨 오브 상하이 (WISS)", "name_en": "Western International School of Shanghai", "country": "중국", "city": "상하이", "curricula": ["ibdp"], "note": "IB 연속과정"},
    {"name": "예청 국제학교 상하이 (YCIS)", "name_en": "Yew Chung International School of Shanghai", "country": "중국", "city": "상하이", "curricula": ["igcse", "ibdp"], "note": ""},
    {"name": "브리티시 인터내셔널 스쿨 상하이 푸시 (BISS)", "name_en": "The British International School Shanghai, Puxi", "country": "중국", "city": "상하이", "curricula": ["igcse", "ibdp"], "note": "노드 앵글리아 산하"},
    {"name": "노드 앵글리아 인터내셔널 스쿨 상하이 푸동 (NAIS)", "name_en": "Nord Anglia International School Shanghai, Pudong", "country": "중국", "city": "상하이", "curricula": ["igcse", "ibdp"], "note": "노드 앵글리아 산하"},
    {"name": "해로우 인터내셔널 스쿨 상하이", "name_en": "Harrow International School Shanghai", "country": "중국", "city": "상하이", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "상하이 싱가포르 국제학교 (SSIS)", "name_en": "Shanghai Singapore International School", "country": "중국", "city": "상하이", "curricula": ["igcse", "ibdp"], "note": ""},
    {"name": "상하이 유나이티드 국제학교 (SUIS)", "name_en": "Shanghai United International School", "country": "중국", "city": "상하이", "curricula": ["ibdp"], "note": "구베이 등 다수 캠퍼스"},
    {"name": "브리태니카 인터내셔널 스쿨 상하이", "name_en": "Britannica International School Shanghai", "country": "중국", "city": "상하이", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "상하이 하이스쿨 국제부 (SHSID)", "name_en": "Shanghai High School International Division", "country": "중국", "city": "상하이", "curricula": ["ap", "ibdp"], "note": "상하이중학 국제부"},
    {"name": "상하이 리빙스턴 아메리칸 스쿨", "name_en": "Shanghai Livingston American School", "country": "중국", "city": "상하이", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "YK 파오 스쿨", "name_en": "YK Pao School", "country": "중국", "city": "상하이", "curricula": ["igcse", "ibdp"], "note": "중영 이중언어 학교"},
    {"name": "홍차오 국제학교 (HQIS)", "name_en": "Hong Qiao International School", "country": "중국", "city": "상하이", "curricula": [], "note": ""},
    {"name": "상하이 SMIC 사립학교 국제부", "name_en": "SMIC Private School (International Division)", "country": "중국", "city": "상하이", "curricula": ["ap"], "note": "미국식 커리큘럼"},

    # ---------------- 중국 / 베이징 ----------------
    {"name": "인터내셔널 스쿨 오브 베이징 (ISB)", "name_en": "International School of Beijing", "country": "중국", "city": "베이징", "curricula": ["ibdp"], "note": "순이 지역"},
    {"name": "웨스턴 아카데미 오브 베이징 (WAB)", "name_en": "Western Academy of Beijing", "country": "중국", "city": "베이징", "curricula": ["ibdp"], "note": "IB 연속과정"},
    {"name": "베이징 시티 인터내셔널 스쿨 (BCIS)", "name_en": "Beijing City International School", "country": "중국", "city": "베이징", "curricula": ["ibdp"], "note": "IB 연속과정"},
    {"name": "덜위치 칼리지 베이징", "name_en": "Dulwich College Beijing", "country": "중국", "city": "베이징", "curricula": ["igcse", "ibdp"], "note": "영국식 커리큘럼"},
    {"name": "해로우 인터내셔널 스쿨 베이징", "name_en": "Harrow International School Beijing", "country": "중국", "city": "베이징", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "브리티시 스쿨 오브 베이징 순이 (BSB)", "name_en": "The British School of Beijing, Shunyi", "country": "중국", "city": "베이징", "curricula": ["igcse", "ibdp"], "note": "노드 앵글리아 산하"},
    {"name": "키스톤 아카데미", "name_en": "Keystone Academy", "country": "중국", "city": "베이징", "curricula": ["ibdp"], "note": "중영 이중언어, 기숙 운영"},
    {"name": "예청 국제학교 베이징 (YCIS)", "name_en": "Yew Chung International School of Beijing", "country": "중국", "city": "베이징", "curricula": ["igcse", "ibdp"], "note": ""},
    {"name": "캐나디안 인터내셔널 스쿨 오브 베이징 (CISB)", "name_en": "Canadian International School of Beijing", "country": "중국", "city": "베이징", "curricula": ["ibdp"], "note": ""},
    {"name": "베이징 월드 유스 아카데미 (BWYA)", "name_en": "Beijing World Youth Academy", "country": "중국", "city": "베이징", "curricula": ["ibdp"], "note": ""},
    {"name": "베이징 55중 국제부", "name_en": "Beijing No.55 High School International Student Section", "country": "중국", "city": "베이징", "curricula": ["ibdp"], "note": "공립학교 국제부"},
    {"name": "칭화 인터내셔널 스쿨 (THIS)", "name_en": "Tsinghua International School", "country": "중국", "city": "베이징", "curricula": ["ap"], "note": "미국식 커리큘럼"},

    # ---------------- 중국 / 광저우 ----------------
    {"name": "아메리칸 인터내셔널 스쿨 오브 광저우 (AISG)", "name_en": "American International School of Guangzhou", "country": "중국", "city": "광저우", "curricula": ["ibdp"], "note": ""},
    {"name": "유타로이 국제학교 광저우 (UISG)", "name_en": "Utahloy International School Guangzhou", "country": "중국", "city": "광저우", "curricula": ["ibdp"], "note": "IB 연속과정"},
    {"name": "유타로이 국제학교 쩡청 (UISZ)", "name_en": "Utahloy International School Zengcheng", "country": "중국", "city": "광저우", "curricula": ["ibdp"], "note": "기숙 운영"},
    {"name": "브리티시 스쿨 오브 광저우 (BSG)", "name_en": "The British School of Guangzhou", "country": "중국", "city": "광저우", "curricula": ["igcse", "ibdp"], "note": "노드 앵글리아 산하"},
    {"name": "캐나디안 인터내셔널 스쿨 오브 광저우 (CIS)", "name_en": "Canadian International School of Guangzhou", "country": "중국", "city": "광저우", "curricula": [], "note": "캐나다 온타리오 커리큘럼"},
    {"name": "ISA 사이언스시티 국제학교 광저우", "name_en": "ISA Science City International School of Guangzhou", "country": "중국", "city": "광저우", "curricula": ["ibdp"], "note": "IB 연속과정"},

    # ---------------- 중국 / 선전 ----------------
    {"name": "셔커우 인터내셔널 스쿨 (SIS)", "name_en": "Shekou International School", "country": "중국", "city": "선전", "curricula": ["ibdp"], "note": ""},
    {"name": "QSI 인터내셔널 스쿨 오브 선전", "name_en": "QSI International School of Shenzhen", "country": "중국", "city": "선전", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "인터내셔널 스쿨 오브 난산 선전 (ISNS)", "name_en": "International School of Nanshan Shenzhen", "country": "중국", "city": "선전", "curricula": ["ibdp"], "note": "IB 연속과정"},
    {"name": "선전 칼리지 오브 인터내셔널 에듀케이션 (SCIE)", "name_en": "Shenzhen College of International Education", "country": "중국", "city": "선전", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "베이시스 인터내셔널 스쿨 선전", "name_en": "BASIS International School Shenzhen", "country": "중국", "city": "선전", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "해로우 인터내셔널 스쿨 선전 첸하이", "name_en": "Harrow International School Shenzhen Qianhai", "country": "중국", "city": "선전", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "머치스턴 인터내셔널 스쿨 선전", "name_en": "Merchiston International School Shenzhen", "country": "중국", "city": "선전", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "선와이 국제학교 (SWIS)", "name_en": "Shen Wai International School", "country": "중국", "city": "선전", "curricula": ["ibdp"], "note": "IB 연속과정"},

    # ---------------- 중국 / 톈진 ----------------
    {"name": "인터내셔널 스쿨 오브 톈진 (IST)", "name_en": "International School of Tianjin", "country": "중국", "city": "톈진", "curricula": ["ibdp"], "note": "IB 연속과정"},
    {"name": "웰링턴 칼리지 인터내셔널 톈진", "name_en": "Wellington College International Tianjin", "country": "중국", "city": "톈진", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "톈진 인터내셔널 스쿨 (TIS)", "name_en": "Tianjin International School", "country": "중국", "city": "톈진", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "테다 인터내셔널 스쿨", "name_en": "Teda International School", "country": "중국", "city": "톈진", "curricula": [], "note": ""},

    # ---------------- 중국 / 칭다오 ----------------
    {"name": "칭다오 아메라시아 인터내셔널 스쿨 (QAIS)", "name_en": "Qingdao Amerasia International School", "country": "중국", "city": "칭다오", "curricula": ["ibdp"], "note": ""},
    {"name": "인터내셔널 스쿨 오브 칭다오 (ISQ)", "name_en": "International School of Qingdao", "country": "중국", "city": "칭다오", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "칭다오 제1국제학교 (QISS)", "name_en": "Qingdao No.1 International School of Shandong Province", "country": "중국", "city": "칭다오", "curricula": [], "note": ""},
    {"name": "말번 칼리지 칭다오", "name_en": "Malvern College Qingdao", "country": "중국", "city": "칭다오", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "예청 국제학교 칭다오 (YCIS)", "name_en": "Yew Chung International School of Qingdao", "country": "중국", "city": "칭다오", "curricula": ["igcse"], "note": ""},

    # ---------------- 중국 / 쑤저우 ----------------
    {"name": "덜위치 칼리지 쑤저우", "name_en": "Dulwich College Suzhou", "country": "중국", "city": "쑤저우", "curricula": ["igcse", "ibdp"], "note": "영국식 커리큘럼"},
    {"name": "쑤저우 싱가포르 국제학교 (SSIS)", "name_en": "Suzhou Singapore International School", "country": "중국", "city": "쑤저우", "curricula": ["ibdp"], "note": "IB 연속과정"},

    # ---------------- 중국 / 난징 ----------------
    {"name": "난징 인터내셔널 스쿨 (NIS)", "name_en": "Nanjing International School", "country": "중국", "city": "난징", "curricula": ["ibdp"], "note": "IB 연속과정"},
    {"name": "브리티시 스쿨 오브 난징 (BSN)", "name_en": "The British School of Nanjing", "country": "중국", "city": "난징", "curricula": [], "note": "노드 앵글리아 산하"},

    # ---------------- 중국 / 항저우 ----------------
    {"name": "항저우 인터내셔널 스쿨 (HIS)", "name_en": "Hangzhou International School", "country": "중국", "city": "항저우", "curricula": ["ibdp"], "note": ""},
    {"name": "웰링턴 칼리지 인터내셔널 항저우", "name_en": "Wellington College International Hangzhou", "country": "중국", "city": "항저우", "curricula": ["igcse", "ibdp"], "note": "영국식 커리큘럼"},

    # ---------------- 중국 / 청두 ----------------
    {"name": "레만 인터내셔널 스쿨 청두", "name_en": "Leman International School Chengdu", "country": "중국", "city": "청두", "curricula": ["ibdp"], "note": ""},
    {"name": "QSI 인터내셔널 스쿨 오브 청두", "name_en": "QSI International School of Chengdu", "country": "중국", "city": "청두", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "청두 인터내셔널 스쿨 (CDIS)", "name_en": "Chengdu International School", "country": "중국", "city": "청두", "curricula": [], "note": "미국식 커리큘럼"},

    # ---------------- 중국 / 다롄 ----------------
    {"name": "다롄 아메리칸 인터내셔널 스쿨 (DAIS)", "name_en": "Dalian American International School", "country": "중국", "city": "다롄", "curricula": [], "note": "미국식 커리큘럼"},
    {"name": "다롄 메이플리프 국제학교", "name_en": "Dalian Maple Leaf International School", "country": "중국", "city": "다롄", "curricula": [], "note": "캐나다 BC주 커리큘럼"},

    # ---------------- 중국 / 우한 ----------------
    {"name": "우한 양쯔 인터내셔널 스쿨 (WYIS)", "name_en": "Wuhan Yangtze International School", "country": "중국", "city": "우한", "curricula": [], "note": "미국식 커리큘럼"},

    # ---------------- 중국 / 시안 ----------------
    {"name": "시안 량자탄 국제학교 (XLIS)", "name_en": "Xi'an Liangjiatan International School", "country": "중국", "city": "시안", "curricula": ["ibdp"], "note": "IB 연속과정"},
    {"name": "시안 하노바 국제학교", "name_en": "Xi'an Hanova International School", "country": "중국", "city": "시안", "curricula": [], "note": ""},
    {"name": "시안 인터내셔널 스쿨 (XIS)", "name_en": "Xi'an International School", "country": "중국", "city": "시안", "curricula": [], "note": "미국식 커리큘럼"},

    # ---------------- 홍콩 ----------------
    {"name": "홍콩 인터내셔널 스쿨 (HKIS)", "name_en": "Hong Kong International School", "country": "홍콩", "city": "홍콩", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "캐나디안 인터내셔널 스쿨 오브 홍콩 (CDNIS)", "name_en": "Canadian International School of Hong Kong", "country": "홍콩", "city": "홍콩", "curricula": ["ibdp"], "note": "IB 연속과정"},
    {"name": "차이니즈 인터내셔널 스쿨 (CIS)", "name_en": "Chinese International School", "country": "홍콩", "city": "홍콩", "curricula": ["ibdp"], "note": "영중 이중언어"},
    {"name": "저먼 스위스 인터내셔널 스쿨 (GSIS)", "name_en": "German Swiss International School", "country": "홍콩", "city": "홍콩", "curricula": ["ibdp"], "note": "영어 스트림 IBDP, 독일어 스트림 별도"},
    {"name": "킹 조지 5세 스쿨 (KGV)", "name_en": "King George V School", "country": "홍콩", "city": "홍콩", "curricula": ["igcse", "ibdp"], "note": "ESF 산하"},
    {"name": "아일랜드 스쿨", "name_en": "Island School", "country": "홍콩", "city": "홍콩", "curricula": ["igcse", "ibdp"], "note": "ESF 산하"},
    {"name": "사우스 아일랜드 스쿨", "name_en": "South Island School", "country": "홍콩", "city": "홍콩", "curricula": ["igcse", "ibdp"], "note": "ESF 산하"},
    {"name": "웨스트 아일랜드 스쿨", "name_en": "West Island School", "country": "홍콩", "city": "홍콩", "curricula": ["igcse", "ibdp"], "note": "ESF 산하"},
    {"name": "샤틴 칼리지", "name_en": "Sha Tin College", "country": "홍콩", "city": "홍콩", "curricula": ["igcse", "ibdp"], "note": "ESF 산하"},
    {"name": "르네상스 칼리지", "name_en": "Renaissance College", "country": "홍콩", "city": "홍콩", "curricula": ["ibdp"], "note": "ESF 산하, IB 연속과정"},
    {"name": "디스커버리 칼리지", "name_en": "Discovery College", "country": "홍콩", "city": "홍콩", "curricula": ["ibdp"], "note": "ESF 산하, IB 연속과정"},
    {"name": "해로우 인터내셔널 스쿨 홍콩", "name_en": "Harrow International School Hong Kong", "country": "홍콩", "city": "홍콩", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "예청 국제학교 홍콩 (YCIS)", "name_en": "Yew Chung International School of Hong Kong", "country": "홍콩", "city": "홍콩", "curricula": ["igcse", "ibdp"], "note": ""},
    {"name": "빅토리아 상하이 아카데미 (VSA)", "name_en": "Victoria Shanghai Academy", "country": "홍콩", "city": "홍콩", "curricula": ["ibdp"], "note": "IB 연속과정"},
    {"name": "싱가포르 인터내셔널 스쿨 홍콩 (SIS)", "name_en": "Singapore International School (Hong Kong)", "country": "홍콩", "city": "홍콩", "curricula": ["igcse", "ibdp"], "note": ""},
    {"name": "오스트레일리안 인터내셔널 스쿨 홍콩 (AISHK)", "name_en": "Australian International School Hong Kong", "country": "홍콩", "city": "홍콩", "curricula": ["ibdp"], "note": "호주 HSC 과정 병행"},
    {"name": "프렌치 인터내셔널 스쿨 홍콩 (FIS)", "name_en": "French International School of Hong Kong", "country": "홍콩", "city": "홍콩", "curricula": ["ibdp"], "note": "국제 스트림 IBDP"},
    {"name": "홍콩 아카데미 (HKA)", "name_en": "Hong Kong Academy", "country": "홍콩", "city": "홍콩", "curricula": ["ibdp"], "note": "IB 연속과정"},
    {"name": "켈렛 스쿨", "name_en": "Kellett School", "country": "홍콩", "city": "홍콩", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "아메리칸 스쿨 홍콩 (ASHK)", "name_en": "American School Hong Kong", "country": "홍콩", "city": "홍콩", "curricula": [], "note": "미국식 커리큘럼"},
    {"name": "아메리칸 인터내셔널 스쿨 홍콩 (AIS)", "name_en": "American International School Hong Kong", "country": "홍콩", "city": "홍콩", "curricula": [], "note": "미국식 커리큘럼"},
    {"name": "크리스천 얼라이언스 인터내셔널 스쿨 (CAIS)", "name_en": "Christian Alliance International School", "country": "홍콩", "city": "홍콩", "curricula": [], "note": "캐나다 앨버타 커리큘럼"},
    {"name": "인터내셔널 크리스천 스쿨 (ICS)", "name_en": "International Christian School", "country": "홍콩", "city": "홍콩", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "노드 앵글리아 인터내셔널 스쿨 홍콩 (NAIS)", "name_en": "Nord Anglia International School Hong Kong", "country": "홍콩", "city": "홍콩", "curricula": ["igcse", "ibdp"], "note": "노드 앵글리아 산하"},
    {"name": "말번 칼리지 홍콩", "name_en": "Malvern College Hong Kong", "country": "홍콩", "city": "홍콩", "curricula": ["ibdp"], "note": "IB 연속과정"},
    {"name": "리포춘 유나이티드 월드 칼리지 (LPCUWC)", "name_en": "Li Po Chun United World College of Hong Kong", "country": "홍콩", "city": "홍콩", "curricula": ["ibdp"], "note": "UWC 산하, 2년제 기숙"},
    {"name": "ISF 아카데미", "name_en": "The Independent Schools Foundation Academy", "country": "홍콩", "city": "홍콩", "curricula": ["ibdp"], "note": "영중 이중언어"},
    {"name": "스탬포드 아메리칸 스쿨 홍콩", "name_en": "Stamford American School Hong Kong", "country": "홍콩", "city": "홍콩", "curricula": ["ibdp"], "note": ""},
    {"name": "델리아 스쿨 오브 캐나다", "name_en": "Delia School of Canada", "country": "홍콩", "city": "홍콩", "curricula": [], "note": "캐나다 온타리오 커리큘럼"},
    {"name": "디스커버리 베이 인터내셔널 스쿨 (DBIS)", "name_en": "Discovery Bay International School", "country": "홍콩", "city": "홍콩", "curricula": ["igcse"], "note": "영국식 커리큘럼"},

    # ---------------- 마카오 ----------------
    {"name": "인터내셔널 스쿨 오브 마카오 (TIS)", "name_en": "The International School of Macao", "country": "마카오", "city": "마카오", "curricula": ["ibdp"], "note": "캐나다 앨버타 커리큘럼 병행"},
    {"name": "마카오 앵글리칸 칼리지 (MAC)", "name_en": "Macau Anglican College", "country": "마카오", "city": "마카오", "curricula": ["ibdp"], "note": ""},
    {"name": "스쿨 오브 더 네이션스", "name_en": "School of the Nations", "country": "마카오", "city": "마카오", "curricula": [], "note": ""},

    # ---------------- 대만 ----------------
    {"name": "타이베이 아메리칸 스쿨 (TAS)", "name_en": "Taipei American School", "country": "대만", "city": "타이베이", "curricula": ["ap", "ibdp"], "note": "미국식 커리큘럼"},
    {"name": "타이베이 유러피언 스쿨 (TES)", "name_en": "Taipei European School", "country": "대만", "city": "타이베이", "curricula": ["igcse", "ibdp"], "note": "영국·프랑스·독일 섹션 운영"},
    {"name": "도미니칸 인터내셔널 스쿨", "name_en": "Dominican International School", "country": "대만", "city": "타이베이", "curricula": [], "note": "미국식 커리큘럼"},
    {"name": "모리슨 아카데미 타이베이", "name_en": "Morrison Academy Taipei", "country": "대만", "city": "타이베이", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "모리슨 아카데미 타이중", "name_en": "Morrison Academy Taichung", "country": "대만", "city": "타이중", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "아메리칸 스쿨 인 타이중 (AST)", "name_en": "American School in Taichung", "country": "대만", "city": "타이중", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "가오슝 아메리칸 스쿨 (KAS)", "name_en": "Kaohsiung American School", "country": "대만", "city": "가오슝", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "모리슨 아카데미 가오슝", "name_en": "Morrison Academy Kaohsiung", "country": "대만", "city": "가오슝", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "이소우 국제학교 (IIS)", "name_en": "I-Shou International School", "country": "대만", "city": "가오슝", "curricula": ["ibdp"], "note": ""},
    {"name": "신주 인터내셔널 스쿨 (HIS)", "name_en": "Hsinchu International School", "country": "대만", "city": "신주", "curricula": [], "note": "미국식 커리큘럼"},
    {"name": "신주현 아메리칸 스쿨 (HCAS)", "name_en": "Hsinchu County American School", "country": "대만", "city": "신주", "curricula": [], "note": "미국식 커리큘럼"},
    {"name": "퍼시픽 아메리칸 스쿨 (PAS)", "name_en": "Pacific American School", "country": "대만", "city": "신주", "curricula": [], "note": "미국식 커리큘럼"},

    # ---------------- 일본 ----------------
    {"name": "아메리칸 스쿨 인 재팬 (ASIJ)", "name_en": "The American School in Japan", "country": "일본", "city": "도쿄", "curricula": ["ap"], "note": "미국식 커리큘럼, 초후 캠퍼스"},
    {"name": "브리티시 스쿨 인 도쿄 (BST)", "name_en": "The British School in Tokyo", "country": "일본", "city": "도쿄", "curricula": ["igcse", "alevel"], "note": "영국식 커리큘럼"},
    {"name": "니시마치 인터내셔널 스쿨", "name_en": "Nishimachi International School", "country": "일본", "city": "도쿄", "curricula": [], "note": "유치~9학년"},
    {"name": "세이센 인터내셔널 스쿨", "name_en": "Seisen International School", "country": "일본", "city": "도쿄", "curricula": ["ibdp"], "note": "가톨릭 여학교"},
    {"name": "세인트 메리즈 인터내셔널 스쿨", "name_en": "St. Mary's International School", "country": "일본", "city": "도쿄", "curricula": ["ibdp"], "note": "가톨릭 남학교"},
    {"name": "인터내셔널 스쿨 오브 더 세이크리드 하트 (ISSH)", "name_en": "International School of the Sacred Heart", "country": "일본", "city": "도쿄", "curricula": [], "note": "가톨릭 여학교"},
    {"name": "도쿄 인터내셔널 스쿨 (TIS)", "name_en": "Tokyo International School", "country": "일본", "city": "도쿄", "curricula": [], "note": ""},
    {"name": "크리스천 아카데미 인 재팬 (CAJ)", "name_en": "Christian Academy in Japan", "country": "일본", "city": "도쿄", "curricula": ["ap"], "note": "미국식 커리큘럼, 히가시쿠루메"},
    {"name": "K 인터내셔널 스쿨 도쿄 (KIST)", "name_en": "K. International School Tokyo", "country": "일본", "city": "도쿄", "curricula": ["ibdp"], "note": "IB 연속과정"},
    {"name": "아오바 재팬 인터내셔널 스쿨", "name_en": "Aoba-Japan International School", "country": "일본", "city": "도쿄", "curricula": ["ibdp"], "note": "IB 연속과정"},
    {"name": "캐나디안 인터내셔널 스쿨 도쿄", "name_en": "Canadian International School Tokyo", "country": "일본", "city": "도쿄", "curricula": [], "note": "캐나다 온타리오 커리큘럼"},
    {"name": "뉴 인터내셔널 스쿨 오브 재팬", "name_en": "New International School of Japan", "country": "일본", "city": "도쿄", "curricula": [], "note": ""},
    {"name": "말번 칼리지 도쿄", "name_en": "Malvern College Tokyo", "country": "일본", "city": "도쿄", "curricula": [], "note": "고다이라 캠퍼스"},
    {"name": "요코하마 인터내셔널 스쿨 (YIS)", "name_en": "Yokohama International School", "country": "일본", "city": "요코하마", "curricula": ["ibdp"], "note": "IB 연속과정"},
    {"name": "세인트 모어 인터내셔널 스쿨", "name_en": "Saint Maur International School", "country": "일본", "city": "요코하마", "curricula": ["ibdp"], "note": ""},
    {"name": "호라이즌 재팬 인터내셔널 스쿨", "name_en": "Horizon Japan International School", "country": "일본", "city": "요코하마", "curricula": [], "note": ""},
    {"name": "오사카 인터내셔널 스쿨 (OIS)", "name_en": "Osaka International School of Kwansei Gakuin", "country": "일본", "city": "오사카", "curricula": ["ibdp"], "note": "관서학원 산하"},
    {"name": "오사카 YMCA 인터내셔널 스쿨", "name_en": "Osaka YMCA International School", "country": "일본", "city": "오사카", "curricula": [], "note": ""},
    {"name": "캐나디안 아카데미", "name_en": "Canadian Academy", "country": "일본", "city": "고베", "curricula": ["ibdp"], "note": "롯코 아일랜드"},
    {"name": "마리스트 브라더스 인터내셔널 스쿨", "name_en": "Marist Brothers International School", "country": "일본", "city": "고베", "curricula": [], "note": ""},
    {"name": "나고야 인터내셔널 스쿨 (NIS)", "name_en": "Nagoya International School", "country": "일본", "city": "나고야", "curricula": ["ibdp"], "note": "IB 연속과정"},
    {"name": "후쿠오카 인터내셔널 스쿨 (FIS)", "name_en": "Fukuoka International School", "country": "일본", "city": "후쿠오카", "curricula": ["ibdp"], "note": ""},

    # ---------------- 몽골 ----------------
    {"name": "인터내셔널 스쿨 오브 울란바토르 (ISU)", "name_en": "International School of Ulaanbaatar", "country": "몽골", "city": "울란바토르", "curricula": ["ibdp"], "note": "IB 연속과정"},
    {"name": "아메리칸 스쿨 오브 울란바토르 (ASU)", "name_en": "American School of Ulaanbaatar", "country": "몽골", "city": "울란바토르", "curricula": [], "note": "미국식 커리큘럼"},
    {"name": "브리티시 스쿨 오브 울란바토르", "name_en": "The British School of Ulaanbaatar", "country": "몽골", "city": "울란바토르", "curricula": [], "note": "영국식 커리큘럼"},
]
