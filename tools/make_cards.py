# -*- coding: utf-8 -*-
"""공용 사진이 없는 학교용 브랜드 카드 이미지 생성 → img/cards/<slug>.jpg (1200x630)
python tools/make_cards.py [--all]   (기본: 사진 없는 학교만. --all: 전부)
칼럼 상단 이미지·og:image 대체용. 학교명·영문명·도시·교육과정만 그린다(사실 외 문구 없음).
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "data"))
import build

W, H = 1200, 630
NAVY, NAVY2, CREAM, BRASS, MINT = (18, 58, 46), (27, 77, 61), (246, 242, 231), (201, 164, 92), (231, 239, 233)
FB, FR = r"C:\Windows\Fonts\malgunbd.ttf", r"C:\Windows\Fonts\malgun.ttf"
OUT = os.path.join(ROOT, "img", "cards")
os.makedirs(OUT, exist_ok=True)


def font(p, s):
    return ImageFont.truetype(p, s)


def fit(draw, text, f_path, max_w, start, min_size=30):
    size = start
    while size > min_size:
        f = font(f_path, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return font(f_path, min_size)


def wrap(draw, text, f, max_w):
    words, lines, cur = text.split(" "), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=f) <= max_w:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines[:2]


def make(s):
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    for i in range(W):
        t = i / W
        d.line([(i, 0), (i, H)], fill=tuple(int(NAVY[k] + (NAVY2[k] - NAVY[k]) * t) for k in range(3)))
    d.ellipse((860, -160, 1360, 340), outline=(60, 110, 90), width=2)
    d.ellipse((920, -100, 1300, 280), outline=BRASS, width=2)
    d.rectangle((0, 0, W, 10), fill=BRASS)
    d.text((72, 56), build.BRAND, font=font(FB, 34), fill=CREAM)
    d.text((72, 118), f"{s['country']} · {s['city']}  ·  국제학교 1:1 화상과외", font=font(FR, 24), fill=BRASS)
    # 학교명 (최대 2줄)
    f = fit(d, s["name"], FB, 1000, 64, 40)
    lines = wrap(d, s["name"], f, 1000)
    y = 180
    for ln in lines:
        d.text((72, y), ln, font=f, fill=(255, 255, 255)); y += f.size + 12
    # 영문명
    fe = fit(d, s["name_en"], FR, 1000, 32, 22)
    d.text((72, y + 6), s["name_en"], font=fe, fill=(203, 213, 230)); y += fe.size + 40
    # 교육과정 칩
    chips = [build.CURRICULA[c]["name"] for c in s["curricula"]] or ["교육과정 상담 때 확인"]
    x = 72
    for c in chips:
        fc = font(FB, 24); w = d.textlength(c, font=fc) + 36
        d.rounded_rectangle((x, y, x + w, y + 46), radius=23, fill=MINT)
        d.text((x + 18, y + 9), c, font=fc, fill=(31, 92, 71)); x += w + 12
    d.rectangle((0, H - 70, W, H), fill=CREAM)
    d.text((72, H - 52), build.DOMAIN.replace("https://", ""), font=font(FB, 28), fill=NAVY)
    tail = "수학 · 영어·에세이 · 과학 · 입학 준비"
    d.text((W - 72 - d.textlength(tail, font=font(FR, 24)), H - 50), tail, font=font(FR, 24), fill=(90, 90, 80))
    img.save(os.path.join(OUT, s["slug"] + ".jpg"), "JPEG", quality=85, optimize=True)


def main():
    schools = build.load_schools()
    n = 0
    for s in schools:
        if "--all" in sys.argv or not build.school_image(s):
            make(s); n += 1
    print("cards", n, "→ img/cards/")


if __name__ == "__main__":
    main()
