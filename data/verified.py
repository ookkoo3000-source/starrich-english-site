# -*- coding: utf-8 -*-
"""공식 출처로 확인된 학교 사실 (기존 intl 저널의 '정보 출처' 박스에서 추출, _journal_sources.json).
MAP: 저널 slug → (name_en 부분 문자열, 국가). 빌드 때 디렉토리 학교와 매칭해 출처 박스를 붙인다.
"""
import json, os

MAP = {
    "aes-delhi-admission": ("American Embassy School", "인도"),
    "ais-singapore-admission": ("Australian International School", "싱가포르"),
    "alice-smith-kl-admission": ("Alice Smith", "말레이시아"),
    "american-school-dubai-admission": ("American School of Dubai", "아랍에미리트"),
    "aoba-tokyo-admission": ("Aoba", "일본"),
    "apis-admission-eligibility": ("Asia Pacific International School", "대한민국"),
    "apis-foreign-language-requirement": ("Asia Pacific International School", "대한민국"),
    "asb-bangkok-admission": ("American School of Bangkok", "태국"),
    "asb-mumbai-admission": ("American School of Bombay", "인도"),
    "asd-doha-admission": ("American School of Doha", "카타르"),
    "asij-tokyo-admission": ("American School in Japan", "일본"),
    "bangkok-patana-admission": ("Bangkok Patana School", "태국"),
    "bfs-admission-priority": ("Busan Foreign School", "대한민국"),
    "bha-ib-math-aa-ai": ("Branksome Hall Asia", "대한민국"),
    "bis-hanoi-admission": ("British International School Hanoi", "베트남"),
    "bis-hcmc-admission": ("British International School Ho Chi Minh", "베트남"),
    "brent-manila-admission": ("Brent International School Manila", "필리핀"),
    "british-school-manila-admission": ("British School Manila", "필리핀"),
    "bsj-jakarta-admission": ("British School Jakarta", "인도네시아"),
    "bst-tokyo-admission": ("British School in Tokyo", "일본"),
    "cairo-american-college-admission": ("Cairo American College", "이집트"),
    "cdnis-hongkong-admission": ("Canadian International School of Hong Kong", "홍콩"),
    "chadwick-admission-prep": ("Chadwick International", "대한민국"),
    "cis-hongkong-admission": ("Chinese International School", "홍콩"),
    "concordia-shanghai-admission": ("Concordia International School Shanghai", "중국"),
    "dis-daegu-admission": ("Daegu International School", "대한민국"),
    "dssi-abitur-english": ("Deutsche Schule Seoul", "대한민국"),
    "dubai-american-academy-admission": ("Dubai American Academy", "아랍에미리트"),
    "dubai-college-admission": ("Dubai College", "아랍에미리트"),
    "dulwich-beijing-admission": ("Dulwich College Beijing", "중국"),
    "dulwich-seoul-eal-english": ("Dulwich College Seoul", "대한민국"),
    "dulwich-shanghai-puxi-admission": ("Dulwich College Shanghai Puxi", "중국"),
    "dulwich-singapore-admission": ("Dulwich College (Singapore)", "싱가포르"),
    "dwight-seoul-admission": ("Dwight School Seoul", "대한민국"),
    "dwight-seoul-ib-continuum": ("Dwight School Seoul", "대한민국"),
    "esf-hongkong-admission": ("English Schools Foundation", "홍콩"),
    "fis-hongkong-admission": ("French International School", "홍콩"),
    "gems-dubai-admission": ("GEMS World Academy", "아랍에미리트"),
    "germanswiss-hongkong-admission": ("German Swiss International School", "홍콩"),
    "giis-singapore-admission": ("Global Indian International School", "싱가포르"),
    "gis-admission-rd-zone": ("Gwangju International School", "대한민국"),
    "gsis-admission-test": ("Gyeonggi Suwon International School", "대한민국"),
    "harrow-bangkok-admission": ("Harrow International School Bangkok", "태국"),
    "harrow-beijing-admission": ("Harrow Beijing", "중국"),
    "harrow-hongkong-admission": ("Harrow International School Hong Kong", "홍콩"),
    "hkis-admission-waitpool": ("Hong Kong International School", "홍콩"),
    "isb-beijing-admission": ("International School of Beijing", "중국"),
    "ishcmc-admission": ("International School Ho Chi Minh City", "베트남"),
    "iskl-kualalumpur-admission": ("International School of Kuala Lumpur", "말레이시아"),
    "ism-manila-eligibility": ("International School Manila", "필리핀"),
    "jis-jakarta-admission": ("Jakarta Intercultural School", "인도네시아"),
    "kellett-hongkong-admission": ("Kellett School", "홍콩"),
    "keystone-beijing-admission": ("Keystone Academy", "중국"),
    "kis-international-bangkok-admission": ("KIS International School", "태국"),
    "kis-jeju-admission": ("Korea International School Jeju", "대한민국"),
    "kis-pangyo-admission": ("Korea International School Pangyo", "대한민국"),
    "kis-seoul-elementary-admission": ("Korea International School Seoul", "대한민국"),
    "kkfs-admission-checklist": ("Korea Kent Foreign School", "대한민국"),
    "lfs-sia-english-track": ("Lycée Français de Séoul", "대한민국"),
    "mahindra-uwc-admission": ("UWC Mahindra", "인도"),
    "nais-pudong-admission": ("Nord Anglia International School Shanghai", "중국"),
    "nas-dubai-admission": ("Nord Anglia International School Dubai", "아랍에미리트"),
    "nishimachi-tokyo-admission": ("Nishimachi", "일본"),
    "nist-bangkok-admission": ("NIST", "태국"),
    "nlcs-jeju-admission-steps": ("North London Collegiate School Jeju", "대한민국"),
    "nlcs-jeju-alevel-math": ("North London Collegiate School Jeju", "대한민국"),
    "ofs-singapore-admission": ("Overseas Family School", "싱가포르"),
    "owis-riyadh-admission": ("One World International School", "사우디아라비아"),
    "reedley-manila-admission": ("Reedley", "필리핀"),
    "regents-bangkok-admission": ("Regents International School Bangkok", "태국"),
    "renaissance-saigon-admission": ("Renaissance International School Saigon", "베트남"),
    "repton-dubai-admission": ("Repton School Dubai", "아랍에미리트"),
    "ris-bangkok-admission": ("Ruamrudee", "태국"),
    "sas-shanghai-admission": ("Shanghai American School", "중국"),
    "sas-singapore-admission": ("Singapore American School", "싱가포르"),
    "scis-shanghai-admission": ("Shanghai Community International School", "중국"),
    "seisen-tokyo-admission": ("Seisen", "일본"),
    "sfs-two-tracks": ("Seoul Foreign School", "대한민국"),
    "shrewsbury-bangkok-admission": ("Shrewsbury International School Bangkok", "태국"),
    "sis-admission-steps": ("Seoul International School", "대한민국"),
    "sis-ap-course-selection": ("Seoul International School", "대한민국"),
    "stamford-singapore-admission": ("Stamford American", "싱가포르"),
    "tanglin-trust-admission": ("Tanglin Trust", "싱가포르"),
    "tas-taipei-admission": ("Taipei American School", "대만"),
    "tcis-admission-test": ("Taejon Christian International School", "대한민국"),
    "tcis-math-myp-dp": ("Taejon Christian International School", "대한민국"),
    "tes-taipei-admission": ("Taipei European School", "대만"),
    "wab-beijing-admission": ("Western Academy of Beijing", "중국"),
    "woodstock-mussoorie-admission": ("Woodstock School", "인도"),
    "ycis-hongkong-admission": ("Yew Chung International School of Hong Kong", "홍콩"),
    "yiss-admission-waitpool": ("Yongsan International School", "대한민국"),
    "ykpao-shanghai-admission": ("YK Pao", "중국"),
}

# 직접 확인한 추가 사실 (저널 외)
EXTRA = [
    {"match": ("Chadwick International", "대한민국"), "source": "https://www.chadwickinternational.org/", "checked": "2026-11-04",
     "quote": "4 IB Accredited Programs / PRE-KINDERGARTEN - GRADE 5 VILLAGE SCHOOL / GRADES 6 - 8 MIDDLE SCHOOL / GRADES 9 - 12 UPPER SCHOOL"},
    {"match": ("Korea International School Pangyo", "대한민국"), "source": "https://www.kis.or.kr/", "checked": "2026-11-04",
     "quote": "A trusted international PK-12 curriculum. / AP courses: 26 / Our learning spaces purposefully accommodate elementary, middle, and high school needs."},
    {"match": ("Seoul Foreign School", "대한민국"), "source": "https://www.seoulforeign.org/", "checked": "2026-11-04",
     "quote": "offering the International Baccalaureate Diploma Programme, making our High School the most experienced IB school in Korea / the English National Curriculum"},
    {"match": ("Shanghai American School", "중국"), "source": "https://www.saschina.org/", "checked": "2026-11-04",
     "quote": "Since we offer both AP and IB, our students have the opportunity to dive deep into advanced subjects"},
    {"match": ("Concordia International School Shanghai", "중국"), "source": "https://www.concordiashanghai.org/", "checked": "2026-11-04",
     "quote": "offers a comprehensive American-style education to students from Preschool through High School. (High School 메뉴에 Advanced Placement 항목)"},
    {"match": ("Hong Kong International School", "홍콩"), "source": "https://www.hkis.edu.hk/", "checked": "2026-11-04",
     "quote": "An American-style education grounded in the Christian faith and respecting the spiritual lives of all"},
    {"match": ("Canadian International School of Hong Kong", "홍콩"), "source": "https://www.cdnis.edu.hk/", "checked": "2026-11-04",
     "quote": "Learn about our through-train IB education with distinct pathways that open doors worldwide. / Ontario Secondary School Diploma / DUAL DIPLOMA EXCELLENCE"},
    {"match": ("Taipei American School", "대만"), "source": "https://www.tas.edu.tw/", "checked": "2026-11-04",
     "quote": "offering both the IB Diploma and AP Courses. / from PreK to Grade 12 / Upper School: Grade 9 - 12"},
    {"match": ("Taipei European School", "대만"), "source": "https://www.tes.tp.edu.tw/", "checked": "2026-11-04",
     "quote": "IB Diploma Programme (IB DP) & IB Careers-related Programme (IB CP) - TES High School / BRITISH SECONDARY AND HIGH SCHOOL SECTION"},
    {"match": ("American School in Japan", "일본"), "source": "https://www.asij.ac.jp/", "checked": "2026-11-04",
     "quote": "The school's curriculum is modeled on the American system of education / including Advanced Placement (AP) courses / 9th Grade - 12th Grade"},
    {"match": ("British School in Tokyo", "일본"), "source": "https://www.bst.ac.jp/", "checked": "2026-11-04",
     "quote": "based on the National Curriculum for England / aged 3 to 18 years old / examination success a significant element in Years 10-13 / Year 12 - 13"},
    {"match": ("Yongsan International School", "대한민국"), "source": "https://www.yisseoul.org/", "checked": "2026-11-04",
     "quote": "Our accredited K-12 instructional program is academically rigorous"},
]


def load():
    """return list of {match:(en, country), source, quote, checked}"""
    path = os.path.join(os.path.dirname(__file__), "_journal_sources.json")
    out = list(EXTRA)
    if os.path.exists(path):
        for o in json.load(open(path, encoding="utf-8")):
            slug = o["file"][len("journal-"):-len(".html")]
            if slug not in MAP:
                continue
            src = o["src"]
            # "학교 공식 홈페이지 — "..."" 형태에서 따옴표 안만
            q = src.split("—", 1)[1].strip() if "—" in src else src
            q = q.strip().strip('"').strip("“”").strip()
            out.append({"match": MAP[slug], "source": (o["links"] or [""])[0], "quote": q, "checked": o["checked"]})
    return out


import re as _re
_STOP = {"international", "school", "of", "the", "in"}
def _norm(x):
    return _re.sub(r"[^a-z0-9]+", "", x.lower())
def _words(x):
    return set(w for w in _re.findall(r"[a-z0-9]+", x.lower()) if w not in _STOP)
_CACHE = None
def find(name_en, country):
    """엄격 매칭: 정규화 이름이 같거나, 매칭 문자열로 시작(앞에 the/gems만 허용)하거나, 의미 단어 집합이 같을 때만"""
    global _CACHE
    if _CACHE is None:
        _CACHE = load()
    n = _norm(name_en); nw = _words(name_en)
    out = []
    for v in _CACHE:
        m, c = v["match"]
        if c != country:
            continue
        nm = _norm(m)
        if n == nm or n.startswith(nm) or n.startswith("the" + nm) or n.startswith("gems" + nm) or (_words(m) and _words(m) == nw):
            out.append(v)
    return out
