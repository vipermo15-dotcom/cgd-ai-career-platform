# 02. GitHub 사용법

> GitHub를 활용하여 포트폴리오를 관리하고 취업 준비를 완성합니다.

---

## 목차

1. [GitHub 계정 생성](#1-github-계정-생성)
2. [Repository 만들기](#2-repository-만들기)
3. [Fork와 Clone](#3-fork와-clone)
4. [Pull Request 개념](#4-pull-request-개념)
5. [Issues 활용법](#5-issues-활용법)
6. [GitHub Pages 소개](#6-github-pages-소개)
7. [GitHub Projects로 취업 관리](#7-github-projects로-취업-관리)
8. [프로필 꾸미기 (취업 포트폴리오)](#8-프로필-꾸미기-취업-포트폴리오)

---

## 1. GitHub 계정 생성

### 가입 절차

1. [github.com](https://github.com) 접속
2. "Sign up" 클릭
3. 정보 입력:
   - **Email**: 주로 사용하는 이메일 주소
   - **Password**: 8자 이상, 숫자+소문자 포함
   - **Username**: 영문+숫자+하이픈만 가능
4. 이메일 인증 코드 입력
5. 계정 유형: "Free" 선택

### 사용자명(Username) 선택 팁

GitHub 사용자명은 포트폴리오 URL로 사용됩니다.  
예: `https://github.com/[사용자명]`

**좋은 사용자명 예시**:
- `kimminsu-design` (이름 + 직군)
- `parkgraphic` (이름 + 분야)
- `leeui2024` (이름 + 연도)

**피해야 할 사용자명**:
- `aaaa1234` (기억하기 어려움)
- `cutegirl99` (비전문적)
- `abcdef` (정체성 없음)

### 2단계 인증 설정 (보안)

1. 우상단 프로필 사진 → Settings
2. Password and authentication
3. Two-factor authentication → Enable
4. Google Authenticator 앱 연동 (권장)

---

## 2. Repository 만들기

### 새 Repository 생성

1. 우상단 `+` 버튼 → "New repository"
2. 설정 항목:

| 항목 | 설명 | 권장값 |
|------|------|--------|
| Repository name | 저장소 이름 | `cgd-portfolio` |
| Description | 설명 | `CGD과 포트폴리오 및 취업 준비` |
| Public/Private | 공개 여부 | Public (포트폴리오 목적) |
| Add a README file | README 자동 생성 | 체크 |
| Add .gitignore | 불필요 파일 제외 | None (나중에 추가) |
| Choose a license | 라이선스 | MIT License |

3. "Create repository" 클릭

### Repository 구성 요소

```
저장소 메인 페이지
├── Code 탭          : 파일 목록, 코드 확인
├── Issues 탭        : 버그 신고, 개선 요청
├── Pull requests 탭 : PR 목록
├── Actions 탭       : 자동화 워크플로우
├── Projects 탭      : 칸반 보드 (일정 관리)
├── Settings 탭      : 저장소 설정
└── Insights 탭      : 통계 및 기여자 정보
```

### README.md 작성

README.md는 저장소의 첫인상입니다. 취업 포트폴리오 저장소의 README 예시:

```markdown
# 홍길동 디자인 포트폴리오

서울시기술교육원 컴퓨터그래픽디자인과 교육생의 포트폴리오입니다.

## 보유 기술
- Adobe Photoshop, Illustrator, InDesign
- Figma (UI/UX 디자인)
- After Effects (모션 그래픽)

## 주요 프로젝트
1. [브랜드 아이덴티티 프로젝트](link)
2. [앱 UI 디자인 프로젝트](link)

## 연락처
- Email: honggildong@email.com
- Behance: behance.net/honggildong
```

---

## 3. Fork와 Clone

### Fork (포크)

Fork는 다른 사람의 저장소를 본인 계정으로 복사하는 기능입니다.

**언제 사용하나요?**
- 공개 저장소를 본인 계정에 복사하여 수정하고 싶을 때
- 오픈소스 프로젝트에 기여하고 싶을 때
- 이 CGD 플랫폼을 본인 계정에서 관리하고 싶을 때

**Fork 방법**:
1. Fork하고 싶은 저장소 접속
2. 우상단 "Fork" 버튼 클릭
3. 본인 계정 선택 → "Create fork"
4. 본인 계정에 복사된 저장소 확인

### Clone (클론)

Clone은 GitHub의 저장소를 로컬 컴퓨터로 복사하는 명령어입니다.

```bash
# HTTPS 방식 (권장, 초보자)
git clone https://github.com/사용자명/저장소명.git

# CGD 플랫폼 Clone 예시
git clone https://github.com/cgd-ai/cgd-ai-career-platform.git
```

### Fork 후 원본과 동기화

Fork한 저장소는 원본이 업데이트되어도 자동으로 반영되지 않습니다.

```bash
# 원본 저장소를 upstream으로 추가
git remote add upstream https://github.com/cgd-ai/cgd-ai-career-platform.git

# 원본 저장소의 최신 변경사항 가져오기
git fetch upstream

# 로컬 main 브랜치에 병합
git merge upstream/main

# 본인 GitHub 저장소에도 반영
git push origin main
```

---

## 4. Pull Request 개념

### Pull Request (PR)란?

Pull Request는 "내가 수정한 내용을 원본 저장소에 반영해달라"는 요청입니다.

### PR 생성 과정

```
내 Fork 저장소에서 수정
    ↓
Branch 생성
    ↓
파일 수정 후 Commit
    ↓
GitHub에 Push
    ↓
Pull Request 생성 (원본 저장소에 요청)
    ↓
리뷰 및 토론
    ↓
Merge (승인 후 원본에 반영)
```

### 실제 PR 생성 방법

```bash
# 1. Fork한 저장소 Clone
git clone https://github.com/본인계정/cgd-ai-career-platform.git
cd cgd-ai-career-platform

# 2. 새 브랜치 생성
git checkout -b fix/오탈자-수정

# 3. 파일 수정 후 커밋
git add docs/01-Git설치.md
git commit -m "fix: 01-Git설치 오탈자 수정"

# 4. Push
git push origin fix/오탈자-수정
```

5. GitHub에서 `Compare & pull request` 버튼 클릭
6. 제목과 설명 작성
7. `Create pull request` 클릭

---

## 5. Issues 활용법

### Issues란?

Issues는 버그 신고, 기능 요청, 질문 등을 관리하는 공간입니다.

**취업 준비에서 활용**:
- 포트폴리오 개선 사항 기록
- 취업 지원 현황 추적
- 학습 목표 설정

### Issue 생성 방법

1. 저장소 → "Issues" 탭
2. "New issue" 클릭
3. 제목 및 내용 작성
4. Labels 설정 (bug, enhancement, question 등)
5. Assignees 설정 (담당자)
6. Submit 클릭

### Issue 레이블 (Labels) 활용

| 레이블 | 색상 | 용도 |
|--------|------|------|
| `취업준비` | 파란색 | 취업 관련 이슈 |
| `포트폴리오` | 초록색 | 포트폴리오 개선 |
| `자기소개서` | 노란색 | 자기소개서 관련 |
| `기업분석` | 빨간색 | 기업 조사 |
| `완료` | 회색 | 완료된 이슈 |

### Issue를 Todo로 활용하기

```markdown
## 이번 주 취업 준비 목표

- [x] 포트폴리오 표지 디자인 수정
- [ ] 자기소개서 2차 첨삭 요청
- [ ] A사 기업분석 보고서 작성
- [ ] B사 채용공고 분석
- [ ] 모의 면접 준비 (Claude 활용)
```

---

## 6. GitHub Pages 소개

### GitHub Pages란?

GitHub Pages는 저장소의 파일을 웹사이트로 호스팅하는 무료 서비스입니다.

**활용 방법**:
- 포트폴리오 웹사이트 무료 호스팅
- 이력서 웹 버전 배포
- 프로젝트 소개 페이지

### GitHub Pages 설정 방법

1. 저장소 → Settings
2. 왼쪽 메뉴에서 "Pages"
3. Source: "Deploy from a branch"
4. Branch: `main` → `/ (root)` → Save
5. 몇 분 후 `https://[사용자명].github.io/[저장소명]` 에서 확인

### 포트폴리오 페이지 예시

`index.html` 파일을 저장소 루트에 생성:

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>홍길동 포트폴리오</title>
    <style>
        body { font-family: 'Malgun Gothic', sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1 { color: #333; }
        .project { border: 1px solid #ddd; padding: 20px; margin: 10px 0; border-radius: 8px; }
    </style>
</head>
<body>
    <h1>홍길동 디자인 포트폴리오</h1>
    <p>서울시기술교육원 컴퓨터그래픽디자인과</p>
    
    <h2>주요 프로젝트</h2>
    <div class="project">
        <h3>브랜드 아이덴티티 프로젝트</h3>
        <p>카페 브랜드 로고 및 아이덴티티 디자인</p>
    </div>
</body>
</html>
```

---

## 7. GitHub Projects로 취업 관리

### 취업 현황 관리 보드 만들기

1. 저장소 → "Projects" 탭
2. "New project" → "Board" 선택
3. 컬럼 구성:

| 컬럼 | 내용 |
|------|------|
| 기업 리서치 | 관심 기업 목록 |
| 지원 준비 중 | 서류 작성 중 |
| 지원 완료 | 지원서 제출 완료 |
| 서류 통과 | 서류 합격 |
| 면접 예정 | 면접 일정 확정 |
| 최종 결과 | 합격/불합격 |

4. 각 기업을 카드로 추가하여 진행 상황 추적

---

## 8. 프로필 꾸미기 (취업 포트폴리오)

### GitHub 프로필 README 만들기

사용자명과 동일한 저장소를 만들면 프로필 페이지에 README가 표시됩니다.

```bash
# 예: 사용자명이 kimminsu인 경우
# kimminsu/kimminsu 저장소를 생성하면 프로필에 표시됨
```

### 프로필 README 예시

```markdown
# 안녕하세요, 김민수입니다 👋

서울시기술교육원 컴퓨터그래픽디자인과 교육생입니다.

## 🎨 보유 기술
![Photoshop](https://img.shields.io/badge/Photoshop-31A8FF?style=flat&logo=adobe-photoshop&logoColor=white)
![Illustrator](https://img.shields.io/badge/Illustrator-FF9A00?style=flat&logo=adobe-illustrator&logoColor=white)
![Figma](https://img.shields.io/badge/Figma-F24E1E?style=flat&logo=figma&logoColor=white)

## 📊 GitHub 통계
![GitHub stats](https://github-readme-stats.vercel.app/api?username=kimminsu&show_icons=true&theme=default)

## 📫 연락처
- Email: kimminsu@email.com
- Behance: [behance.net/kimminsu](https://behance.net/kimminsu)
```

### Contribution 잔디 심기

매일 GitHub에 커밋을 하면 프로필에 녹색 잔디가 생깁니다.  
학습 일지를 매일 커밋하는 것이 취업에 유리합니다.

```bash
# 매일 학습 일지 커밋 예시
echo "## $(date '+%Y-%m-%d') 학습 내용\n\n- Claude로 자기소개서 첨삭\n- 기업 A 홈페이지 분석" >> 학습일지.md
git add 학습일지.md
git commit -m "docs: $(date '+%Y-%m-%d') 학습 일지"
git push origin main
```

---

*이전 문서: [01-Git설치.md](01-Git설치.md) | 다음 문서: [03-VSCode.md](03-VSCode.md) →*
