# -*- coding: utf-8 -*-
# 국내 국제학교·외국인학교·국제고 디렉토리. curricula는 확신 있는 것만(학교 공식 안내·기존 저널 확인분), 아니면 [].
SCHOOLS = [
    # 서울
    {"name": "서울외국인학교 (SFS)", "name_en": "Seoul Foreign School", "country": "대한민국", "city": "서울", "curricula": ["ibdp"], "note": "IB 트랙·영국식 트랙 2개 운영(학교 공식 안내)"},
    {"name": "서울용산국제학교 (YISS)", "name_en": "Yongsan International School of Seoul", "country": "대한민국", "city": "서울", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "드와이트 외국인학교 서울", "name_en": "Dwight School Seoul", "country": "대한민국", "city": "서울", "curricula": ["ibdp"], "note": "PYP·MYP·DP 전 과정 IB(IB 디렉토리 확인)"},
    {"name": "한국외국인학교 서울캠퍼스 (KIS Seoul)", "name_en": "Korea International School Seoul Campus", "country": "대한민국", "city": "서울", "curricula": [], "note": "초등 전용 캠퍼스(학교 공식 안내)"},
    {"name": "덜위치 칼리지 서울", "name_en": "Dulwich College Seoul", "country": "대한민국", "city": "서울", "curricula": ["igcse", "ibdp"], "note": "영국식 커리큘럼, IGCSE 후 IB DP"},
    {"name": "아시아퍼시픽국제외국인학교 (APIS)", "name_en": "Asia Pacific International School", "country": "대한민국", "city": "서울", "curricula": [], "note": "K-12"},
    {"name": "한국켄트외국인학교 (KKFS)", "name_en": "Korea Kent Foreign School", "country": "대한민국", "city": "서울", "curricula": [], "note": "미국식 커리큘럼"},
    {"name": "서울프랑스학교 (LFS)", "name_en": "Lycée Français de Séoul", "country": "대한민국", "city": "서울", "curricula": [], "note": "프랑스 교육과정, 영어 섹션(SIA) 운영"},
    {"name": "서울독일학교 (DSSI)", "name_en": "Deutsche Schule Seoul International", "country": "대한민국", "city": "서울", "curricula": [], "note": "독일 아비투어 과정"},
    {"name": "하비에르 국제학교", "name_en": "Xavier International School", "country": "대한민국", "city": "서울", "curricula": [], "note": ""},
    {"name": "서울국제고등학교", "name_en": "Seoul Global High School", "country": "대한민국", "city": "서울", "curricula": [], "note": "공립 국제고"},
    # 경기
    {"name": "서울국제학교 (SIS)", "name_en": "Seoul International School", "country": "대한민국", "city": "경기 성남", "curricula": ["ap"], "note": "AP 과목 24개(학교 공식 안내)"},
    {"name": "한국외국인학교 판교 (KIS Pangyo)", "name_en": "Korea International School Pangyo", "country": "대한민국", "city": "경기 성남", "curricula": ["ap"], "note": "PK~12, AP 과목 26개(학교 공식 안내)"},
    {"name": "경기수원외국인학교 (GSIS)", "name_en": "Gyeonggi Suwon International School", "country": "대한민국", "city": "경기 수원", "curricula": ["ibdp"], "note": "IB 학교"},
    {"name": "청심국제중고등학교", "name_en": "Cheongshim International Academy", "country": "대한민국", "city": "경기 가평", "curricula": [], "note": "사립 국제중·고"},
    {"name": "고양국제고등학교", "name_en": "Goyang Global High School", "country": "대한민국", "city": "경기 고양", "curricula": [], "note": "공립 국제고"},
    {"name": "동탄국제고등학교", "name_en": "Dongtan Global High School", "country": "대한민국", "city": "경기 화성", "curricula": [], "note": "공립 국제고"},
    {"name": "국제크리스천스쿨 평택 (ICS Pyeongtaek)", "name_en": "International Christian School Pyeongtaek", "country": "대한민국", "city": "경기 평택", "curricula": [], "note": "미국식 커리큘럼"},
    # 인천
    {"name": "채드윅 송도국제학교", "name_en": "Chadwick International", "country": "대한민국", "city": "인천 송도", "curricula": ["ibdp"], "note": "PK~G12, IB 인가 프로그램 운영(학교 공식 안내)"},
    {"name": "청라달튼외국인학교 (CDS)", "name_en": "Cheongna Dalton School", "country": "대한민국", "city": "인천 청라", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "인천국제고등학교", "name_en": "Incheon International High School", "country": "대한민국", "city": "인천", "curricula": [], "note": "공립 국제고"},
    # 제주
    {"name": "NLCS 제주", "name_en": "North London Collegiate School Jeju", "country": "대한민국", "city": "제주 영어교육도시", "curricula": ["igcse", "ibdp"], "note": "IGCSE(Year 10~11) 후 IB DP(Year 12~13)"},
    {"name": "브랭섬홀 아시아 (BHA)", "name_en": "Branksome Hall Asia", "country": "대한민국", "city": "제주 영어교육도시", "curricula": ["ibdp"], "note": "IB 학교(IB 디렉토리 확인)"},
    {"name": "한국국제학교 제주 (KIS Jeju)", "name_en": "Korea International School Jeju", "country": "대한민국", "city": "제주 영어교육도시", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "세인트존스베리 아카데미 제주 (SJA Jeju)", "name_en": "St. Johnsbury Academy Jeju", "country": "대한민국", "city": "제주 영어교육도시", "curricula": [], "note": "미국식 커리큘럼"},
    # 대전·대구·부산·세종·광주·울산·경남
    {"name": "대전외국인학교 (TCIS)", "name_en": "Taejon Christian International School", "country": "대한민국", "city": "대전", "curricula": ["ibdp"], "note": "PYP·MYP·DP 전 과정 IB(학교 공식 안내)"},
    {"name": "대구국제학교 (DIS)", "name_en": "Daegu International School", "country": "대한민국", "city": "대구", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "부산외국인학교 (BFS)", "name_en": "Busan Foreign School", "country": "대한민국", "city": "부산", "curricula": ["ap"], "note": "미국식 커리큘럼"},
    {"name": "부산국제외국인학교 (BIFS)", "name_en": "Busan International Foreign School", "country": "대한민국", "city": "부산", "curricula": ["ibdp"], "note": "IB 학교"},
    {"name": "부산국제고등학교", "name_en": "Busan International High School", "country": "대한민국", "city": "부산", "curricula": [], "note": "공립 국제고"},
    {"name": "세종국제고등학교", "name_en": "Sejong International High School", "country": "대한민국", "city": "세종", "curricula": [], "note": "공립 국제고"},
    {"name": "광주국제외국인학교 (GIS)", "name_en": "Gwangju International School", "country": "대한민국", "city": "광주", "curricula": [], "note": "미국식 커리큘럼, Pre-K~12(학교 공식 안내)"},
    {"name": "현대외국인학교 (HFS)", "name_en": "Hyundai Foreign School", "country": "대한민국", "city": "울산", "curricula": [], "note": ""},
    {"name": "경남국제외국인학교 (GIFS)", "name_en": "Gyeongnam International Foreign School", "country": "대한민국", "city": "경남 사천", "curricula": [], "note": ""},
]
