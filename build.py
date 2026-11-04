# -*- coding: utf-8 -*-
"""국제학교 학교별 1:1 화상과외 사이트 생성기 (가칭 인터튜터)
python build.py  →  index.html, schools.html, regions.html, region/<country>.html, city/<slug>.html, school/<slug>.html, sitemap.xml
데이터: data/dir_*.py (학교 디렉토리), data/verified.py (공식 출처 확인분), data/subjects.py
규칙: 학교명·소재지는 공개 정보. 교육과정은 확신 있는 것만 표기, 없으면 '확인 전'으로 두고 단정하지 않는다.
      선생님 수·후기·합격 실적·가격 등 미확인 수치 금지. 입학 준비는 공식 전형 기준 상담만, 합격 보장·내부 자료·제휴 표현 금지.
"""
import os, sys, re, html, glob, datetime, importlib
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "data"))
from subjects import SUBJECTS, CURRICULA
import verified

BRAND = "인터튜터"            # 가칭
DOMAIN = "https://starrichenglish.co.kr"
PHONE_DISPLAY = "010-3131-5305"
PHONE_TEL = "01031315305"
KAKAO = "https://open.kakao.com/o/sX9no5Ki"
LEAD_EMAIL = "ookkoo12@naver.com"
TODAY = datetime.date.today().isoformat()
GRADES = ["초등(G1~5)", "G6", "G7", "G8", "G9 / Year 10", "G10 / Year 11", "G11 / Year 12", "G12 / Year 13", "입학 준비 중"]

COUNTRY_SLUG = {
    "대한민국": "korea", "중국": "china", "홍콩": "hongkong", "마카오": "macau", "대만": "taiwan", "일본": "japan", "몽골": "mongolia",
    "싱가포르": "singapore", "말레이시아": "malaysia", "태국": "thailand", "베트남": "vietnam", "인도네시아": "indonesia", "필리핀": "philippines",
    "캄보디아": "cambodia", "미얀마": "myanmar", "라오스": "laos", "브루나이": "brunei",
    "인도": "india", "스리랑카": "srilanka", "방글라데시": "bangladesh", "파키스탄": "pakistan", "카자흐스탄": "kazakhstan", "우즈베키스탄": "uzbekistan",
    "아랍에미리트": "uae", "카타르": "qatar", "사우디아라비아": "saudi-arabia", "쿠웨이트": "kuwait", "바레인": "bahrain", "오만": "oman",
    "튀르키예": "turkiye", "터키": "turkiye", "이집트": "egypt", "케냐": "kenya", "남아프리카공화국": "south-africa", "나이지리아": "nigeria",
    "영국": "uk", "독일": "germany", "프랑스": "france", "네덜란드": "netherlands", "벨기에": "belgium", "스위스": "switzerland", "스페인": "spain",
    "이탈리아": "italy", "오스트리아": "austria", "체코": "czechia", "폴란드": "poland", "헝가리": "hungary", "스웨덴": "sweden", "덴마크": "denmark",
    "핀란드": "finland", "노르웨이": "norway", "아일랜드": "ireland", "포르투갈": "portugal", "그리스": "greece",
    "호주": "australia", "뉴질랜드": "new-zealand", "캐나다": "canada", "미국": "usa", "멕시코": "mexico", "브라질": "brazil", "아르헨티나": "argentina", "칠레": "chile",
}
GROUPS = [
    ("국내", ["대한민국"]),
    ("동북아시아", ["중국", "홍콩", "마카오", "대만", "일본", "몽골"]),
    ("동남아시아", ["싱가포르", "말레이시아", "태국", "베트남", "인도네시아", "필리핀", "캄보디아", "미얀마", "라오스", "브루나이"]),
    ("남아시아·중앙아시아", ["인도", "스리랑카", "방글라데시", "파키스탄", "카자흐스탄", "우즈베키스탄"]),
    ("중동·아프리카", ["아랍에미리트", "카타르", "사우디아라비아", "쿠웨이트", "바레인", "오만", "튀르키예", "터키", "이집트", "케냐", "남아프리카공화국", "나이지리아"]),
    ("유럽", ["영국", "독일", "프랑스", "네덜란드", "벨기에", "스위스", "스페인", "이탈리아", "오스트리아", "체코", "폴란드", "헝가리", "스웨덴", "덴마크", "핀란드", "노르웨이", "아일랜드", "포르투갈", "그리스"]),
    ("미주·오세아니아", ["미국", "캐나다", "멕시코", "브라질", "아르헨티나", "칠레", "호주", "뉴질랜드"]),
]


def esc(s):
    return html.escape(str(s), quote=True)


def ascii_slug(s):
    s = s.lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "x"


# ---------------- data ----------------
def load_schools():
    rows = []
    for f in sorted(glob.glob(os.path.join(ROOT, "data", "dir_*.py"))):
        mod = importlib.import_module(os.path.basename(f)[:-3])
        rows.extend(mod.SCHOOLS)
    seen = {}
    for s in rows:
        s["curricula"] = [c for c in s.get("curricula", []) if c in CURRICULA]
        s["note"] = s.get("note", "") or ""
        base = ascii_slug(s["name_en"])
        slug = base
        n = 2
        while slug in seen:
            slug = f"{base}-{n}"; n += 1
        seen[slug] = True
        s["slug"] = slug
        s["cslug"] = COUNTRY_SLUG.get(s["country"])
        if not s["cslug"]:
            print("!! 국가 슬러그 없음:", s["country"], "→ build.py COUNTRY_SLUG에 추가 필요")
            s["cslug"] = "country-" + ascii_slug(s["country"]) if ascii_slug(s["country"]) != "x" else "country-etc"
        s["sources"] = verified.find(s["name_en"], s["country"])
        s["verified"] = bool(s["sources"])
    return rows


def city_slug(country_slug, city, cities_in_country):
    # 도시 영문 슬러그: 영문 매핑이 없으므로 국가슬러그-순번 + 학교 영문명에서 도시 추정 안 함 → 안정적인 순번 방식
    idx = cities_in_country.index(city) + 1
    return f"{country_slug}-{idx}"



# ---------------- images (Wikimedia Commons, CC) ----------------
import json as _json
_IMG_PATH = os.path.join(ROOT, "data", "images.json")
IMAGES = _json.load(open(_IMG_PATH, encoding="utf-8")) if os.path.exists(_IMG_PATH) else {}

def school_image(s):
    v = IMAGES.get(s["slug"]) if s else None
    return v if (v and os.path.exists(os.path.join(ROOT, v["file"]))) else None

def figure_html(s, rel, style=""):
    v = school_image(s)
    if not v:
        return ""
    lic = f'<a href="{esc(v["license_url"])}" target="_blank" rel="noopener license">{esc(v["license"])}</a>' if v.get("license_url") else esc(v["license"])
    artist = esc(v["artist"]) if v.get("artist") else "작자 미상"
    return f"""<figure class="school-photo" style="{style}">
  <img src="{rel}{v['file']}" alt="{esc(s['name'])} ({esc(s['name_en'])})" loading="lazy">
  <figcaption>사진 출처: <a href="{esc(v['page'])}" target="_blank" rel="noopener">Wikimedia Commons</a> · {artist} · {lic}</figcaption>
</figure>"""

def og_image_url(s):
    v = school_image(s) if s else None
    return f"{DOMAIN}/{v['file']}" if v else None

# ---------------- html pieces ----------------
def head(title, desc, path, rel, og=None):
    canonical = f"{DOMAIN}/{path}" if path else f"{DOMAIN}/"
    og = og or f"{DOMAIN}/img/og-default.jpg"
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="naver-site-verification" content="045ffaffc914b769fd4ab255c91a6f027f11fb38" />
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{og}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@600;700;900&display=swap">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<link rel="stylesheet" href="{rel}css/style.css">
</head>
<body>"""


def header(rel):
    return f"""
<header class="top"><div class="wrap">
  <a class="logo" href="{rel}index.html">{BRAND}<span>.</span></a>
  <nav class="nav" id="nav">
    <a href="{rel}schools.html">학교 찾기</a>
    <a href="{rel}regions.html">국가·도시별</a>
    <a href="{rel}column.html">칼럼</a>
    <a href="{rel}index.html#subjects">과목·교육과정</a>
    <a href="{rel}index.html#how">진행 절차</a>
    <a href="{rel}index.html#faq">자주 묻는 질문</a>
  </nav>
  <div class="top-cta">
    <a class="btn kakao" href="{KAKAO}" target="_blank" rel="noopener">카톡 상담</a>
    <a class="btn btn-d" href="{rel}index.html#contact">무료 상담 신청</a>
  </div>
  <button class="ham" aria-label="메뉴" onclick="document.getElementById('nav').classList.toggle('open')">☰</button>
</div></header>"""


def footer(rel, countries):
    region_links = "".join(f'<a href="{rel}region/{cs}.html">{c} 국제학교 과외</a>' for c, cs in countries[:12])
    subj_links = "".join(f'<a href="{rel}index.html#subjects">국제학교 {x["name"]} 과외</a>' for x in SUBJECTS)
    return f"""
<footer><div class="wrap">
  <div class="cols">
    <div>
      <h4>{BRAND}</h4>
      <p>국제학교·외국인학교 재학생과 입학 준비 학생을 위한 1:1 화상과외 상담 안내. IB·AP·IGCSE·A-Level 등 교육과정에 맞춰 수학·영어·과학을 지도합니다. 상담 신청은 무료이며, 수업료는 학년·과목·횟수에 따라 상담 때 안내합니다.</p>
      <p>상담 전화 <a href="tel:{PHONE_TEL}" style="display:inline;color:#fff;font-weight:700">{PHONE_DISPLAY}</a> · <a href="{KAKAO}" target="_blank" rel="noopener" style="display:inline;color:#fff;font-weight:700">카카오톡 오픈채팅</a></p>
    </div>
    <div><h4>국가별 안내</h4>{region_links}<a href="{rel}regions.html">전체 국가·도시 →</a></div>
    <div><h4>과목별 과외</h4>{subj_links}<a href="{rel}schools.html">전체 학교 목록 →</a></div>
  </div>
  <div class="copy">© {datetime.date.today().year} {BRAND}. 학교명·소재지는 공개 정보 기준이며, 교육과정·입학 전형은 각 학교 공식 홈페이지에서 확인한 내용만 출처·확인일과 함께 표기합니다. 학교와의 제휴·협약은 없습니다.</div>
</div></footer>
<div class="m-bar">
  <a class="btn kakao" href="{KAKAO}" target="_blank" rel="noopener">카톡 상담</a>
  <a class="btn btn-d" href="{rel}index.html#contact">무료 상담 신청</a>
</div>
<script>
document.querySelectorAll('.tabs button').forEach(function(b){{
  b.addEventListener('click',function(){{
    var k=b.dataset.k;
    document.querySelectorAll('.tabs button').forEach(function(x){{x.classList.toggle('on',x===b)}});
    document.querySelectorAll('.panel').forEach(function(p){{p.classList.toggle('on',p.dataset.k===k)}});
  }});
}});
(function(){{
  var box=document.getElementById('q'); var list=document.getElementById('school-list'); if(!box||!list) return;
  var items=Array.prototype.slice.call(list.querySelectorAll('[data-s]'));
  var heads=Array.prototype.slice.call(list.querySelectorAll('[data-h]'));
  function run(){{
    var q=box.value.trim().toLowerCase(); var n=0;
    items.forEach(function(el){{var ok=!q||el.dataset.s.indexOf(q)>=0; el.style.display=ok?'':'none'; if(ok)n++;}});
    heads.forEach(function(h){{var any=false; var el=h.nextElementSibling; while(el&&!el.hasAttribute('data-h')){{if(el.hasAttribute('data-s')&&el.style.display!=='none')any=true; el=el.nextElementSibling;}} h.style.display=any?'':'none';}});
    var c=document.getElementById('q-count'); if(c) c.textContent=n+'곳';
  }}
  box.addEventListener('input',run);
  var m=location.hash.match(/q=([^&]+)/); if(m){{box.value=decodeURIComponent(m[1]); }} run();
}})();
</script>
</body></html>"""


def contact_form(rel, default_school=""):
    grade_opts = "".join(f"<option>{g}</option>" for g in GRADES)
    subj_opts = "".join(f"<option>{x['name']}</option>" for x in SUBJECTS) + "<option>기타 (메모에 적어 주세요)</option>"
    curr_opts = "".join(f"<option>{c['name']}</option>" for c in CURRICULA.values()) + "<option>모름 / 상담 때 확인</option>"
    return f"""
<section class="form-sec" id="contact"><div class="wrap">
  <div>
    <span class="eyebrow">무료 상담</span>
    <h2>학교·학년·과목만 알려주세요</h2>
    <p class="lead">접수 내용을 보고 교육과정·과목이 맞는 선생님을 찾아 연락드립니다. 상담은 무료이고, 수업료는 학년·과목·횟수에 따라 상담 때 안내합니다. 해외 거주 학생은 현지 시간대를 적어 주시면 시차를 맞춰 연락합니다.</p>
    <a class="phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
    <p><a class="btn kakao" href="{KAKAO}" target="_blank" rel="noopener">카카오톡 오픈채팅으로 문의</a></p>
  </div>
  <form class="form" action="https://formsubmit.co/{LEAD_EMAIL}" method="POST">
    <input type="hidden" name="_subject" value="[{BRAND}] 상담 신청{(' - ' + default_school) if default_school else ''}">
    <input type="hidden" name="_captcha" value="false">
    <input type="hidden" name="_template" value="table">
    <input type="hidden" name="_next" value="{DOMAIN}/{rel}index.html#contact">
    <input type="text" name="_honey" style="display:none">
    <div class="row">
      <div><label class="req">학부모/학생 이름</label><input name="이름" required></div>
      <div><label class="req">연락처 (전화 또는 카톡 ID)</label><input name="연락처" required placeholder="010-0000-0000 / 카톡 ID"></div>
    </div>
    <div class="row">
      <div><label class="req">학교</label><input name="학교" required value="{esc(default_school)}" placeholder="학교 이름 (입학 준비 중이면 희망 학교)"></div>
      <div><label class="req">학년</label><select name="학년" required><option value="">선택</option>{grade_opts}</select></div>
    </div>
    <div class="row">
      <div><label class="req">과목</label><select name="과목" required><option value="">선택</option>{subj_opts}</select></div>
      <div><label>교육과정</label><select name="교육과정"><option value="">선택</option>{curr_opts}</select></div>
    </div>
    <div class="row">
      <div><label>거주 지역 (국내 시·구 / 해외 도시)</label><input name="거주지" placeholder="예: 인천 송도 / 싱가포르"></div>
      <div><label>희망 수업 시간대</label><input name="시간대" placeholder="예: 평일 저녁 8시 이후 (현지 시간)"></div>
    </div>
    <label>남기실 말씀</label><textarea name="메모" placeholder="현재 코스(예: IB Math AA HL), 목표, 고민 등"></textarea>
    <button class="btn btn-p" type="submit">무료 상담 신청하기</button>
    <small>남겨주신 정보는 상담 연락 외의 목적으로 쓰지 않습니다.</small>
  </form>
</div></section>"""


def curr_text(s):
    return " · ".join(CURRICULA[c]["name"] for c in s["curricula"]) if s["curricula"] else "교육과정 확인 전"


def school_card(s, rel):
    badge = f'<span class="badge curr">{curr_text(s)}</span>' if s["curricula"] else '<span class="badge">교육과정 상담 때 확인</span>'
    v = ' <span class="badge region">공식 출처 확인</span>' if s["verified"] else ""
    v_img = school_image(s)
    thumb = f'<img class="card-thumb" src="{rel}{v_img["file"]}" alt="" loading="lazy">' if v_img else ""
    return f"""<a class="card school-card{' has-thumb' if v_img else ''}" href="{rel}school/{s['slug']}.html">
  {thumb}{badge}<span class="badge region">{s['city']}</span>{v}
  <h3 style="margin-top:10px">{s['name']} 과외</h3>
  <p>{s['name_en']}{(' · ' + s['note']) if s['note'] else ''}<br>수학·영어·과학 1:1 화상과외 안내 →</p>
</a>"""


def steps_html(school=None):
    nm = school["name"] if school else "학교"
    return f"""<div class="steps">
    <div class="step"><h3>상담 신청</h3><p>학교·학년·과목·현재 코스를 남겨 주세요.</p></div>
    <div class="step"><h3>선생님 안내</h3><p>교육과정과 과목이 맞는 선생님을 찾아 프로필을 안내합니다.</p></div>
    <div class="step"><h3>첫 수업</h3><p>학교 자료(syllabus·과제·시험지)를 보고 계획을 정합니다.</p></div>
    <div class="step"><h3>정기 수업</h3><p>{nm} 평가 일정(IA·시험·과제)에 맞춰 조정합니다.</p></div>
    <div class="step"><h3>점검</h3><p>성적표·피드백을 보고 다음 계획을 다시 잡습니다.</p></div>
  </div>"""


# ---------------- pages ----------------
def build_index(schools, countries, by_country, posts=()):
    n_cities = len({(s["country"], s["city"]) for s in schools})
    kr = by_country.get("대한민국", [])
    kr_cities = []
    for s in kr:
        if s["city"] not in kr_cities:
            kr_cities.append(s["city"])
    kr_items = "".join(f'<a href="region/korea.html#{ascii_slug(str(i))}">{c}<span>학교 {sum(1 for s in kr if s["city"]==c)}곳</span></a>' for i, c in enumerate(kr_cities))
    ov_items = "".join(f'<a href="region/{cs}.html">{c}<span>학교 {len(by_country[c])}곳</span></a>' for c, cs in countries if c != "대한민국")
    featured = [s for s in schools if s["verified"] and s["curricula"]][:6]
    feat_cards = "".join(school_card(s, "") for s in featured)
    subj_cards = "".join(f'<a class="card subj" href="#contact"><i>{esc(x["icon"])}</i><div><h3 style="margin:0;font-size:16px">{x["name"]}</h3><p style="font-size:13px">{x["desc"]}</p></div></a>' for x in SUBJECTS)
    curr_cards = "".join(f'<div class="card"><h3>{c["name"]}</h3><p>{c["full"]}</p></div>' for c in CURRICULA.values())
    body = head(f"{BRAND} | 국제학교 학교별 1:1 화상과외 (IB·AP·IGCSE·A-Level)",
                f"국내·해외 국제학교 {len(schools)}곳 학교별 1:1 화상과외 상담. 학교 이름으로 찾고 IB·AP·IGCSE·A-Level 교육과정과 과목으로 고르는 수학·영어·과학 과외, 상담 신청은 무료입니다.", "", "")
    body += header("")
    body += f"""
<section class="hero"><div class="wrap">
  <div>
    <div class="tag">국제학교 · 외국인학교 학교별 1:1 화상과외</div>
    <h1>우리 아이 학교의 교육과정에<br>맞춘 1:1 화상과외</h1>
    <p>같은 수학이어도 IB·AP·IGCSE는 평가 방식이 다릅니다. 학교를 먼저 고르면 그 학교의 교육과정 기준으로 과목과 수업 방향을 안내합니다. 국내·해외 어디서든 화상으로 진행합니다.</p>
    <div class="cta">
      <a class="btn btn-p" href="schools.html">우리 학교 찾기 →</a>
      <a class="btn btn-o" href="#contact">무료 상담 신청</a>
    </div>
  </div>
  <div>
    <div class="pill">IB DP</div><div class="pill">IGCSE</div><div class="pill">AP</div><div class="pill">A-Level</div>
    <div class="stats" style="margin-top:14px">
      <div class="stat"><b>{len(schools):,}</b><span>안내 학교</span></div>
      <div class="stat"><b>{len(countries)}</b><span>국가</span></div>
      <div class="stat"><b>{n_cities}</b><span>도시</span></div>
      <div class="stat"><b>1:1</b><span>화상 수업</span></div>
    </div>
  </div>
</div></section>

<div class="wrap"><div class="finder">
  <form action="schools.html" method="get" onsubmit="location.href='schools.html#q='+encodeURIComponent(this.q.value);return false;">
    <input name="q" placeholder="학교 이름으로 찾기 (예: 채드윅, Dulwich, 싱가포르)" required style="grid-column:span 3">
    <button class="btn btn-d" type="submit">학교 찾기</button>
  </form>
</div></div>

<section id="schools"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">학교별 과외</span><h2>국내 국제학교·외국인학교·국제고</h2><p>지역을 누르면 학교 목록이 나옵니다. 목록에 없는 학교도 상담 접수는 가능합니다.</p></div>
  <div class="region-list">{kr_items}</div>
  <div class="sec-head" style="margin-top:36px"><h2 style="font-size:22px">해외 국제학교</h2><p>한인 가정이 많은 도시의 국제학교를 국가별로 정리했습니다.</p></div>
  <div class="region-list">{ov_items}</div>
  <p style="margin-top:16px"><a class="btn btn-d" href="schools.html">전체 학교 {len(schools):,}곳 보기</a> <a class="btn btn-o" style="border-color:var(--navy);color:var(--navy)" href="regions.html">국가·도시별 보기</a></p>
</div></section>

<section style="background:#fff"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">공식 출처 확인 학교</span><h2>공식 출처를 함께 적은 학교</h2><p>학교 공식 홈페이지에서 확인한 내용(교육과정·입학 전형 등)을 출처와 확인일과 함께 적은 페이지입니다. 차례로 늘려 갑니다.</p></div>
  <div class="grid g3">{feat_cards}</div>
</div></section>

<section id="subjects"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">과목 · 교육과정</span><h2>과목은 넷, 기준은 교육과정</h2><p>학교 페이지에서 과목을 누르면 그 학교 교육과정 기준 수업 포인트가 나옵니다.</p></div>
  <div class="grid g4">{subj_cards}</div>
  <div class="grid g4" style="margin-top:16px">{curr_cards}</div>
</div></section>

<section id="how" style="background:#fff"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">진행 절차</span><h2>수업은 이렇게 시작됩니다</h2></div>
  {steps_html()}
</div></section>

<section id="column"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">칼럼</span><h2>최근 칼럼</h2><p>학교별 교육과정·과목 공부법을 학교 공식 출처와 함께 정리합니다. 매일 새 글이 올라옵니다.</p></div>
  <div class="grid g3">{"".join(post_card(p, "") for p in posts[:6])}</div>
  <p style="margin-top:14px"><a class="btn btn-d" href="column.html">칼럼 전체 보기</a></p>
</div></section>

<section id="faq" style="background:#fff"><div class="wrap faq">
  <div class="sec-head"><span class="eyebrow">FAQ</span><h2>자주 묻는 질문</h2></div>
  <details open><summary>상담 신청에 비용이 드나요?</summary><p>상담 신청은 무료입니다. 수업료는 학년·과목·교육과정·주당 횟수에 따라 다르므로 상담 때 안내합니다.</p></details>
  <details><summary>목록에 우리 학교가 없는데 신청할 수 있나요?</summary><p>네. 상담 접수는 국내·해외 어느 학교든 가능합니다. 폼에 학교 이름과 교육과정을 적어 주세요.</p></details>
  <details><summary>해외에 살고 있어도 되나요?</summary><p>네. 화상 수업이라 지역 제한이 없습니다. 거주 도시와 가능한 시간대(현지 시간)를 적어 주시면 시차를 맞춰 안내합니다.</p></details>
  <details><summary>"교육과정 확인 전"은 무슨 뜻인가요?</summary><p>학교 공식 홈페이지에서 아직 교육과정을 확인하지 않아 단정하지 않은 상태입니다. 상담 때 학생이 실제 듣는 코스를 기준으로 안내합니다.</p></details>
  <details><summary>입학시험 기출문제가 있나요?</summary><p>학교 내부 시험지나 기출은 보유하지 않으며, 학교와 제휴도 없습니다. 각 학교 공식 입학 안내에 적힌 전형을 기준으로 준비 방향을 상담합니다.</p></details>
</div></section>
"""
    body += contact_form("")
    body += footer("", countries)
    write("index.html", body)


def build_schools_index(schools, countries, by_country):
    rel = ""
    blocks = ""
    for c, cs in countries:
        rows = by_country[c]
        blocks += f'<h2 data-h style="font-size:20px;margin:28px 0 10px"><a href="region/{cs}.html">{c}</a> <span style="color:var(--mute);font-weight:500;font-size:14px">{len(rows)}곳</span></h2>'
        for s in rows:
            key = f"{s['name']} {s['name_en']} {s['city']} {s['country']}".lower()
            blocks += f'<a data-s="{esc(key)}" class="card school-card" style="padding:12px 16px;margin-bottom:8px" href="school/{s["slug"]}.html"><b>{s["name"]}</b> <span style="color:var(--mute);font-size:13px">{s["name_en"]} · {s["city"]} · {curr_text(s)}</span></a>'
    body = head(f"전체 학교 목록 {len(schools)}곳 | {BRAND}", f"국내·해외 국제학교 {len(schools)}곳 학교별 1:1 화상과외 안내 페이지 목록. 학교 이름으로 검색하세요.", "schools.html", rel)
    body += header(rel)
    body += f"""
<section class="page-hero"><div class="wrap">
  <div class="crumb"><a href="index.html">홈</a> › 학교 찾기</div>
  <h1>전체 학교 목록</h1>
  <p>국내·해외 국제학교 {len(schools):,}곳. 학교 이름(한글·영문)이나 도시로 검색하세요.</p>
  <input id="q" placeholder="예: 채드윅 / Dulwich / 싱가포르" style="width:100%;max-width:520px;height:48px;border:0;border-radius:12px;padding:0 16px;font-size:16px;font-family:inherit">
  <p style="margin-top:10px;font-size:14px">표시 <span id="q-count">{len(schools)}곳</span></p>
</div></section>
<section><div class="wrap" id="school-list">{blocks}</div></section>
"""
    body += contact_form(rel)
    body += footer(rel, countries)
    write("schools.html", body)


def build_regions(schools, countries, by_country, city_pages):
    rel = ""
    blocks = ""
    for gname, clist in GROUPS:
        cs_in = [(c, cs) for c, cs in countries if c in clist]
        if not cs_in:
            continue
        blocks += f'<h2 style="font-size:20px;margin:28px 0 12px">{gname}</h2><div class="region-list">'
        for c, cs in cs_in:
            blocks += f'<a href="region/{cs}.html">{c}<span>학교 {len(by_country[c])}곳</span></a>'
        blocks += "</div>"
    other = [(c, cs) for c, cs in countries if not any(c in cl for _, cl in GROUPS)]
    if other:
        blocks += '<h2 style="font-size:20px;margin:28px 0 12px">기타</h2><div class="region-list">' + "".join(f'<a href="region/{cs}.html">{c}<span>학교 {len(by_country[c])}곳</span></a>' for c, cs in other) + "</div>"
    city_blocks = "".join(f'<a href="city/{slug}.html">{city}<span>{country} · {n}곳</span></a>' for (country, city), (slug, n) in city_pages.items())
    body = head(f"국가·도시별 국제학교 화상과외 | {BRAND}", f"{len(countries)}개국 {len(city_pages)}개 도시의 국제학교를 국가·도시별로 정리했습니다. 해외 거주 학생도 화상 1:1 과외로 안내합니다.", "regions.html", rel)
    body += header(rel)
    body += f"""
<section class="page-hero"><div class="wrap">
  <div class="crumb"><a href="index.html">홈</a> › 국가·도시별</div>
  <h1>국가·도시별 국제학교 과외</h1>
  <p>{len(countries)}개국 · {len(city_pages)}개 도시 · 학교 {len(schools):,}곳. 화상 수업이라 어느 도시든 가능합니다.</p>
</div></section>
<section><div class="wrap">{blocks}
  <h2 style="font-size:20px;margin:36px 0 12px">도시별 바로가기</h2><div class="region-list">{city_blocks}</div>
</div></section>
"""
    body += contact_form(rel)
    body += footer(rel, countries)
    write("regions.html", body)


def build_country(country, cslug, rows, countries, city_pages):
    rel = "../"
    cities = []
    for s in rows:
        if s["city"] not in cities:
            cities.append(s["city"])
    sections = ""
    for i, city in enumerate(cities):
        cs = [s for s in rows if s["city"] == city]
        cslug_city = city_pages[(country, city)][0]
        sections += f'<h2 id="{ascii_slug(str(i))}" style="font-size:20px;margin:30px 0 12px"><a href="{rel}city/{cslug_city}.html">{city}</a> <span style="color:var(--mute);font-weight:500;font-size:14px">{len(cs)}곳 · {city} 페이지 →</span></h2><div class="grid g3">' + "".join(school_card(s, rel) for s in cs) + "</div>"
    title = f"{country} 국제학교 과외 | 학교 {len(rows)}곳 1:1 화상과외 {BRAND}"
    desc = f"{country} 국제학교 {len(rows)}곳({', '.join(cities[:5])}{' 등' if len(cities) > 5 else ''}) 학교별 1:1 화상과외 안내. IB·AP·IGCSE 교육과정 기준 수학·영어·과학, 무료 상담."
    body = head(title, desc, f"region/{cslug}.html", rel)
    body += header(rel)
    body += f"""
<section class="page-hero"><div class="wrap">
  <div class="crumb"><a href="{rel}index.html">홈</a> › <a href="{rel}regions.html">국가·도시별</a> › {country}</div>
  <h1>{country} 국제학교 과외</h1>
  <p>{country} 국제학교 {len(rows)}곳 · 도시 {len(cities)}곳. 학교를 고르면 교육과정 기준 과목 안내가 나옵니다. 화상 1:1 수업이라 현지 시간대에 맞춰 진행합니다.</p>
  <div class="facts">{"".join(f'<span><a href="#{ascii_slug(str(i))}">{c}</a></span>' for i, c in enumerate(cities))}</div>
  <div class="cta"><a class="btn btn-p" href="#contact">무료 상담 신청</a> <a class="btn btn-o" href="{KAKAO}" target="_blank" rel="noopener">카톡 상담</a></div>
</div></section>
<section><div class="wrap">{sections}</div></section>
<section style="background:#fff"><div class="wrap faq">
  <div class="sec-head"><span class="eyebrow">FAQ</span><h2>{country} 거주 학생 자주 묻는 질문</h2></div>
  <details open><summary>{country}에 살고 있는데 시차는 어떻게 맞추나요?</summary><p>상담 신청 때 현지 시간 기준 가능한 시간대를 적어 주세요. 그 시간대에 가능한 선생님을 찾아 안내합니다.</p></details>
  <details><summary>목록에 없는 {country} 학교도 되나요?</summary><p>네. 학교 이름과 교육과정(모르면 "모름")을 적어 주시면 학교 공식 안내를 함께 확인해 상담합니다.</p></details>
  <details><summary>한국 교육과정(특례·검정고시)도 함께 볼 수 있나요?</summary><p>상담 때 말씀해 주시면 가능한 범위를 솔직하게 안내합니다. 이 페이지에서는 국제학교 교육과정 과목을 기준으로 안내합니다.</p></details>
</div></section>
"""
    body += contact_form(rel)
    body += footer(rel, countries)
    write(f"region/{cslug}.html", body)


def build_city(country, city, slug, rows, countries, cslug):
    rel = "../"
    cards = "".join(school_card(s, rel) for s in rows)
    title = f"{city} 국제학교 과외 | {city} 국제학교 {len(rows)}곳 1:1 화상과외 {BRAND}"
    desc = f"{city}({country}) 국제학교 {len(rows)}곳 학교별 1:1 화상과외 안내. {', '.join(s['name'] for s in rows[:4])} 등. IB·AP·IGCSE 기준 수학·영어·과학, 현지 시간대 맞춤 화상 수업."
    body = head(title, desc, f"city/{slug}.html", rel)
    body += header(rel)
    body += f"""
<section class="page-hero"><div class="wrap">
  <div class="crumb"><a href="{rel}index.html">홈</a> › <a href="{rel}regions.html">국가·도시별</a> › <a href="{rel}region/{cslug}.html">{country}</a> › {city}</div>
  <h1>{city} 국제학교 과외</h1>
  <p>{city} 국제학교 {len(rows)}곳 학교별 1:1 화상과외 안내. 학교를 고르면 교육과정 기준 과목 안내가 나옵니다.</p>
  <div class="cta"><a class="btn btn-p" href="#contact">무료 상담 신청</a> <a class="btn btn-o" href="{KAKAO}" target="_blank" rel="noopener">카톡 상담</a></div>
</div></section>
<section><div class="wrap"><div class="grid g3">{cards}</div></div></section>
<section style="background:#fff"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{city} 화상과외</span><h2>{city}에서 화상으로 수업하려면</h2></div>
  <div class="two">
    <div class="card"><h3>시간대</h3><p>상담 신청 때 현지 시간 기준 가능한 요일·시간을 적어 주세요. 그 시간대에 맞는 선생님을 찾아 안내합니다.</p></div>
    <div class="card"><h3>수업 자료</h3><p>학생이 받은 syllabus·과제·시험지를 공유하면 그 자료를 기준으로 수업합니다. 학교별 진도는 학교 안내를 우선합니다.</p></div>
  </div>
</div></section>
"""
    body += contact_form(rel)
    body += footer(rel, countries)
    write(f"city/{slug}.html", body)


def build_school(s, all_rows, countries, city_pages, posts=()):
    rel = "../"
    currs = s["curricula"] if s["curricula"] else list(CURRICULA.keys())
    curr_names = curr_text(s)
    tabs = "".join(f'<button data-k="{x["key"]}"{" class=on" if i == 0 else ""}>{x["name"]}</button>' for i, x in enumerate(SUBJECTS))
    panels = ""
    for i, x in enumerate(SUBJECTS):
        blocks = ""
        for ck in currs:
            c = CURRICULA[ck]
            pts = "".join(f"<li>{p}</li>" for p in x["by"][ck])
            blocks += f'<h4 style="margin:14px 0 4px;font-size:15px;color:var(--mint2)">{c["name"]} 기준</h4><ul>{pts}</ul>'
        if s["curricula"]:
            note = f"{s['name']}의 {x['name']} 실제 코스·진도·평가 일정은 학교 syllabus와 학생이 받은 자료를 기준으로 상담 때 확인합니다. 위 내용은 {curr_names} 일반 안내입니다."
        else:
            note = f"{s['name']}의 교육과정은 아직 학교 공식 안내로 확인하지 않아 IB DP·IGCSE·AP·A-Level 일반 안내를 모두 보여 드립니다. 상담 때 학생이 실제 듣는 코스를 기준으로 정리합니다."
        panels += f"""<div class="panel{' on' if i == 0 else ''}" data-k="{x['key']}">
  <h3>{s['name']} {x['name']} 과외</h3>
  <p style="margin:0;color:var(--mute)">{x['desc']}</p>
  {blocks}
  <div class="note">{note}</div>
  <p style="margin-top:16px"><a class="btn btn-d" href="#contact">{s['name']} {x['name']} 상담 신청</a></p>
</div>"""
    if s["sources"]:
        src_items = "".join(f'<div style="margin-top:8px"><a href="{esc(v["source"])}" target="_blank" rel="noopener">{esc(v["source"])}</a> · 확인일 {v["checked"]}<q>{esc(v["quote"])}</q></div>' for v in s["sources"])
        src = f'<div class="src"><b>학교 정보 출처 (공식 홈페이지)</b>{src_items}<div style="margin-top:8px">위 내용 외의 학교별 진도·시험 범위·평가 방식은 학교 안내를 우선하며, 이 페이지에서 추측하지 않습니다.</div></div>'
    else:
        src = f'<div class="src"><b>학교 정보 안내</b>학교명·소재지는 공개 정보 기준입니다. 교육과정·입학 전형은 아직 학교 공식 홈페이지로 확인하지 않았으므로 단정하지 않으며, 상담 때 학생이 실제 듣는 코스와 학교 공식 안내를 기준으로 정리합니다.</div>'
    same_city = [o for o in all_rows if o["country"] == s["country"] and o["city"] == s["city"] and o["slug"] != s["slug"]][:6]
    others = "".join(school_card(o, rel) for o in same_city)
    cslug = s["cslug"]
    city_slug_ = city_pages[(s["country"], s["city"])][0]
    facts = "".join(f"<span>{f}</span>" for f in [s["country"] + " · " + s["city"], curr_names] + ([s["note"]] if s["note"] else []))
    title = f"{s['name']} 과외 | {curr_names if s['curricula'] else s['city'] + ' 국제학교'} 1:1 화상과외 {BRAND}"
    desc = f"{s['city']} {s['name']}({s['name_en']}) 학생을 위한 1:1 화상과외 안내. {curr_names} 기준 수학·영어·과학·입학 준비, 현지 시간대 맞춤, 무료 상담 신청."
    body = head(title, desc, f"school/{s['slug']}.html", rel, og=og_image_url(s))
    body += header(rel)
    body += f"""
<section class="page-hero"><div class="wrap">
  <div class="crumb"><a href="{rel}index.html">홈</a> › <a href="{rel}region/{cslug}.html">{s['country']}</a>{'' if s['city']==s['country'] else ' › <a href="' + rel + 'city/' + city_slug_ + '.html">' + s['city'] + '</a>'} › {s['name']}</div>
  <h1>{s['name']} 과외</h1>
  <p>{s['name_en']} · {s['city']} · 1:1 화상과외</p>
  <div class="facts">{facts}</div>
  <div class="cta"><a class="btn btn-p" href="#contact">무료 상담 신청</a> <a class="btn btn-o" href="{KAKAO}" target="_blank" rel="noopener">카톡 상담</a></div>
</div></section>

<section><div class="wrap">
  {figure_html(s, rel)}
  <div class="sec-head"><span class="eyebrow">과목 선택</span><h2>{s['name']} 과목별 1:1 화상과외</h2><p>과목을 누르면 {"이 학교의 교육과정(" + curr_names + ")" if s['curricula'] else "교육과정별"} 수업 포인트가 나옵니다.</p></div>
  <div class="tabs">{tabs}</div>
  {panels}
  <div style="margin-top:18px">{src}</div>
</div></section>

<section style="background:#fff"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">수업 방식</span><h2>화상 1:1, 학교 자료 기준</h2></div>
  <div class="two">
    <div class="card"><h3>화상 1:1 수업</h3><p>{s['city']}에서도 화면으로 진행합니다. 학생이 받은 syllabus·과제·시험지를 공유하면 그 자료를 기준으로 수업하고, 현지 시간대에 맞춥니다.</p></div>
    <div class="card"><h3>교육과정에 맞는 선생님</h3><p>{curr_names if s['curricula'] else '해당 교육과정'} 과목 지도 경험이 있는 선생님을 찾아 안내합니다. 조건에 맞는 선생님이 없으면 솔직하게 말씀드립니다.</p></div>
  </div>
</div></section>

<div class="cta-band"><div class="wrap">
  <b>{s['name']} 학생, 어떤 과목부터 시작할까요?</b>
  <a class="btn btn-d" href="#contact">무료 상담 신청</a>
</div></div>

<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">진행 절차</span><h2>신청 뒤 이렇게 진행됩니다</h2></div>
  {steps_html(s)}
</div></section>

<section id="faq" style="background:#fff"><div class="wrap faq">
  <div class="sec-head"><span class="eyebrow">FAQ</span><h2>{s['name']} 과외 자주 묻는 질문</h2></div>
  <details open><summary>{s['name']} 교육과정을 알고 수업하나요?</summary><p>{"이 학교의 교육과정(" + curr_names + ")을 기준으로 안내하고," if s['curricula'] else "학교 교육과정은 상담 때 학교 공식 안내로 함께 확인하고,"} 학생의 실제 코스(예: HL/SL, AP 과목)는 학교 자료로 확인합니다.</p></details>
  <details><summary>{s['name']} 학생이 아니어도 신청할 수 있나요?</summary><p>네. {s['city']}의 다른 학교 학생이나 입학 준비 중인 학생도 같은 방법으로 신청하실 수 있습니다.</p></details>
  <details><summary>수업료는 얼마인가요?</summary><p>학년·과목·교육과정·주당 횟수에 따라 달라서 상담 때 안내합니다. 상담 신청은 무료입니다.</p></details>
  <details><summary>입학 준비도 도와주나요?</summary><p>학교 공식 입학 안내에 적힌 전형을 기준으로 준비 방향을 상담합니다. 내부 기출이나 학교와의 제휴는 없으며 합격을 보장하지 않습니다.</p></details>
</div></section>

{school_posts_html(s, posts, rel)}
<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">{s['city']}</span><h2>{s['city']} 다른 국제학교</h2><p><a href="{rel}city/{city_slug_}.html">{s['city']} 전체 보기 →</a> · <a href="{rel}region/{cslug}.html">{s['country']} 전체 보기 →</a></p></div>
  <div class="grid g3">{others if others else '<p style="color:var(--mute)">같은 도시에 등록된 다른 학교가 아직 없습니다.</p>'}</div>
</div></section>
"""
    body += contact_form(rel, default_school=s["name"])
    body += footer(rel, countries)
    write(f"school/{s['slug']}.html", body)



# ---------------- column (posts) ----------------
POSTS_DIR = os.path.join(ROOT, "posts")

def load_posts(schools):
    """posts/<slug>.html : 앞부분 '---' 블록(title/slug/date/school/summary/sources), 뒤는 본문 HTML"""
    by_slug = {s["slug"]: s for s in schools}
    posts = []
    for f in sorted(glob.glob(os.path.join(POSTS_DIR, "*.html"))):
        raw = open(f, encoding="utf-8").read()
        m = re.match(r"\s*---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.S)
        if not m:
            print("!! front matter 없음:", f); continue
        meta, body = {}, m.group(2).strip()
        sources = []
        for line in m.group(1).splitlines():
            if line.strip().startswith("- "):
                parts = [x.strip() for x in line.strip()[2:].split("|")]
                if len(parts) >= 2:
                    sources.append({"url": parts[0], "checked": parts[1], "quote": parts[2] if len(parts) > 2 else ""})
            elif ":" in line:
                k, v = line.split(":", 1); meta[k.strip()] = v.strip()
        slug = meta.get("slug") or os.path.basename(f)[:-5]
        school = by_slug.get(meta.get("school", ""))
        if meta.get("school") and not school:
            print("!! 학교 slug 불일치:", f, meta.get("school"))
        posts.append({"file": f, "slug": slug, "title": meta.get("title", slug), "date": meta.get("date", TODAY),
                      "summary": meta.get("summary", ""), "school": school, "sources": sources, "body": body,
                      "chars": len(re.sub(r"<[^>]+>", "", body).replace(" ", "").replace("\n", ""))})
    posts.sort(key=lambda p: (p["date"], p["slug"]), reverse=True)
    return posts


def post_card(p, rel):
    sc = f'<span class="badge region">{p["school"]["name"]}</span>' if p["school"] else ""
    return f"""<a class="card school-card" href="{rel}column/{p['slug']}.html">
  <span class="badge">{p['date']}</span>{sc}
  <h3 style="margin-top:10px;font-size:17px">{esc(p['title'])}</h3>
  <p>{esc(p['summary'])}</p>
</a>"""


def build_column_index(posts, countries):
    rel = ""
    cards = "".join(post_card(p, rel) for p in posts)
    body = head(f"국제학교 칼럼 | 학교별 교육과정·과목 공부법 {BRAND}", f"국제학교 학교별 칼럼 {len(posts)}편. 학교 공식 출처를 바탕으로 교육과정·과목·입학 준비를 정리합니다. 매일 새 글이 올라옵니다.", "column.html", rel)
    body += header(rel)
    body += f"""
<section class="page-hero"><div class="wrap">
  <div class="crumb"><a href="index.html">홈</a> › 칼럼</div>
  <h1>국제학교 칼럼</h1>
  <p>학교별 교육과정·과목 공부법·입학 준비를 학교 공식 출처와 함께 정리합니다. 전체 {len(posts)}편.</p>
</div></section>
<section><div class="wrap"><div class="grid g3">{cards if cards else '<p>첫 글을 준비 중입니다.</p>'}</div></div></section>
"""
    body += contact_form(rel)
    body += footer(rel, countries)
    write("column.html", body)


def build_post(p, posts, countries, city_pages):
    rel = "../"
    s = p["school"]
    src = ""
    if p["sources"]:
        items = "".join(f'<div style="margin-top:8px"><a href="{esc(v["url"])}" target="_blank" rel="noopener">{esc(v["url"])}</a> · 확인일 {esc(v["checked"])}{("<q>" + esc(v["quote"]) + "</q>") if v["quote"] else ""}</div>' for v in p["sources"])
        src = f'<div class="src" style="margin:26px 0"><b>정보 출처 (학교 공식 자료)</b>{items}<div style="margin-top:8px">학교 공식 자료에서 확인한 사실과 일반적인 교육과정·공부법 설명을 구분해 썼습니다. 학교별 세부 진도·시험 난도는 학교 안내를 우선합니다.</div></div>'
    school_box = ""
    if s:
        school_box = f"""<div class="card" style="margin:26px 0"><span class="badge curr">{curr_text(s)}</span><span class="badge region">{s['city']}</span>
  <h3 style="margin-top:10px">{s['name']} 과외 안내 페이지</h3><p>{s['name_en']} · 과목별 1:1 화상과외 포인트와 출처 보기 → <a href="{rel}school/{s['slug']}.html" style="color:var(--mint2);text-decoration:underline">{s['name']} 과외</a></p></div>"""
    related = [q for q in posts if q["slug"] != p["slug"] and (s and q["school"] and q["school"]["country"] == s["country"])][:3] or [q for q in posts if q["slug"] != p["slug"]][:3]
    rel_cards = "".join(post_card(q, rel) for q in related)
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": p["title"], "description": p["summary"], "datePublished": p["date"], "dateModified": p["date"],
          "author": {"@type": "Organization", "name": BRAND}, "publisher": {"@type": "Organization", "name": BRAND}, "mainEntityOfPage": f"{DOMAIN}/column/{p['slug']}.html"}
    import json as _json
    body = head(f"{p['title']} | {BRAND}", p["summary"], f"column/{p['slug']}.html", rel, og=og_image_url(s))
    body = body.replace("</head>", f'<script type="application/ld+json">{_json.dumps(ld, ensure_ascii=False)}</script>\n</head>')
    body += header(rel)
    body += f"""
<section class="page-hero"><div class="wrap">
  <div class="crumb"><a href="{rel}index.html">홈</a> › <a href="{rel}column.html">칼럼</a>{(' › <a href="' + rel + 'school/' + s['slug'] + '.html">' + s['name'] + '</a>') if s else ''}</div>
  <h1>{esc(p['title'])}</h1>
  <p>{esc(p['summary'])}</p>
  <div class="facts"><span>{p['date']}</span><span>읽는 데 약 {max(3, round(p['chars'] / 600))}분</span>{('<span>' + s['name'] + '</span>') if s else ''}</div>
</div></section>
<section><div class="wrap" style="max-width:820px">
  {figure_html(s, rel, "margin:0 0 22px") if s else ""}
  <article class="post">{p['body']}</article>
  {src}
  {school_box}
  <div class="cta-band" style="border-radius:14px"><div class="wrap" style="padding:0"><b>{(s['name'] + ' ') if s else ''}과목·학년만 알려주시면 맞는 선생님을 찾아 안내합니다</b><a class="btn btn-d" href="#contact">무료 상담 신청</a></div></div>
</div></section>
<section style="background:#fff"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">함께 읽기</span><h2>다른 칼럼</h2></div>
  <div class="grid g3">{rel_cards}</div>
  <p style="margin-top:14px"><a href="{rel}column.html">칼럼 전체 보기 →</a></p>
</div></section>
"""
    body += contact_form(rel, default_school=s["name"] if s else "")
    body += footer(rel, countries)
    write(f"column/{p['slug']}.html", body)


def build_rss(posts):
    items = "".join(f"<item><title>{esc(p['title'])}</title><link>{DOMAIN}/column/{p['slug']}.html</link><guid>{DOMAIN}/column/{p['slug']}.html</guid><pubDate>{p['date']}</pubDate><description>{esc(p['summary'])}</description></item>" for p in posts[:50])
    write("rss.xml", f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>{BRAND} 칼럼</title><link>{DOMAIN}/column.html</link><description>국제학교 학교별 칼럼</description>{items}</channel></rss>')


def school_posts_html(s, posts, rel):
    mine = [p for p in posts if p["school"] and p["school"]["slug"] == s["slug"]]
    if not mine:
        return ""
    return f"""<section style="background:#fff"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">칼럼</span><h2>{s['name']} 칼럼</h2><p>학교 공식 출처를 바탕으로 쓴 글입니다.</p></div>
  <div class="grid g3">{"".join(post_card(p, rel) for p in mine[:6])}</div>
</div></section>"""


def build_sitemap(schools, countries, city_pages, posts):
    urls = [f"{DOMAIN}/", f"{DOMAIN}/schools.html", f"{DOMAIN}/regions.html"]
    urls += [f"{DOMAIN}/region/{cs}.html" for _, cs in countries]
    urls += [f"{DOMAIN}/city/{slug}.html" for slug, _ in city_pages.values()]
    urls += [f"{DOMAIN}/school/{s['slug']}.html" for s in schools]
    urls += [f"{DOMAIN}/column.html"] + [f"{DOMAIN}/column/{p['slug']}.html" for p in posts]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += "".join(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    write("sitemap.xml", xml)
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    return len(urls)


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full) or ROOT, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    schools = load_schools()
    # 국가 순서: GROUPS 순 → 그 외
    order = [c for _, cl in GROUPS for c in cl]
    by_country = {}
    for s in schools:
        by_country.setdefault(s["country"], []).append(s)
    countries = sorted(by_country.keys(), key=lambda c: (order.index(c) if c in order else 999, c))
    countries = [(c, by_country[c][0]["cslug"]) for c in countries]
    # 도시 페이지 슬러그
    city_pages = {}
    for c, cs in countries:
        cities = []
        for s in by_country[c]:
            if s["city"] not in cities:
                cities.append(s["city"])
        for i, city in enumerate(cities):
            n = sum(1 for s in by_country[c] if s["city"] == city)
            city_pages[(c, city)] = (f"{cs}-{i+1}", n)
    posts = load_posts(schools)
    for d in ("school", "region", "city", "column"):
        for f in glob.glob(os.path.join(ROOT, d, "*.html")):
            os.remove(f)
    build_index(schools, countries, by_country, posts)
    build_schools_index(schools, countries, by_country)
    build_regions(schools, countries, by_country, city_pages)
    for c, cs in countries:
        build_country(c, cs, by_country[c], countries, city_pages)
    for (c, city), (slug, n) in city_pages.items():
        build_city(c, city, slug, [s for s in by_country[c] if s["city"] == city], countries, by_country[c][0]["cslug"])
    for s in schools:
        build_school(s, schools, countries, city_pages, posts)
    build_column_index(posts, countries)
    for p in posts:
        build_post(p, posts, countries, city_pages)
    build_rss(posts)
    n = build_sitemap(schools, countries, city_pages, posts)
    nv = sum(1 for s in schools if s["verified"])
    nc = sum(1 for s in schools if s["curricula"])
    print(f"칼럼 {len(posts)}편 / 학교 {len(schools)}곳 / 국가 {len(countries)} / 도시 {len(city_pages)} / 공식출처 확인 {nv} / 교육과정 표기 {nc} / URL {n}")


if __name__ == "__main__":
    main()
