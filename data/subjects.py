# -*- coding: utf-8 -*-
# 교육과정 × 과목 수업 포인트. 일반적인 교육과정 설명이며 학교별 진도·난도·채점 성향은 쓰지 않는다.
CURRICULA = {
    "ibdp":  {"name": "IB DP",  "full": "IB Diploma Programme"},
    "igcse": {"name": "IGCSE",  "full": "Cambridge/Edexcel IGCSE"},
    "ap":    {"name": "AP",     "full": "Advanced Placement (College Board)"},
    "alevel":{"name": "A-Level","full": "A-Level"},
}

SUBJECTS = [
    {"key": "math", "name": "수학", "icon": "∑",
     "desc": "교육과정별 코스 선택부터 내부평가(IA)·외부시험까지 1:1로 잡습니다.",
     "by": {
        "ibdp":  ["Mathematics AA / AI, HL / SL 선택 기준 정리", "Paper 1·2(·3) 유형별 접근과 시간 배분", "Math IA 주제 선정과 탐구 보고서 구조"],
        "igcse": ["0580/0606 등 코스 코드별 범위 확인", "Paper별 계산기 사용 규정과 풀이 습관", "Past paper 기반 반복과 mark scheme 읽기"],
        "ap":    ["Precalculus → AP Calculus AB/BC 진도 설계", "Free Response 서술 방식 훈련", "AP Statistics 선택 시 자료 해석 기초"],
        "alevel":["Pure·Mechanics·Statistics 모듈 구성 이해", "Paper별 기출 패턴과 서술 풀이", "Predicted grade를 위한 내부 시험 대비"],
     }},
    {"key": "english", "name": "영어·에세이", "icon": "A",
     "desc": "교과 영어(문학·언어)와 학업용 영어 글쓰기를 함께 봅니다.",
     "by": {
        "ibdp":  ["English A Language & Literature / Literature 과제 구조", "Individual Oral(IO)·Paper 1 분석 글쓰기", "EE·TOK 에세이 논리 점검"],
        "igcse": ["First Language / Second Language English 코스 구분", "Reading·Writing·Speaking 영역별 채점 기준", "요약·논설문 쓰기 패턴 연습"],
        "ap":    ["AP English Language / Literature 선택 기준", "Rhetorical analysis·argument essay 구조", "수업 내 토론·발표용 학업 영어"],
        "alevel":["English Literature 텍스트 분석 에세이", "비교 에세이 구조와 인용 방식", "시험용 타임드 에세이 연습"],
     }},
    {"key": "science", "name": "과학", "icon": "⚗",
     "desc": "물리·화학·생물 가운데 선택한 과목을 교육과정 형식에 맞춰 지도합니다.",
     "by": {
        "ibdp":  ["Physics·Chemistry·Biology HL/SL 범위 정리", "Internal Assessment 실험 설계와 보고서", "Data-based question 접근법"],
        "igcse": ["Combined / Coordinated / 단일 과학 코스 구분", "Practical·Alternative to Practical 문항 대비", "용어 정의 암기와 서술형 답안"],
        "ap":    ["AP Physics 1·Chemistry·Biology 단원별 핵심", "Lab 기반 Free Response 서술", "수식·그래프 해석 훈련"],
        "alevel":["AS·A2 단계별 범위와 Practical 평가", "서술형 채점 기준(mark scheme) 분석", "기출 반복과 오답 정리"],
     }},
    {"key": "admission", "name": "입학 준비", "icon": "✓",
     "desc": "학교 공식 입학 안내에 적힌 전형만 기준으로 준비 방향을 상담합니다. 합격 보장이나 내부 자료 보유를 말하지 않습니다.",
     "by": {
        "ibdp":  ["지원 학년의 공식 전형 절차 확인", "영어·수학 평가가 있는 경우 범위 점검", "인터뷰가 있는 경우 말하기 연습"],
        "igcse": ["영국식 Year 배정과 한국 학년 차이 확인", "지원 학년의 공식 평가 항목 점검", "전환 시 과목 선택 상담"],
        "ap":    ["지원 자격(국적·해외 체류 등) 공식 요건 확인", "제출 서류와 성적표 준비", "영어 평가·인터뷰가 있는 경우 준비"],
        "alevel":["AS 진입 전 과목 선택 상담", "지원 학년 공식 전형 확인", "영어 평가 대비"],
     }},
]
