# GitHub 저장소 운영 가이드 - 교수자용

## 개요
cgd-ai-career-platform 저장소를 효율적으로 운영하고 학생 과제를 관리하는 방법입니다.

---

## 1. 저장소 관리 방법

### 1.1 저장소 구조 원칙

```
main 브랜치: 배포용 (항상 안정적이어야 함)
develop 브랜치: 개발/업데이트 작업용
feature/* 브랜치: 새 기능 추가용
student/* 브랜치: 학생 과제 제출용
```

### 1.2 정기 관리 작업

**매주 금요일**
```bash
# 학생 PR 검토 및 병합
git checkout main
git pull origin main

# 이번 주 업데이트된 내용 확인
git log --oneline --since="1 week ago"

# 미병합 PR 목록 확인
gh pr list --state open
```

**매월 1일**
```bash
# Release 태그 생성
git tag -a v2026.01 -m "2026년 1월 업데이트"
git push origin v2026.01

# CHANGELOG 업데이트
# docs/CHANGELOG.md에 이번 달 변경사항 추가
```

---

## 2. 브랜치 전략

### 2.1 Gitflow 기반 운영

```
main
├── develop
│   ├── feature/update-week05-materials
│   ├── feature/add-company-db
│   └── feature/new-firecrawl-scripts
│
└── hotfix/typo-week03-readme
```

### 2.2 브랜치 명명 규칙

```
feature/내용-설명      - 새 기능 또는 자료 추가
update/파일명-변경내용  - 기존 자료 업데이트
fix/버그내용           - 오류 수정
student/학번-과제명     - 학생 과제 브랜치
```

---

## 3. 학생 과제 PR 관리

### 3.1 PR 검토 기준

```markdown
## PR 체크리스트 (교수자용)

기본 확인:
[ ] 파일명이 규칙에 맞는가 (예: week01_홍길동.md)
[ ] 내용이 충분한가 (최소 분량 충족)
[ ] Markdown 문법 오류 없는가
[ ] 커밋 메시지가 명확한가

내용 평가:
[ ] 미션 요구사항을 모두 충족했는가
[ ] AI 도구를 활용한 흔적이 있는가
[ ] 개인적인 생각/분석이 담겨있는가
[ ] 다음 주를 위한 준비가 되었는가
```

### 3.2 PR 피드백 작성 예시

```markdown
## Week01 미션 피드백 - 홍길동

**잘한 점:**
- README.md 구성이 깔끔하고 정보가 충분합니다
- 커밋 메시지를 규칙에 맞게 작성했습니다 (feat:, docs: 등)
- 도전 미션(브랜치 생성)까지 완료했습니다

**개선할 점:**
- 자기소개에 '목표 기업' 항목을 추가하면 좋겠습니다
- 보유 스킬 섹션에 숙련도(★☆ 형식)를 추가해보세요
- 다음 커밋부터는 `git commit -S` 로 서명을 추가해보세요

**점수**: 88점 / 100점

다음 주도 파이팅! 💪
```

---

## 4. GitHub Issues 활용

### 4.1 학생 지원 이슈 트래킹

```markdown
## Issue 템플릿: 학생 지원 요청

**학생 이름**: 홍길동
**Week**: 04
**문제 내용**: MCP 설치 시 "npx not found" 오류 발생

**시도한 해결책**:
1. Node.js 재설치
2. PATH 환경변수 확인

**필요한 지원**: 원격 지원 또는 추가 가이드 요청

**긴급도**: 높음 (다음 수업까지 해결 필요)
```

---

*CGD AI Career Platform - instructors/05-GitHub운영.md*
