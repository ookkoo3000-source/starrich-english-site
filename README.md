# tutormap-site (가칭 인터튜터) — 국제학교 학교별 1:1 화상과외 사이트

tutornet.co.kr의 "학교 먼저 → 과목" 구조를 참고해 만든 새 브랜드 사이트. 학교당 1페이지(과목은 탭, 교육과정 기준) 방식.
(폴더명은 초기 작업명. 브랜드 확정 시 함께 변경)

- `build.py` : index.html + school/<slug>.html + sitemap.xml 생성. 브랜드·도메인·연락처는 상단 상수
- `data/schools.py` : 학교 목록. 공식 홈페이지에서 확인한 사실 + 출처 URL + 확인일만. curricula로 과목 탭 내용 결정
- `data/subjects.py` : 과목 4영역(수학·영어·과학·입학 준비) × 교육과정(IB DP·IGCSE·AP·A-Level) 포인트
- `css/style.css` : 딥그린·크림·브라스 팔레트, 제목 Noto Serif KR

## 규칙
- 학교 정보는 출처+확인일 있는 사실만. 학교별 진도·난도·채점 성향 추측 금지
- 선생님 수·후기·합격 실적·가격 등 미확인 수치 없음 (히어로 수치는 데이터 개수만)
- 입학 준비는 공식 전형 기준 "상담"으로만. 합격 보장·내부 기출·제휴 표현 금지
- 사업자정보 비공개
- 학교 추가: 공식 홈페이지 확인 → `data/schools.py`에 추가 → `python build.py`
- 브랜드·도메인 확정 시 `build.py` BRAND / DOMAIN 수정 후 재빌드

## 명령
```
python build.py
```

## 칼럼 (2026-11-04 추가) — 매일 10편
- 원고: `posts/YYYY-MM-DD-<slug>.html` 파일 1개 = 글 1편. 앞부분 `---` 블록(title/slug/date/school/summary/sources), 뒤는 본문 HTML
- `school:`에 학교 slug(= school/<slug>.html)를 넣으면 학교 페이지 "칼럼" 섹션·빵부스러기·상담폼 학교명이 자동 연결
- `sources:`는 `- URL | 확인일 | 원문 인용` 줄. 빌드가 글 아래 출처 박스를 만든다(본문에 출처 박스 직접 쓰지 않기)
- 검수: `python tools/check_post.py posts/<file>` (서론 300+, h2 6+, 섹션 700+, FAQ 3+, 본문 4,000+ 목표/2,000 최소, 금지 문구). 통과 ≠ 사실 검증
- 후보: `python tools/topics.py 10` (칼럼 없는 학교, 출처·교육과정 있는 순). 학교 교육과정은 글 쓰기 전 공식 홈페이지에서 확인해 sources에 넣는다
- 빌드: `python build.py` → column.html, column/<slug>.html, rss.xml, sitemap, 메인 최근 칼럼 6편
- 규칙: 학교 사실은 출처 인용분만, 나머지는 "일반적으로". 학교 세부 진도·난도·실적·가격 추측 금지. 합격 보장·기출 보유·제휴 표현 금지. 예시 문제는 "예시" 표기

## 학교 사진 (2026-11-04 추가) — 위키미디어 공용만
- 학교 홈페이지 사진은 쓰지 않는다(저작권). `tools/fetch_images.py --missing`이 Wikimedia Commons에서 CC0·퍼블릭도메인·CC BY·CC BY-SA 사진만 골라 `img/schools/<slug>.jpg`로 받고 `data/images.json`에 촬영자·라이선스·원본 링크를 기록
- 빌드가 학교 페이지·칼럼·학교 카드에 사진 + 캡션(촬영자·라이선스 링크·원본 링크·"학교 제공 아님, 문제 시 삭제") 자동 삽입, og:image도 설정
- 사진이 없는 학교는 사진 없이 그대로. 잘못 매칭된 사진은 images.json에서 해당 slug 값을 null로 바꾸고 jpg 삭제 후 재빌드
- 특정 학교만 다시: `python tools/fetch_images.py <slug> ...`

## 링크 미리보기 이미지
- `python tools/make_og.py` → img/og-default.jpg (1200x630). 브랜드명·도메인·학교 수를 build.py와 데이터에서 읽음. 브랜드 바꾸면 다시 실행
- 모든 페이지 og:image 기본값. 학교 사진이 있는 학교·칼럼 페이지는 그 사진이 og:image
- 네이버 블로그 링크 삽입 시 미리보기가 안 뜨면 URL 뒤에 `?v=2` 같은 쿼리를 붙이면 재수집됨(네이버 URL 단위 캐시)

## 인물 사진 금지 (2026-11-04)
- 사람 얼굴·인물이 보이는 사진은 쓰지 않는다(초상권). `tools/face_check.py`(OpenCV Haar)로 검사, `--remove`로 일괄 제거. fetch_images.py는 다운로드 직후 얼굴 검사해 자동 제외
- 공용 사진이 없는 학교는 `tools/make_cards.py`가 img/cards/<slug>.jpg(학교명·영문명·도시·교육과정 카드) 생성 → 칼럼 상단·og:image에 자동 사용. 학교 추가 후엔 make_cards.py 재실행
