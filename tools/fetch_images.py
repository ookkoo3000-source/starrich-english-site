# -*- coding: utf-8 -*-
"""위키미디어 공용(Wikimedia Commons)에서 학교 사진을 찾아 받아온다. 학교 홈페이지 사진은 쓰지 않는다.
python tools/fetch_images.py [--missing] [--limit N] [slug ...]
- 허용 라이선스: CC0, Public domain, CC BY x.x, CC BY-SA x.x (NC/ND 제외)
- 결과: data/images.json {slug: {file, page, thumb, license, license_url, artist, credit, title}} + img/schools/<slug>.jpg
- 관련성: 학교 영문명 핵심 단어가 파일 제목/설명에 있어야 함. 로고·지도·SVG·PDF·군(軍) 홍보사진 제외
"""
import os, sys, re, json, time, glob, importlib, urllib.request, urllib.parse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "data")); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "images.json")
IMG_DIR = os.path.join(ROOT, "img", "schools")
UA = "IntlSchoolTutorSite/0.1 (contact: ookkoo12@naver.com) python-urllib"
API = "https://commons.wikimedia.org/w/api.php"
STOP = {"international", "school", "of", "the", "in", "college", "academy", "campus", "and"}
BAD = re.compile(r"logo|map|seal|crest|emblem|flag|\.svg|\.pdf|\.gif|us navy|u\.s\. navy|army|usace|air force|marine|badge|diagram|chart|student|teacher|principal|ambassador|graduat|class of|visit|cheer|choir|parade|cadet|concert|basketball|football|soccer|rugby|dance|jersey|museum|portrait|\(talk\)|unveil|band|team|ceremony|celebrat|homecoming|1[89]\d\d", re.I)
ALLOWED = re.compile(r"^(cc0|public domain|pd|cc by(-sa)?( \d\.\d)?)", re.I)


def norm_tokens(s):
    return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 2]


def api(params):
    params = dict(params, format="json")
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()


def search(name_en, extra_terms=()):
    cands = []
    queries = [f'"{name_en}"'] + [f'"{t}"' for t in extra_terms if t]
    seen = set()
    for q in queries:
        try:
            d = api({"action": "query", "generator": "search", "gsrsearch": q, "gsrnamespace": 6, "gsrlimit": 12,
                     "prop": "imageinfo", "iiprop": "url|extmetadata|mime|size", "iiurlwidth": 1200})
        except Exception as e:
            print("   api err", e); continue
        for pg in (d.get("query", {}).get("pages", {}) or {}).values():
            if pg.get("pageid") in seen:
                continue
            seen.add(pg.get("pageid"))
            ii = (pg.get("imageinfo") or [{}])[0]
            if not ii or not ii.get("mime", "").startswith("image/") or ii.get("mime") in ("image/svg+xml", "image/gif"):
                continue
            if (ii.get("width") or 0) < 600:
                continue
            md = ii.get("extmetadata", {})
            lic = strip_tags(md.get("LicenseShortName", {}).get("value", ""))
            if not ALLOWED.match(lic):
                continue
            title = pg.get("title", "")
            desc = strip_tags(md.get("ImageDescription", {}).get("value", ""))
            if BAD.search(title) or BAD.search(desc[:200]):
                continue
            toks = norm_tokens(name_en)
            tl, dl = title.lower(), desc.lower()
            in_title = sum(1 for t in toks if t in tl)
            in_desc = sum(1 for t in toks if t in dl)
            if toks and in_title < max(1, len(toks) - 1) and in_desc < len(toks):
                continue
            score = in_title * 3 + in_desc + (2 if "campus" in tl or "building" in tl or "school" in tl else 0) + (1 if lic.lower().startswith("cc0") or "public" in lic.lower() else 0)
            cands.append({"score": score, "title": title, "page": ii.get("descriptionurl"), "thumb": ii.get("thumburl") or ii.get("url"),
                          "license": lic, "license_url": strip_tags(md.get("LicenseUrl", {}).get("value", "")),
                          "artist": strip_tags(md.get("Artist", {}).get("value", ""))[:80], "credit": strip_tags(md.get("Credit", {}).get("value", ""))[:120]})
        time.sleep(0.3)
    cands.sort(key=lambda c: -c["score"])
    return cands[0] if cands else None


def download(url, path):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r, open(path, "wb") as f:
        f.write(r.read())


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    only_missing = "--missing" in sys.argv
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    sys.path.insert(0, ROOT)
    import build
    schools = build.load_schools()
    if args:
        schools = [s for s in schools if s["slug"] in args]
    data = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    os.makedirs(IMG_DIR, exist_ok=True)
    done = 0
    for s in schools:
        if only_missing and s["slug"] in data:
            continue
        if limit and done >= limit:
            break
        done += 1
        print(f"[{done}] {s['name']} / {s['name_en']}")
        acr = re.search(r"\(([A-Z]{2,6})\)", s["name"])
        extra = []
        if acr and s["city"]:
            extra.append(f"{acr.group(1)} {s['city_en']}" if s.get("city_en") else None)
        c = search(s["name_en"], extra)
        if not c:
            data[s["slug"]] = None
            print("   없음")
        else:
            path = os.path.join(IMG_DIR, s["slug"] + ".jpg")
            try:
                download(c["thumb"], path)
                try:
                    from face_check import faces_in
                    nf = faces_in(path)
                except Exception:
                    nf = 0
                if nf:
                    os.remove(path)
                    data[s["slug"]] = None
                    print(f"   제외(얼굴 {nf}) {c['title'][:60]}")
                    json.dump(data, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
                    continue
                c["file"] = f"img/schools/{s['slug']}.jpg"
                data[s["slug"]] = c
                print(f"   OK {c['license']} | {c['artist']} | {c['title'][:60]}")
            except Exception as e:
                print("   다운로드 실패", e)
                data[s["slug"]] = None
        json.dump(data, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    have = sum(1 for v in data.values() if v)
    print(f"\n사진 있음 {have} / 조회 {len(data)}")


if __name__ == "__main__":
    main()
