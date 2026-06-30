# 07. GitHub Projects 활용 - 취업 준비 현황 관리

> GitHub Projects로 취업 준비 현황을 체계적으로 관리합니다.

---

## 목차

1. [GitHub Projects란?](#1-github-projects란)
2. [취업 준비 보드 만들기](#2-취업-준비-보드-만들기)
3. [기업 지원 현황 관리](#3-기업-지원-현황-관리)
4. [학습 진도 관리](#4-학습-진도-관리)
5. [팀 협업 활용법](#5-팀-협업-활용법)
6. [자동화 설정](#6-자동화-설정)

---

## 1. GitHub Projects란?

GitHub Projects는 칸반(Kanban) 보드 방식으로 작업을 관리하는 기능입니다.

### 특징

- **무료**: 개인 계정에서 무료로 사용 가능
- **연동**: GitHub Issues, PR과 연동
- **필터링**: 라벨, 담당자, 날짜 기준 필터
- **뷰 다양성**: 보드, 테이블, 로드맵 뷰 지원
- **자동화**: 상태 변경 자동화 가능

### 취업 준비에서의 활용

| 용도 | 설명 |
|------|------|
| 기업 지원 현황 | 지원 → 서류통과 → 면접 → 결과 추적 |
| 학습 진도 | Week01~20 진행 상황 |
| 포트폴리오 작업 | 각 작업물 제작 진행 상황 |
| 취업 준비 체크리스트 | 항목별 완료 여부 |

---

## 2. 취업 준비 보드 만들기

### 프로젝트 생성

1. GitHub 프로필 → "Projects" 탭
2. "New project" 클릭
3. 템플릿 선택: "Board" (칸반 보드)
4. 이름 입력: `CGD 취업 준비 현황`
5. "Create project" 클릭

### 기본 컬럼 구성

| 컬럼 이름 | 내용 | 아이콘 |
|-----------|------|--------|
| 관심 기업 | 지원 고려 중인 기업 | 👀 |
| 서류 준비 | 자기소개서·포트폴리오 작성 중 | ✍️ |
| 지원 완료 | 서류 제출 완료 | 📤 |
| 서류 합격 | 서류 통과, 면접 대기 | ✅ |
| 면접 예정 | 면접 일정 확정 | 📅 |
| 면접 완료 | 면접 진행 완료, 결과 대기 | ⏳ |
| 최종 합격 | 최종 합격 | 🎉 |
| 불합격 | 불합격 (분석 및 재도전) | 📝 |

### 컬럼 생성 방법

1. 보드 우측 `+` 버튼 클릭
2. 컬럼 이름 입력
3. "Save" 클릭
4. 필요한 컬럼 모두 생성

---

## 3. 기업 지원 현황 관리

### 기업 카드 만들기

**방법 1: 직접 카드 추가**
1. 컬럼 하단 `+ Add item` 클릭
2. 기업명 입력 (예: `카카오 - 그래픽 디자이너`)
3. Enter로 생성

**방법 2: Issue로 생성 (상세 정보 포함)**
1. Issues → "New issue"
2. 제목: `[카카오] 브랜드 디자이너 지원`
3. 내용 작성:

```markdown
## 기업 정보
- **회사명**: 카카오
- **직무**: 브랜드 디자이너
- **공고 URL**: https://careers.kakao.com/...
- **마감일**: 2024년 XX월 XX일
- **연봉**: 협의

## 지원 요건
- 필수: Adobe CC 2년 이상, 브랜딩 경험
- 우대: UI 디자인 경험, 모션 그래픽

## 내 매칭 점수
- 필수 자격: 70%
- 우대 사항: 50%
- 전반적 매칭: 60%

## 준비 사항
- [ ] 자기소개서 작성
- [ ] 포트폴리오 브랜딩 섹션 강화
- [ ] 기업 분석 완료
- [ ] 모의 면접 준비

## Claude 분석 메모
(기업 분석 내용 붙여넣기)
```

### 카드 이동 방법

- 드래그 앤 드롭으로 컬럼 간 이동
- 카드 클릭 후 상태 변경

### 우선순위 설정

카드에 라벨을 추가하여 우선순위를 시각화:
- 🔴 `최우선`: 마감 임박 또는 가장 원하는 기업
- 🟡 `중요`: 좋은 조건의 기업
- 🟢 `일반`: 일반 지원

---

## 4. 학습 진도 관리

### 학습 진도 보드 만들기

별도 프로젝트 생성: `CGD 학습 진도`

**컬럼 구성**:
```
미시작 | 학습 중 | 실습 중 | 완료 | 복습 필요
```

**주차별 카드 생성 예시**:

```markdown
## Week01: 오리엔테이션 + Git/GitHub

### 완료 목표
- [x] GitHub 계정 생성
- [x] 저장소 Fork
- [ ] Git 설치
- [ ] 첫 커밋 생성
- [ ] Claude 가입

### 메모
- Git Bash 설치 시 경로 설정 주의
- 커밋 메시지 컨벤션 기억할 것

### 다음 주 준비
- VSCode 설치 시작하기
```

### 학습 체크리스트 연동

GitHub Issue를 학습 체크리스트로 활용:

```bash
# Week01 학습 체크리스트 Issue 생성
gh issue create --title "Week01 학습 체크리스트" \
  --body "- [ ] GitHub 계정 생성
- [ ] Fork 완료
- [ ] Git 설치
- [ ] VSCode 설치
- [ ] 첫 커밋
- [ ] Claude 가입"
```

---

## 5. 팀 협업 활용법

### 그룹 스터디 보드

같이 취업 준비하는 동기들과 보드를 공유할 수 있습니다.

**공유 방법**:
1. Project 설정 → "Manage access"
2. "Invite" → 동기 GitHub 계정 입력
3. 권한 설정: Read (보기) 또는 Write (편집)

### 포트폴리오 리뷰 시스템

```markdown
## 포트폴리오 리뷰 요청

### 작업 정보
- **작업명**: 카페 브랜드 아이덴티티
- **사용 툴**: Adobe Illustrator, Photoshop
- **제작 기간**: 1주일
- **파일 링크**: (Behance 또는 Google Drive 링크)

### 리뷰 요청 사항
1. 전체적인 디자인 완성도
2. 브랜드 컬러 선택의 적절성
3. 타이포그래피 사용
4. 포트폴리오 발표용으로 적합한지

### 피드백 기록
(리뷰어가 여기에 피드백 작성)
```

---

## 6. 자동화 설정

### 상태 변경 자동화

Project 설정 → "Workflows"에서 자동화 규칙 설정:

**자동화 규칙 예시**:
- Issue가 `closed` 되면 → 해당 카드를 "완료" 컬럼으로 이동
- PR이 `merged` 되면 → 관련 카드를 "완료"로 이동
- Issue에 `면접` 라벨 추가 시 → "면접 예정" 컬럼으로 이동

### GitHub Actions와 연동

```yaml
# .github/workflows/update-project.yml
name: Update Project Status

on:
  issues:
    types: [labeled]

jobs:
  update-project:
    runs-on: ubuntu-latest
    steps:
      - name: Move to interview column
        if: github.event.label.name == '면접예정'
        uses: actions/github-script@v7
        with:
          script: |
            // Project 카드 이동 로직
            console.log('면접 예정 라벨 추가됨');
```

### 주간 취업 현황 요약 알림

```python
# 매주 월요일 현황 요약 생성 스크립트
import requests
from datetime import datetime

GITHUB_TOKEN = "ghp_xxxxxxxx"
REPO_OWNER = "본인계정"
REPO_NAME = "cgd-ai-career-platform"

headers = {"Authorization": f"token {GITHUB_TOKEN}"}

# Issues 목록 가져오기
response = requests.get(
    f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues",
    headers=headers,
    params={"labels": "취업준비", "state": "open"}
)

issues = response.json()

print(f"\n=== {datetime.now().strftime('%Y년 %m월 %d일')} 취업 준비 현황 ===")
print(f"진행 중인 기업 지원: {len(issues)}개")

for issue in issues:
    labels = [l['name'] for l in issue['labels']]
    print(f"- {issue['title']}: {', '.join(labels)}")
```

---

## 빠른 시작 체크리스트

- [ ] GitHub Projects 접속
- [ ] "CGD 취업 준비 현황" 프로젝트 생성
- [ ] 8개 컬럼 생성
- [ ] 관심 기업 5개 카드 추가
- [ ] 각 카드에 마감일, 지원 요건 정보 입력
- [ ] 우선순위 라벨 설정

---

*이전 문서: [06-Firecrawl.md](06-Firecrawl.md) | 다음 문서: [08-Markdown.md](08-Markdown.md) →*
