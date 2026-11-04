# -*- coding: utf-8 -*-
"""학교 사진에서 사람 얼굴 검출 → 초상권 문제 사진 제외.
python tools/face_check.py            : img/schools/*.jpg 전체 검사, 얼굴 있는 파일 목록 + _review/faces.html 생성
python tools/face_check.py --remove   : 검출된 사진을 images.json에서 null 처리하고 파일 삭제
fetch_images.py에서도 import해 다운로드 직후 검사한다.
"""
import os, sys, json, html
import cv2

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(ROOT, "img", "schools")
CASCADES = [cv2.data.haarcascades + "haarcascade_frontalface_default.xml",
            cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml",
            cv2.data.haarcascades + "haarcascade_profileface.xml"]
_DET = [cv2.CascadeClassifier(c) for c in CASCADES]


def faces_in(path, min_frac=0.025):
    """이미지 긴 변의 min_frac 이상 크기의 얼굴 개수 (작은 배경 인물은 무시)"""
    img = cv2.imread(path)
    if img is None:
        return 0
    h, w = img.shape[:2]
    scale = 1000 / max(h, w)
    if scale < 1:
        img = cv2.resize(img, (int(w * scale), int(h * scale)))
        h, w = img.shape[:2]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    minsz = max(20, int(max(h, w) * min_frac))
    n = 0
    for det in _DET:
        found = det.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6, minSize=(minsz, minsz))
        n = max(n, len(found))
        if n:
            break
    return n


def main():
    data_p = os.path.join(ROOT, "data", "images.json")
    data = json.load(open(data_p, encoding="utf-8"))
    flagged = []
    for slug, v in data.items():
        if not v:
            continue
        p = os.path.join(ROOT, v["file"])
        if not os.path.exists(p):
            continue
        n = faces_in(p)
        if n:
            flagged.append((slug, n, v))
    print(f"얼굴 검출 {len(flagged)}장 / 검사 {sum(1 for v in data.values() if v)}장")
    for slug, n, v in flagged:
        print(f"  {slug} ({n}) {v['title'][5:60]}")
    os.makedirs(os.path.join(ROOT, "_review"), exist_ok=True)
    cards = "".join(f'<div class="c"><img src="../{v["file"]}"><div class="t"><b>{slug}</b><br>얼굴 {n} · {html.escape(v["title"][5:60])}</div></div>' for slug, n, v in flagged)
    open(os.path.join(ROOT, "_review", "faces.html"), "w", encoding="utf-8").write(
        f'<!DOCTYPE html><html lang="ko"><head><meta charset="UTF-8"><style>body{{font-family:sans-serif;margin:16px}}.g{{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}}.c img{{width:100%;height:150px;object-fit:cover}}.t{{font-size:12px;padding:6px}}</style></head><body><h1>얼굴 검출 {len(flagged)}장</h1><div class="g">{cards}</div></body></html>')
    if "--remove" in sys.argv:
        for slug, n, v in flagged:
            data[slug] = None
            p = os.path.join(ROOT, v["file"])
            if os.path.exists(p):
                os.remove(p)
        json.dump(data, open(data_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("제거 완료, 남은 사진", sum(1 for v in data.values() if v))


if __name__ == "__main__":
    main()
