# 01. Git 설치 및 기본 명령어

> Git을 설치하고 첫 커밋을 만들어봅니다.

---

## 목차

1. [Git이란?](#1-git이란)
2. [Git 설치 방법](#2-git-설치-방법)
3. [Git 초기 설정](#3-git-초기-설정)
4. [기본 명령어 완전 정복](#4-기본-명령어-완전-정복)
5. [실습: 첫 커밋 만들기](#5-실습-첫-커밋-만들기)
6. [자주 발생하는 오류와 해결법](#6-자주-발생하는-오류와-해결법)

---

## 1. Git이란?

### 버전 관리 시스템 (Version Control System)

Git은 파일의 변경 이력을 관리하는 도구입니다.

**비유로 이해하기**: 포토샵 작업을 할 때 다음과 같은 경험이 있으신가요?
- `포트폴리오_최종.psd`
- `포트폴리오_최종2.psd`
- `포트폴리오_진짜최종.psd`
- `포트폴리오_진짜진짜최종_수정.psd`

Git을 사용하면 이런 파일명 혼란 없이 변경 이력을 깔끔하게 관리할 수 있습니다.

### Git의 핵심 개념

| 개념 | 설명 | 비유 |
|------|------|------|
| Repository (저장소) | 파일과 이력을 저장하는 공간 | 프로젝트 폴더 |
| Commit (커밋) | 변경사항을 저장하는 단위 | 저장 포인트 |
| Branch (브랜치) | 독립적인 작업 공간 | 작업 복사본 |
| Merge (병합) | 브랜치를 합치는 과정 | 파일 합치기 |
| Clone (클론) | 원격 저장소를 로컬로 복사 | 다운로드 |
| Push (푸시) | 로컬 변경사항을 원격으로 업로드 | 업로드 |
| Pull (풀) | 원격 변경사항을 로컬로 다운로드 | 동기화 |

### Git vs GitHub 차이

- **Git**: 내 컴퓨터에 설치하는 버전 관리 프로그램 (도구)
- **GitHub**: Git 저장소를 온라인으로 관리하는 플랫폼 (서비스)

---

## 2. Git 설치 방법

### Windows 설치

**방법 1: 공식 홈페이지 설치 (권장)**

1. 브라우저에서 [git-scm.com](https://git-scm.com) 접속
2. "Download for Windows" 버튼 클릭
3. 다운로드된 `.exe` 파일 실행
4. 설치 마법사 진행:
   - **Select Components**: 기본값 그대로 (변경 불필요)
   - **Choosing the default editor**: "Use Visual Studio Code as Git's default editor" 선택 (VSCode 설치 후)
   - **Adjusting the name of the initial branch**: "Override the default branch name for new repositories" 선택, `main` 입력
   - **Adjusting your PATH environment**: "Git from the command line and also from 3rd-party software" 선택
   - **Choosing HTTPS transport backend**: "Use the OpenSSL library" 선택
   - **Configuring the line ending conversions**: "Checkout Windows-style, commit Unix-style line endings" 선택
   - 나머지는 기본값으로 Next 클릭
5. "Install" 클릭하여 설치 완료

**설치 확인**:
```bash
# 시작 메뉴에서 "Git Bash" 실행 후 입력
git --version
# 출력 예시: git version 2.43.0.windows.1
```

### macOS 설치

**방법 1: Homebrew 사용 (권장)**

터미널 앱을 열고 순서대로 입력:

```bash
# Homebrew 설치 (이미 설치된 경우 건너뜀)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Git 설치
brew install git

# 설치 확인
git --version
```

**방법 2: Xcode Command Line Tools 사용**

```bash
# 터미널에서 입력
xcode-select --install
# 팝업 창에서 "Install" 클릭
```

**방법 3: 공식 홈페이지 설치**

1. [git-scm.com](https://git-scm.com) 접속
2. macOS용 다운로드 클릭
3. `.dmg` 파일 실행 후 설치

---

## 3. Git 초기 설정

Git을 처음 설치한 후 반드시 이름과 이메일을 설정해야 합니다.

### 사용자 정보 설정

```bash
# 사용자 이름 설정 (GitHub 사용자명과 동일하게 설정 권장)
git config --global user.name "홍길동"

# 이메일 설정 (GitHub 가입 이메일과 동일하게 설정)
git config --global user.email "honggildong@email.com"

# 기본 브랜치 이름을 'main'으로 설정
git config --global init.defaultBranch main

# Windows에서 줄바꿈 문제 방지
git config --global core.autocrlf true  # Windows
git config --global core.autocrlf input # macOS/Linux

# 설정 확인
git config --list
```

### VS Code를 기본 편집기로 설정

```bash
git config --global core.editor "code --wait"
```

### 설정 파일 위치

설정은 `~/.gitconfig` 파일에 저장됩니다:

```
[user]
    name = 홍길동
    email = honggildong@email.com
[core]
    editor = code --wait
    autocrlf = true
[init]
    defaultBranch = main
```

---

## 4. 기본 명령어 완전 정복

### 저장소 초기화 및 복사

```bash
# 새 저장소 초기화 (현재 폴더를 Git 저장소로 만들기)
git init

# 원격 저장소 복사
git clone https://github.com/사용자명/저장소명.git

# 특정 폴더명으로 Clone
git clone https://github.com/사용자명/저장소명.git 폴더명
```

### 상태 확인

```bash
# 현재 상태 확인 (가장 자주 사용)
git status

# 변경 내용 상세 확인
git diff

# 커밋 이력 확인
git log

# 한 줄로 간략하게 이력 확인
git log --oneline

# 그래프 형태로 이력 확인
git log --oneline --graph --all
```

### 파일 스테이징 (Staging Area)

```bash
# 특정 파일 스테이징
git add 파일명.md

# 현재 폴더의 모든 변경 파일 스테이징
git add .

# 특정 폴더 스테이징
git add docs/

# 스테이징 취소
git restore --staged 파일명.md
```

### 커밋 (저장)

```bash
# 커밋 (메시지 포함)
git commit -m "커밋 메시지"

# 예시 커밋 메시지
git commit -m "docs: 포트폴리오 초안 작성"
git commit -m "feat: 자기소개서 1차 완성"
git commit -m "fix: 오탈자 수정"
```

### 원격 저장소 연동

```bash
# 원격 저장소 연결
git remote add origin https://github.com/사용자명/저장소명.git

# 원격 저장소 확인
git remote -v

# 원격 저장소로 Push (업로드)
git push origin main

# 처음 Push할 때 (기본 브랜치 설정 포함)
git push -u origin main

# 원격 저장소에서 Pull (다운로드·동기화)
git pull origin main
```

### 브랜치 관리

```bash
# 현재 브랜치 확인
git branch

# 모든 브랜치 확인 (원격 포함)
git branch -a

# 새 브랜치 생성
git branch 브랜치명

# 브랜치 전환
git checkout 브랜치명

# 브랜치 생성과 동시에 전환
git checkout -b 브랜치명

# 브랜치 병합
git merge 브랜치명

# 브랜치 삭제
git branch -d 브랜치명
```

---

## 5. 실습: 첫 커밋 만들기

### 목표
GitHub에 나만의 저장소를 만들고 첫 파일을 커밋해봅니다.

### 단계별 실습

**Step 1: GitHub에 새 저장소 생성**

1. GitHub 로그인 → 우상단 `+` 버튼 → `New repository`
2. Repository name: `cgd-portfolio` (원하는 이름으로 변경 가능)
3. Description: `서울시기술교육원 CGD과 포트폴리오`
4. Public 선택
5. "Add a README file" 체크
6. `Create repository` 클릭

**Step 2: 로컬로 Clone**

```bash
# 터미널 또는 Git Bash 실행
git clone https://github.com/[본인계정]/cgd-portfolio.git

# 폴더 이동
cd cgd-portfolio

# 현재 상태 확인
git status
```

**Step 3: 파일 만들기**

텍스트 편집기(VSCode)에서 다음 파일을 생성합니다.

파일명: `자기소개.md`

```markdown
# 나의 자기소개

## 기본 정보
- 이름: [본인 이름]
- 교육과정: 서울시기술교육원 컴퓨터그래픽디자인과
- 목표 직종: [디자이너/UI-UX/그래픽 등]

## 보유 기술
- Adobe Photoshop
- Adobe Illustrator
- [기타 보유 기술]

## 목표
취업 준비를 위해 이 저장소를 활용하겠습니다.
```

**Step 4: 파일 스테이징 및 커밋**

```bash
# 파일 추가
git add 자기소개.md

# 상태 확인
git status
# 출력: Changes to be committed: new file: 자기소개.md

# 커밋
git commit -m "docs: 자기소개 파일 추가"

# 이력 확인
git log --oneline
```

**Step 5: GitHub로 Push**

```bash
git push origin main

# GitHub 저장소 페이지에서 파일 확인
# https://github.com/[본인계정]/cgd-portfolio
```

---

## 6. 자주 발생하는 오류와 해결법

### 오류 1: `fatal: not a git repository`

```
fatal: not a git repository (or any of the parent directories): .git
```

**원인**: git 저장소로 초기화되지 않은 폴더에서 명령어 실행

**해결**:
```bash
# 현재 위치 확인
pwd

# Git 저장소 폴더로 이동
cd [저장소 폴더명]

# 또는 현재 폴더를 저장소로 초기화
git init
```

### 오류 2: `Permission denied (publickey)`

```
Permission denied (publickey).
fatal: Could not read from remote repository.
```

**원인**: SSH 키 미설정 또는 HTTPS 인증 필요

**해결**:
```bash
# HTTPS 방식으로 Clone (권장)
git clone https://github.com/사용자명/저장소명.git

# GitHub Personal Access Token 사용
# GitHub → Settings → Developer settings → Personal access tokens → Generate new token
```

### 오류 3: `Updates were rejected`

```
! [rejected] main -> main (fetch first)
error: failed to push some refs
```

**원인**: 원격 저장소에 로컬보다 최신 커밋이 있음

**해결**:
```bash
# 먼저 Pull (동기화)
git pull origin main

# 충돌(Conflict)이 없으면 다시 Push
git push origin main
```

### 오류 4: 커밋 메시지 편집기가 열릴 때

```bash
# 편집기가 열리면 i 키로 입력 모드 진입
# 메시지 입력 후 Esc 키
# :wq 입력 후 Enter (저장 후 종료)

# 또는 이렇게 설정하면 편집기 대신 인라인 메시지 사용
git commit -m "커밋 메시지"
```

---

## 명령어 빠른 참조표

| 명령어 | 설명 |
|--------|------|
| `git init` | 저장소 초기화 |
| `git clone [URL]` | 저장소 복사 |
| `git status` | 현재 상태 확인 |
| `git add .` | 전체 스테이징 |
| `git commit -m "메시지"` | 커밋 |
| `git push origin main` | 원격으로 업로드 |
| `git pull origin main` | 원격에서 다운로드 |
| `git log --oneline` | 이력 확인 |
| `git branch` | 브랜치 목록 |
| `git checkout -b 이름` | 새 브랜치 생성·전환 |

---

*다음 문서: [02-GitHub.md](02-GitHub.md) →*
