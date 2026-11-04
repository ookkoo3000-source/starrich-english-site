# -*- coding: utf-8 -*-
"""받아온 학교 사진 검토용 한 장짜리 페이지 생성: _review/images.html (사이트맵·배포 제외)
python tools/contact_sheet.py
"""
import os, sys, json, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "data"))
import build

schools = build.load_schools()
data = json.load(open(os.path.join(ROOT, "data", "images.json"), encoding="utf-8"))
cards = []
for s in schools:
    v = data.get(s["slug"])
    if not v:
        continue
    cards.append(f'''<div class="c"><img src="../{v["file"]}" loading="lazy"><div class="t"><b>{html.escape(s["name"])}</b><br><small>{html.escape(s["name_en"])} · {s["country"]} {s["city"]}</small><br><small>{html.escape(v["title"][5:70])}</small><br><small>{html.escape(v["license"])} · {html.escape(v["artist"][:30])}</small><br><code>{s["slug"]}</code></div></div>''')
os.makedirs(os.path.join(ROOT, "_review"), exist_ok=True)
page = f'''<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><title>사진 검토 {len(cards)}장</title>
<style>body{{font-family:Pretendard,sans-serif;margin:16px;background:#f4f4f4}}.g{{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}}.c{{background:#fff;border:1px solid #ddd;border-radius:8px;overflow:hidden}}.c img{{width:100%;height:150px;object-fit:cover;display:block}}.t{{padding:8px;font-size:12px;line-height:1.4}}code{{font-size:10px;color:#777}}</style></head>
<body><h1>학교 사진 검토 ({len(cards)}장)</h1><p>잘못 매칭된 사진은 data/images.json에서 해당 slug를 null로 바꾸고 img/schools/&lt;slug&gt;.jpg 삭제</p><div class="g">{"".join(cards)}</div></body></html>'''
open(os.path.join(ROOT, "_review", "images.html"), "w", encoding="utf-8").write(page)
print("_review/images.html", len(cards))
