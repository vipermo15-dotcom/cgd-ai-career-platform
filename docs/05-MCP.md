# 05. MCP (Model Context Protocol) 설치 및 활용

> MCP로 Claude와 외부 도구를 연결하여 자동화를 구현합니다.

---

## 목차

1. [MCP란?](#1-mcp란)
2. [Claude Desktop 설치](#2-claude-desktop-설치)
3. [MCP 서버 개념 이해](#3-mcp-서버-개념-이해)
4. [GitHub MCP 연결](#4-github-mcp-연결)
5. [Firecrawl MCP 연결](#5-firecrawl-mcp-연결)
6. [실습: MCP로 파일 읽기](#6-실습-mcp로-파일-읽기)
7. [MCP 문제해결](#7-mcp-문제해결)

---

## 1. MCP란?

### Model Context Protocol 개념

MCP(Model Context Protocol)는 AI 모델이 외부 도구·데이터·서비스와 소통하기 위한 표준 프로토콜입니다.  
Anthropic이 2024년에 오픈소스로 공개했습니다.

**쉬운 비유**: 
스마트폰에 앱을 설치하면 카메라, 마이크, GPS 등 기기 기능을 앱이 사용할 수 있는 것처럼, MCP를 통해 Claude가 파일 시스템, GitHub, 웹 스크래핑 등 외부 기능을 사용할 수 있습니다.

### MCP 없이 vs MCP 있을 때

| 상황 | MCP 없이 | MCP 있을 때 |
|------|----------|-------------|
| 파일 읽기 | 내용 복사 후 붙여넣기 | 경로만 알려주면 자동 읽기 |
| GitHub 저장소 | URL 공유 후 수동 설명 | 직접 저장소 탐색 |
| 웹 스크래핑 | 수동으로 복사 후 붙여넣기 | URL 입력으로 자동 수집 |
| 채용공고 분석 | 직접 복사 | URL 주면 자동 분석 |

### MCP의 구성요소

```
Claude (AI 모델)
    │
    │ MCP 프로토콜
    │
    ├── MCP 서버 1: GitHub (저장소 접근)
    ├── MCP 서버 2: Firecrawl (웹 스크래핑)
    ├── MCP 서버 3: File System (로컬 파일)
    └── MCP 서버 4: 기타 도구...
```

---

## 2. Claude Desktop 설치

### Claude Desktop이란?

웹 브라우저의 claude.ai와 달리, 데스크톱 앱은 MCP 기능을 지원합니다.

### 설치 방법

**Windows**:
1. [claude.ai/download](https://claude.ai/download) 접속
2. "Download for Windows" 클릭
3. 다운로드된 `.exe` 설치 파일 실행
4. 로그인 (기존 claude.ai 계정 사용)

**macOS**:
1. [claude.ai/download](https://claude.ai/download) 접속
2. "Download for macOS" 클릭
3. `.dmg` 파일 다운로드 후 실행
4. Applications 폴더로 드래그
5. 실행 후 로그인

### 설치 확인

Claude Desktop 실행 후 다음 확인:
- 로그인 성공
- 채팅 기능 정상 작동
- 설정 아이콘 (우상단) 접근 가능

---

## 3. MCP 서버 개념 이해

### MCP 서버 종류

MCP 서버는 Claude에게 특정 기능을 제공하는 소프트웨어입니다.

**공식 MCP 서버 목록** (Anthropic 제공):
- `filesystem`: 로컬 파일 시스템 접근
- `github`: GitHub API 연동
- `web-search`: 웹 검색
- `fetch`: URL 내용 가져오기

**커뮤니티 MCP 서버**:
- `firecrawl`: 웹 스크래핑 전문
- `notion`: Notion 페이지 접근
- `slack`: Slack 메시지 접근
- `google-drive`: Google Drive 접근

### 설정 파일 위치

MCP 설정은 Claude Desktop의 설정 파일에 JSON 형태로 저장됩니다.

```
Windows: %APPDATA%\Claude\claude_desktop_config.json
macOS:   ~/Library/Application Support/Claude/claude_desktop_config.json
```

### 설정 파일 구조

```json
{
  "mcpServers": {
    "서버이름": {
      "command": "실행 명령어",
      "args": ["인수1", "인수2"],
      "env": {
        "API_KEY": "키값"
      }
    }
  }
}
```

---

## 4. GitHub MCP 연결

### 사전 준비

1. Node.js 설치 확인:
```bash
node --version
# v18 이상 필요
```

2. Node.js가 없다면 [nodejs.org](https://nodejs.org) 에서 LTS 버전 설치

3. GitHub Personal Access Token (PAT) 발급:
   - GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
   - "Generate new token (classic)" 클릭
   - Note: `MCP-Claude`
   - Expiration: 90 days (또는 원하는 기간)
   - 권한 체크:
     - `repo` (전체)
     - `read:org`
     - `read:user`
   - "Generate token" 클릭
   - 토큰 복사 (이 페이지를 닫으면 다시 볼 수 없음!)

### GitHub MCP 설치 및 설정

**방법 1: npx 사용 (권장)**

Claude Desktop 설정 파일 열기:

```bash
# Windows
notepad %APPDATA%\Claude\claude_desktop_config.json

# macOS
open ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

다음 내용 추가:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "여기에_PAT_토큰_입력"
      }
    }
  }
}
```

Claude Desktop 재시작

### GitHub MCP 사용 예시

```
이 저장소를 분석해줘: https://github.com/cgd-ai/cgd-ai-career-platform

1. 폴더 구조를 정리해줘
2. README.md 내용을 요약해줘
3. docs/ 폴더에 있는 파일 목록을 보여줘
```

---

## 5. Firecrawl MCP 연결

### Firecrawl API 키 발급

1. [firecrawl.dev](https://www.firecrawl.dev) 접속
2. "Sign up" 클릭 → GitHub 또는 Google 계정으로 가입
3. 대시보드 → "API Keys"
4. "Create API Key" 클릭
5. API 키 복사

### Firecrawl MCP 설치 및 설정

Claude Desktop 설정 파일에 추가:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxxx"
      }
    },
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "fc-xxxx"
      }
    }
  }
}
```

Claude Desktop 재시작

### Firecrawl MCP 사용 예시

```
다음 URL을 스크래핑해줘:
https://www.wanted.co.kr/wd/12345

채용공고의 다음 내용을 정리해줘:
1. 포지션명
2. 주요 업무
3. 자격 요건
4. 우대 사항
5. 연봉 정보 (있다면)
```

---

## 6. 실습: MCP로 파일 읽기

### File System MCP 설치

로컬 파일을 Claude가 읽을 수 있도록 설정합니다.

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/본인계정/Documents",
        "/Users/본인계정/Desktop"
      ]
    }
  }
}
```

**주의**: 접근 허용할 폴더 경로만 지정하세요. 시스템 전체 경로 지정은 보안 위험이 있습니다.

### 실습 1: 로컬 파일 분석

```
/Users/본인계정/Documents/이력서.docx 파일을 읽어줘.
내용을 요약하고 개선할 점을 알려줘.
```

### 실습 2: 저장소 파일 분석

```
이 저장소의 파일들을 순서대로 읽고 학습 계획을 세워줘:
1. docs/00-오리엔테이션.md
2. students/Week01/체크리스트.md

내가 이번 주에 완료해야 할 항목을 정리해줘.
```

### 실습 3: 채용공고 자동 수집 및 분석

```
다음 채용공고 URL들을 순서대로 방문하여 분석해줘:

1. https://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx=12345
2. https://www.jobkorea.co.kr/Recruit/GI_Read/12345

각 공고에 대해:
- 회사명, 직무, 연봉, 자격요건
- 내 포트폴리오와 매칭 점수 (1-10점)
- 지원 추천 여부와 이유
```

---

## 7. MCP 문제해결

### 문제 1: MCP 서버가 연결 안 됨

**증상**: Claude에게 파일 읽기를 요청하면 "파일에 접근할 수 없다"고 답변

**해결 방법**:
1. 설정 파일의 JSON 문법 확인 (콤마, 괄호 등)
2. Claude Desktop 재시작
3. Node.js 설치 확인: `node --version`
4. 설정 파일 경로 확인

```bash
# JSON 문법 검증 (Node.js 필요)
node -e "JSON.parse(require('fs').readFileSync('설정파일경로', 'utf8'))"
```

### 문제 2: GitHub API 오류

**증상**: `GitHub API error: 401 Unauthorized`

**해결 방법**:
1. GitHub PAT 만료 확인 → 새 토큰 발급
2. 토큰에 필요한 권한이 있는지 확인
3. 설정 파일에 토큰이 정확히 입력되었는지 확인

### 문제 3: Firecrawl API 오류

**증상**: `Firecrawl API error: 402 Payment Required`

**해결 방법**:
1. Firecrawl 대시보드에서 사용량 확인
2. 무료 한도 초과 시 교수자에게 문의

### 설정 파일 예시 (전체)

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/본인계정/Documents",
        "/Users/본인계정/Desktop/cgd-ai-career-platform"
      ]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxxxxxxxxxxx"
      }
    },
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "fc-xxxxxxxxxxxx"
      }
    }
  }
}
```

---

*이전 문서: [04-Claude무료.md](04-Claude무료.md) | 다음 문서: [06-Firecrawl.md](06-Firecrawl.md) →*
