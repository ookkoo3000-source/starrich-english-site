# -*- coding: utf-8 -*-
"""링크 미리보기(og:image) 기본 이미지 생성 → img/og-default.jpg (1200x630)
python tools/make_og.py   (브랜드명·도메인은 build.py 상수를 읽음. 브랜드 바꾸면 다시 실행)
"""
import os, sys, re
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "data"))
import build

W, H = 1200, 630
NAVY, NAVY2, CREAM, BRASS, MINT = (18, 58, 46), (27, 77, 61), (246, 242, 231), (201, 164, 92), (231, 239, 233)
FONT_B = r"C:\Windows\Fonts\malgunbd.ttf"
FONT_R = r"C:\Windows\Fonts\malgun.ttf"
BATANG = r"C:\Windows\Fonts\batang.ttc"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.truetype(FONT_R, size)


schools = build.load_schools()
n_schools, n_countries = len(schools), len({s["country"] for s in schools})
domain = build.DOMAIN.replace("https://", "")

img = Image.new("RGB", (W, H), NAVY)
d = ImageDraw.Draw(img)
# 대각 그라데이션 느낌의 밝은 띠
for i in range(W):
    t = i / W
    col = tuple(int(NAVY[k] + (NAVY2[k] - NAVY[k]) * t) for k in range(3))
    d.line([(i, 0), (i, H)], fill=col)
# 오른쪽 장식 원
d.ellipse((860, -160, 1360, 340), outline=(255, 255, 255, 40), width=2)
d.ellipse((920, -100, 1300, 280), outline=BRASS, width=2)
# 브라스 상단 라인
d.rectangle((0, 0, W, 10), fill=BRASS)

# 브랜드
d.text((72, 60), build.BRAND, font=font(FONT_B, 40), fill=CREAM)
d.rectangle((72 + font(FONT_B, 40).getlength(build.BRAND) + 10, 86, 72 + font(FONT_B, 40).getlength(build.BRAND) + 22, 98), fill=BRASS)
# 태그
tag = "국제학교 · 외국인학교 학교별 1:1 화상과외"
d.text((72, 140), tag, font=font(FONT_R, 26), fill=BRASS)
# 헤드라인 (세리프 느낌으로 바탕체 굵게 대신 맑은고딕 볼드 사용)
h1 = ["우리 아이 학교의 교육과정에", "맞춘 1:1 화상과외"]
y = 190
for line in h1:
    d.text((72, y), line, font=font(FONT_B, 66), fill=(255, 255, 255))
    y += 84
# 서브
sub = f"국내·해외 국제학교 {n_schools:,}곳 · {n_countries}개국  |  IB DP · IGCSE · AP · A-Level"
d.text((72, 380), sub, font=font(FONT_R, 28), fill=(203, 213, 230))
# 칩
chips = ["수학", "영어·에세이", "과학", "입학 준비"]
x = 72
for c in chips:
    f = font(FONT_B, 24)
    w = f.getlength(c) + 36
    d.rounded_rectangle((x, 440, x + w, 486), radius=23, fill=MINT)
    d.text((x + 18, 449), c, font=f, fill=(31, 92, 71))
    x += w + 12
# 하단 도메인 바
d.rectangle((0, H - 70, W, H), fill=CREAM)
d.text((72, H - 52), domain, font=font(FONT_B, 28), fill=NAVY)
d.text((W - 72 - font(FONT_R, 24).getlength("무료 상담 · 현지 시간대 맞춤 화상 수업"), H - 50), "무료 상담 · 현지 시간대 맞춤 화상 수업", font=font(FONT_R, 24), fill=(90, 90, 80))

out = os.path.join(ROOT, "img", "og-default.jpg")
img.save(out, "JPEG", quality=88, optimize=True)
print("wrote", out, os.path.getsize(out) // 1024, "KB")
