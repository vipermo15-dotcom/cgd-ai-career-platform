# 03. VSCode 설치 및 설정

> Visual Studio Code로 효율적인 개발 환경을 구축합니다.

---

## 목차

1. [VSCode 소개](#1-vscode-소개)
2. [VSCode 설치](#2-vscode-설치)
3. [필수 확장 프로그램](#3-필수-확장-프로그램)
4. [단축키 모음](#4-단축키-모음)
5. [Git 연동 방법](#5-git-연동-방법)
6. [터미널 사용법](#6-터미널-사용법)
7. [Markdown 작성 팁](#7-markdown-작성-팁)
8. [작업 환경 최적화](#8-작업-환경-최적화)

---

## 1. VSCode 소개

Visual Studio Code(VSCode)는 Microsoft가 만든 무료 코드 편집기입니다.

**CGD 교육에서 VSCode를 사용하는 이유**:
- **무료**: 완전 무료, 상업적 사용 가능
- **가벼움**: 빠른 실행, 낮은 시스템 요구사항
- **Git 내장**: 별도 프로그램 없이 Git 사용 가능
- **Markdown 지원**: 포트폴리오 문서 작성에 최적
- **확장성**: 플러그인으로 기능 무한 확장

---

## 2. VSCode 설치

### Windows 설치

1. [code.visualstudio.com](https://code.visualstudio.com) 접속
2. "Download for Windows" 클릭
3. 다운로드된 `.exe` 파일 실행
4. 설치 옵션 선택 (권장 설정):
   - ✅ "Add 'Open with Code' action to Windows Explorer file context menu"
   - ✅ "Add 'Open with Code' action to Windows Explorer directory context menu"
   - ✅ "Register Code as an editor for supported file types"
   - ✅ "Add to PATH"
5. "Install" 클릭

**설치 확인**:
```bash
code --version
# 출력 예시: 1.85.0
```

### macOS 설치

1. [code.visualstudio.com](https://code.visualstudio.com) 접속
2. "Download for macOS" 클릭
3. 다운로드된 `.zip` 파일 더블클릭 → `Visual Studio Code.app` 생성
4. `Applications` 폴더로 드래그
5. Dock에서 실행

**PATH 설정** (터미널에서 `code` 명령어 사용):
1. VSCode 실행
2. `Cmd+Shift+P` → "Shell Command: Install 'code' command in PATH" 검색 및 실행

---

## 3. 필수 확장 프로그램

확장 프로그램 설치 방법: 좌측 확장 아이콘(네모 4개) 클릭 → 이름 검색 → Install

### 필수 설치 목록

#### 1. Korean Language Pack for Visual Studio Code
- **제작사**: Microsoft
- **검색어**: `Korean Language Pack`
- **용도**: VSCode 한국어 인터페이스
- **설치 후**: VSCode 재시작 → 한국어로 변경됨

#### 2. GitLens — Git supercharged
- **제작사**: GitKraken
- **검색어**: `GitLens`
- **용도**: Git 이력, 커밋 정보 시각화
- **주요 기능**: 각 줄의 마지막 커밋 정보 표시, 파일 이력 확인

#### 3. Markdown Preview Enhanced
- **제작사**: Yiyi Wang
- **검색어**: `Markdown Preview Enhanced`
- **용도**: Markdown 파일 실시간 미리보기
- **단축키**: `Ctrl+Shift+V` (미리보기 열기)

#### 4. Prettier - Code formatter
- **제작사**: Prettier
- **검색어**: `Prettier`
- **용도**: 코드 자동 정렬·포맷팅
- **설정**: `Ctrl+,` → "Format On Save" 검색 → 활성화

#### 5. Auto Rename Tag
- **제작사**: Jun Han
- **검색어**: `Auto Rename Tag`
- **용도**: HTML 태그 수정 시 짝 태그 자동 수정

#### 6. Path Intellisense
- **제작자**: Christian Kohler
- **검색어**: `Path Intellisense`
- **용도**: 파일 경로 자동완성

#### 7. Material Icon Theme
- **제작사**: Philipp Kief
- **검색어**: `Material Icon Theme`
- **용도**: 파일 아이콘을 예쁘게 변경
- **설정**: 설치 후 "Set File Icon Theme" 클릭

#### 8. indent-rainbow
- **제작사**: oderwat
- **검색어**: `indent-rainbow`
- **용도**: 들여쓰기를 색상으로 표시 (코드 가독성 향상)

#### 9. GitHub Copilot (선택)
- **제작사**: GitHub
- **검색어**: `GitHub Copilot`
- **용도**: AI 코드 자동완성
- **비용**: 학생 무료 (GitHub Student Developer Pack 필요)

#### 10. TODO Highlight
- **제작사**: Wayou Liu
- **검색어**: `TODO Highlight`
- **용도**: TODO, FIXME 등 키워드 강조 표시

---

## 4. 단축키 모음

### 필수 단축키 (Windows / Mac)

| 기능 | Windows | macOS |
|------|---------|-------|
| 명령 팔레트 | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| 파일 열기 | `Ctrl+P` | `Cmd+P` |
| 설정 열기 | `Ctrl+,` | `Cmd+,` |
| 터미널 열기 | `Ctrl+`` ` | `Ctrl+`` ` |
| 파일 저장 | `Ctrl+S` | `Cmd+S` |
| 전체 저장 | `Ctrl+K S` | `Cmd+K S` |
| 실행 취소 | `Ctrl+Z` | `Cmd+Z` |
| 다시 실행 | `Ctrl+Y` | `Cmd+Shift+Z` |
| 찾기 | `Ctrl+F` | `Cmd+F` |
| 바꾸기 | `Ctrl+H` | `Cmd+H` |
| 전체 찾기 | `Ctrl+Shift+F` | `Cmd+Shift+F` |

### 편집 단축키

| 기능 | Windows | macOS |
|------|---------|-------|
| 줄 복사 (아래) | `Shift+Alt+↓` | `Shift+Option+↓` |
| 줄 이동 | `Alt+↑/↓` | `Option+↑/↓` |
| 줄 삭제 | `Ctrl+Shift+K` | `Cmd+Shift+K` |
| 줄 선택 | `Ctrl+L` | `Cmd+L` |
| 단어 선택 | `Ctrl+D` | `Cmd+D` |
| 주석 토글 | `Ctrl+/` | `Cmd+/` |
| 들여쓰기 | `Tab` | `Tab` |
| 내어쓰기 | `Shift+Tab` | `Shift+Tab` |
| 멀티커서 | `Alt+클릭` | `Option+클릭` |

### 탐색 단축키

| 기능 | Windows | macOS |
|------|---------|-------|
| 파일 탐색기 | `Ctrl+Shift+E` | `Cmd+Shift+E` |
| 확장 프로그램 | `Ctrl+Shift+X` | `Cmd+Shift+X` |
| Git 패널 | `Ctrl+Shift+G` | `Ctrl+Shift+G` |
| 탭 이동 | `Ctrl+Tab` | `Ctrl+Tab` |
| 사이드바 토글 | `Ctrl+B` | `Cmd+B` |
| 분할 편집기 | `Ctrl+\` | `Cmd+\` |

---

## 5. Git 연동 방법

### VSCode에서 Git 사용하기

VSCode에는 Git이 기본으로 내장되어 있습니다.

**Git 패널 열기**: 좌측 브랜치 아이콘 클릭 또는 `Ctrl+Shift+G`

### 기본 Git 작업 (GUI 방식)

**파일 스테이징**:
1. Git 패널에서 변경된 파일 확인
2. 파일 옆 `+` 버튼 클릭 → 스테이징
3. 또는 "Changes" 옆 `+` 클릭 → 전체 스테이징

**커밋**:
1. 메시지 입력란에 커밋 메시지 작성
2. `Ctrl+Enter` 또는 체크 아이콘 클릭

**Push/Pull**:
- 하단 상태바의 동기화 아이콘 클릭
- 또는 Git 패널 상단 `...` → Push/Pull

### 저장소 Clone하기 (VSCode GUI)

1. `Ctrl+Shift+P` → "Git: Clone" 검색
2. GitHub URL 입력
3. 저장 위치 선택
4. "Open in new window" 또는 "Open" 클릭

---

## 6. 터미널 사용법

### 통합 터미널 열기

- 단축키: `Ctrl+`` ` (백틱)
- 메뉴: View → Terminal
- 새 터미널: `Ctrl+Shift+`` `

### 터미널 종류 선택

우상단 `+` 옆 화살표 클릭:
- **Windows**: PowerShell, Command Prompt, Git Bash
- **macOS**: bash, zsh

**Git Bash 권장** (Windows): Git 명령어를 Linux 스타일로 사용 가능

### 기본 터미널 명령어

```bash
# 현재 위치 확인
pwd

# 폴더 목록 보기
ls        # macOS/Linux/Git Bash
dir       # Windows CMD

# 폴더 이동
cd 폴더명

# 상위 폴더로 이동
cd ..

# 새 폴더 만들기
mkdir 폴더명

# 파일 내용 보기
cat 파일명.md

# 파일 삭제 (주의!)
rm 파일명.md

# 폴더 삭제 (주의!)
rm -rf 폴더명
```

### 분할 터미널 활용

`Ctrl+Shift+5` (또는 우상단 분할 아이콘)로 터미널을 분할하여 여러 명령어를 동시에 실행할 수 있습니다.

---

## 7. Markdown 작성 팁

### Markdown이란?

Markdown은 간단한 기호를 사용하여 서식을 지정하는 마크업 언어입니다.  
GitHub, Notion, Claude에서 모두 사용됩니다.

### 기본 문법

```markdown
# 제목 1
## 제목 2
### 제목 3

**굵은 글씨**
*기울임*
~~취소선~~

- 목록 항목
  - 하위 항목
1. 번호 목록

[링크텍스트](URL)
![이미지설명](이미지URL)

> 인용문

`인라인 코드`

```코드블록```

| 표 | 헤더 |
|---|------|
| 내용 | 내용 |
```

### Markdown 미리보기

`Ctrl+Shift+V` 또는 편집기 우상단 미리보기 아이콘 클릭

---

## 8. 작업 환경 최적화

### 테마 설정

1. `Ctrl+K Ctrl+T` → 테마 목록
2. 권장 테마:
   - Light: `GitHub Light` (밝은 환경)
   - Dark: `One Dark Pro` (어두운 환경)
   - 기본: `Default Dark+`

### 폰트 설정

설정(`Ctrl+,`) → "Font Family" 검색:

```
'D2Coding', 'Nanum Gothic Coding', Consolas, 'Courier New', monospace
```

D2Coding 폰트 다운로드: [github.com/naver/d2codingfont](https://github.com/naver/d2codingfont)

### 자동 저장 설정

설정 → "Auto Save" 검색 → `afterDelay` 선택 (지연 후 자동 저장)

### 설정 파일 직접 편집

`Ctrl+,` → 우상단 `{}` 아이콘 → `settings.json` 편집:

```json
{
    "editor.fontSize": 14,
    "editor.fontFamily": "'D2Coding', Consolas, monospace",
    "editor.tabSize": 2,
    "editor.wordWrap": "on",
    "editor.formatOnSave": true,
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
    "workbench.colorTheme": "Default Dark+",
    "terminal.integrated.defaultProfile.windows": "Git Bash"
}
```

---

*이전 문서: [02-GitHub.md](02-GitHub.md) | 다음 문서: [04-Claude무료.md](04-Claude무료.md) →*
