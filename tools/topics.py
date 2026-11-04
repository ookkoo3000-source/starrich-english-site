# -*- coding: utf-8 -*-
"""오늘 쓸 칼럼 학교 후보. python tools/topics.py [개수=10]
우선순위: 아직 칼럼 없는 학교 중 (1) 공식 출처 있음+교육과정 표기 (2) 국내 (3) 교육과정 표기 (4) 나머지, 같은 국가 연속 배분.
학교당 여러 글 가능(과목·의도가 다르면). 이 목록은 '검색 의도 기반 후보'일 뿐, 검색량 자료 아님.
"""
import sys, os, re, glob, importlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "data"))
import build

n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
schools = build.load_schools()
posts = build.load_posts(schools)
done = {}
for p in posts:
    if p["school"]:
        done[p["school"]["slug"]] = done.get(p["school"]["slug"], 0) + 1

def rank(s):
    return (done.get(s["slug"], 0), 0 if (s["verified"] and s["curricula"]) else 1, 0 if s["country"] == "대한민국" else 1, 0 if s["curricula"] else 1)

cands = sorted(schools, key=rank)
picked, per_country = [], {}
for s in cands:
    if per_country.get(s["country"], 0) >= max(2, n // 4) and len(cands) > n * 3:
        continue
    picked.append(s); per_country[s["country"]] = per_country.get(s["country"], 0) + 1
    if len(picked) >= n:
        break
print(f"칼럼 {len(posts)}편 발행됨 / 학교 {len(schools)}곳 중 칼럼 있는 학교 {len(done)}곳\n")
for s in picked:
    src = s["sources"][0] if s["sources"] else None
    print(f"- {s['name']} | {s['name_en']} | {s['country']} {s['city']} | {build.curr_text(s)} | slug={s['slug']} | 기존글 {done.get(s['slug'],0)}")
    if src:
        print(f"    출처: {src['source']} ({src['checked']}) — {src['quote'][:80]}")
