# Assets - 에셋 폴더 설명

## 개요

이 폴더는 CGD AI Career Platform에서 사용하는 모든 에셋 파일을 관리합니다.

---

## 폴더 구조

```
assets/
├── README.md              ← 이 파일
├── images/
│   ├── logo/              ← 플랫폼 로고 파일
│   │   ├── logo.svg       ← 벡터 로고
│   │   ├── logo.png       ← PNG 로고 (512×512)
│   │   └── logo-dark.png  ← 다크 배경용 로고
│   │
│   ├── docs/              ← 문서에 사용되는 이미지
│   │   ├── git-workflow.png
│   │   ├── mcp-setup.png
│   │   └── platform-screenshot.png
│   │
│   └── examples/          ← 예제 포트폴리오 이미지 (익명화)
│       ├── portfolio-sample-01.jpg
│       └── portfolio-sample-02.jpg
│
├── templates/             ← InDesign/Figma 템플릿 파일
│   ├── portfolio-template.indd
│   ├── resume-template.docx
│   └── business-card-template.ai
│
├── fonts/                 ← 교육에 사용되는 폰트 (라이센스 확인 필수)
│   ├── NotoSansKR/
│   └── NotoSerifKR/
│
└── icons/                 ← 아이콘 모음
    ├── social/
    └── tools/
```

---

## 에셋 사용 규칙

### 이미지 파일

| 용도 | 권장 형식 | 크기 |
|------|---------|------|
| 문서 내 스크린샷 | PNG | 1920×1080 이하 |
| 포트폴리오 예제 | JPG | 2480×3508 (A4 300dpi) |
| 웹 사용 이미지 | WebP/PNG | 1200px 이하 |
| 로고 | SVG | 벡터 |

### 파일명 규칙

```
[카테고리]-[설명]-[크기].[확장자]

예시:
docs-git-workflow-1920w.png
portfolio-sample-branding-a4.jpg
icon-github-32px.svg
```

---

## 에셋 추가 방법

### 1. 이미지 추가

```bash
# 이미지 최적화 후 추가
# Mac의 경우 ImageOptim 사용
# Windows의 경우 squoosh.app 사용

# 크기 확인 (5MB 이하 권장)
ls -lh assets/images/

# Git에 추가
git add assets/images/새파일.png
git commit -m "assets: 플랫폼 스크린샷 추가"
```

### 2. 폰트 추가

```
폰트 추가 전 반드시 확인:
[ ] 상업적 사용 가능 여부
[ ] OFL (Open Font License) 또는 무료 라이센스
[ ] 라이센스 파일 함께 포함

권장 무료 한글 폰트:
- Noto Sans KR (Google Fonts)
- Noto Serif KR (Google Fonts)
- Pretendard (OFL 라이센스)
- Spoqa Han Sans Neo (OFL)
```

---

## 저작권 주의사항

```
주의! 다음 파일은 절대 업로드 금지:
- 구매한 상용 폰트 파일
- 유료 이미지 (셔터스톡, Getty 등)
- 학생 포트폴리오 (동의 없이)
- 기업 로고 (법적 분쟁 가능)

사용 가능:
- GPL/OFL 라이센스 폰트
- CC0 또는 퍼블릭 도메인 이미지
- Unsplash, Pexels 등 무료 이미지 (라이센스 확인)
- 직접 제작한 에셋
```

---

## 에셋 최적화 도구

| 도구 | 용도 | URL |
|------|------|-----|
| Squoosh | 이미지 압축 | squoosh.app |
| SVG OMG | SVG 최적화 | jakearchibald.github.io/svgomg |
| ImageOptim | Mac 이미지 최적화 | imageoptim.com |
| TinyPNG | PNG/JPG 압축 | tinypng.com |

---

*CGD AI Career Platform - assets/README.md*
