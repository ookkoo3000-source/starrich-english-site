# -*- coding: utf-8 -*-
"""칼럼 원고 형식 검수. python tools/check_post.py posts/<file>.html [...]
검사: front matter(title/slug/date/school/summary/sources), 제목에 학교명, 서론 300자+, h2 6개+, 각 섹션 500자+(목표 700), FAQ 3개+, 본문 2,000자+(목표 4,000), 출처 1개+, 금지 문구.
통과 ≠ 내용 검증. 사실·출처는 사람이 본다.
"""
import sys, re, os, glob, importlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "data"))

BANNED = ["합격 보장", "합격보장", "100%", "기출 보유", "기출문제 보유", "내부 자료", "제휴", "협약", "최고의", "1위", "유일한", "무조건", "반드시 합격", "족보"]


def strip(h):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()


def chars(h):
    return len(strip(h).replace(" ", ""))


def check(path):
    raw = open(path, encoding="utf-8").read()
    errs, warns = [], []
    m = re.match(r"\s*---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.S)
    if not m:
        return ["front matter(---) 없음"], []
    meta = {}
    sources = 0
    for line in m.group(1).splitlines():
        if line.strip().startswith("- "):
            sources += 1
        elif ":" in line:
            k, v = line.split(":", 1); meta[k.strip()] = v.strip()
    body = m.group(2)
    for k in ("title", "slug", "date", "summary"):
        if not meta.get(k):
            errs.append(f"{k} 없음")
    if not re.match(r"\d{4}-\d{2}-\d{2}$", meta.get("date", "")):
        errs.append("date 형식(YYYY-MM-DD) 오류")
    if sources < 1:
        errs.append("sources(출처) 없음")
    # 학교 매칭
    schools = []
    for f in sorted(glob.glob(os.path.join(ROOT, "data", "dir_*.py"))):
        schools += importlib.import_module(os.path.basename(f)[:-3]).SCHOOLS
    sch = None
    if meta.get("school"):
        import build
        for s in schools:
            if build.ascii_slug(s["name_en"]) == meta["school"]:
                sch = s; break
        if not sch:
            errs.append(f"school slug '{meta['school']}' 디렉토리에 없음")
        else:
            key = re.sub(r"\s*\(.*?\)", "", sch["name"]).strip()
            short = key.split()[0]
            if key not in meta.get("title", "") and short not in meta.get("title", ""):
                errs.append(f"제목에 학교명('{key}') 없음")
    else:
        warns.append("school 미지정(학교 페이지에 연결 안 됨)")
    # 본문 구조
    total = chars(body)
    if total < 2000:
        errs.append(f"본문 {total}자 (<2,000)")
    elif total < 4000:
        warns.append(f"본문 {total}자 (목표 4,000+)")
    h2s = re.findall(r"<h2[^>]*>(.*?)</h2>", body, re.S)
    first_h2 = body.find("<h2")
    intro = chars(body[:first_h2]) if first_h2 > 0 else 0
    if intro < 300:
        errs.append(f"서론 {intro}자 (<300)")
    secs = re.split(r"<h2[^>]*>.*?</h2>", body, flags=re.S)[1:]
    faq_idx = [i for i, t in enumerate(h2s) if "FAQ" in t.upper() or "자주 묻는" in t]
    content_secs = [(h2s[i], chars(secs[i])) for i in range(len(secs)) if i not in faq_idx]
    if len(content_secs) < 6:
        errs.append(f"소제목(h2) {len(content_secs)}개 (<6, FAQ 제외)")
    for t, n in content_secs:
        if n < 500:
            errs.append(f"섹션 '{strip(t)[:20]}' {n}자 (<500)")
        elif n < 700:
            warns.append(f"섹션 '{strip(t)[:20]}' {n}자 (목표 700+)")
    if not faq_idx:
        errs.append("FAQ 섹션(h2에 FAQ) 없음")
    else:
        faq_q = len(re.findall(r'class="faq-q"|<h3', secs[faq_idx[0]]))
        if faq_q < 3:
            errs.append(f"FAQ 질문 {faq_q}개 (<3)")
    for b in BANNED:
        if b in strip(body) or b in meta.get("title", ""):
            errs.append(f"금지 문구 '{b}'")
    if "정보 출처" in body:
        warns.append("본문에 출처 박스 직접 작성됨 (front matter sources로만 넣기)")
    return errs, warns


if __name__ == "__main__":
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, "posts", "*.html")))
    bad = 0
    for f in files:
        errs, warns = check(f)
        print(("FAIL " if errs else "PASS ") + os.path.basename(f))
        for e in errs: print("   ✗", e)
        for w in warns: print("   -", w)
        bad += bool(errs)
    sys.exit(1 if bad else 0)
