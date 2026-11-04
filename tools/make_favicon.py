# -*- coding: utf-8 -*-
"""파비콘 생성: img/favicon.svg, img/favicon.ico(16·32·48), img/favicon-32.png, img/apple-touch-icon.png(180)
딥그린 둥근 사각 + 브라스 별. python tools/make_favicon.py
"""
import os, math
from PIL import Image, ImageDraw
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "img")
NAVY, BRASS, CREAM = (18, 58, 46), (201, 164, 92), (246, 242, 231)


def star_points(cx, cy, r_out, r_in, n=5, rot=-90):
    pts = []
    for i in range(n * 2):
        r = r_out if i % 2 == 0 else r_in
        a = math.radians(rot + i * 180 / n)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def render(size):
    S = size * 4  # 슈퍼샘플링
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, S - 1, S - 1), radius=int(S * 0.22), fill=NAVY)
    d.polygon(star_points(S / 2, S * 0.52, S * 0.36, S * 0.15), fill=BRASS)
    d.ellipse((S * 0.70, S * 0.14, S * 0.84, S * 0.28), fill=CREAM)
    return im.resize((size, size), Image.LANCZOS)


os.makedirs(IMG, exist_ok=True)
render(512).save(os.path.join(IMG, "favicon-512.png"))
render(180).save(os.path.join(IMG, "apple-touch-icon.png"))
render(32).save(os.path.join(IMG, "favicon-32.png"))
render(64).save(os.path.join(IMG, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in star_points(32, 33.3, 23, 9.6))
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#123a2e"/><polygon points="{pts}" fill="#c9a45c"/><circle cx="49" cy="13.5" r="4.5" fill="#f6f2e7"/></svg>'''
open(os.path.join(IMG, "favicon.svg"), "w", encoding="utf-8").write(svg)
print("favicon ok")
