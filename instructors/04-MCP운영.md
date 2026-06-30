# Claude Desktop + MCP 운영 가이드 - 교수자용

## 개요
교수자가 Claude Desktop과 MCP를 활용하여 교육 자료를 관리하고 학생 지원을 자동화하는 방법입니다.

---

## 1. Claude Desktop + MCP 설정

### 1.1 교수자용 MCP 설정

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_instructor_token"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/instructor/cgd-platform"
      ]
    },
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "fc-instructor-key"
      }
    }
  }
}
```

---

## 2. GitHub MCP 설정

### 2.1 필요 권한 (PAT 설정)

```
GitHub PAT 필요 권한:
[x] repo - 저장소 전체 읽기/쓰기
[x] read:org - 조직 정보 읽기
[x] write:packages - 패키지 관리
[x] admin:repo_hook - 웹훅 관리 (Actions용)
```

### 2.2 교수자 활용 사례

**사례 1: 학생 저장소 일괄 피드백**
```
Claude에게:
"cgd-students 조직의 모든 저장소를 확인하고
포트폴리오 저장소의 README.md를 분석하여
각 학생별 개선 포인트를 정리해줘"
```

**사례 2: 교육 자료 자동 업데이트**
```
Claude에게:
"cgd-ai-career-platform 저장소의 docs/ 폴더에
이번 주 채용 트렌드를 반영하여
docs/09-AI프롬프트.md 파일을 업데이트해줘
채용공고에서 자주 나오는 새 기술 스택 위주로"
```

**사례 3: 주간 학습 현황 리포트**
```
Claude에게:
"students/ 폴더의 각 Week 폴더를 확인하고
이번 주 미션 제출 현황을 정리해줘
제출한 학생, 미제출 학생을 구분하여 표로 만들어줘"
```

---

## 3. 교육 자료 자동 업데이트

### 3.1 월간 자료 업데이트 루틴

```python
# scripts/update_course_materials.py
# 매월 1일 실행 (GitHub Actions)

import anthropic
import os
from datetime import datetime

def update_ai_trends():
    """AI 트렌드 섹션 자동 업데이트"""
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    # 현재 파일 읽기
    with open("docs/09-AI프롬프트.md", 'r', encoding='utf-8') as f:
        current_content = f.read()
    
    # Claude에게 업데이트 요청
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=3000,
        messages=[{
            "role": "user",
            "content": f"""
다음은 현재 CGD 교육 자료입니다:
{current_content[:3000]}

2026년 최신 AI 도구 트렌드를 반영하여
이 문서의 "최신 AI 도구" 섹션을 업데이트해주세요.
그래픽 디자인 취업 준비에 실제로 유용한 도구 위주로.
Markdown 형식 유지.
"""
        }]
    )
    
    # 업데이트된 섹션 추출 및 파일 저장 로직
    print("AI 트렌드 업데이트 완료")

if __name__ == "__main__":
    update_ai_trends()
```

---

## 4. 자주 묻는 질문

**Q: MCP 서버가 연결되지 않을 때**
```
A: 
1. Claude Desktop 완전 종료 후 재시작
2. config.json JSON 문법 오류 확인
3. node/npm 버전 확인 (v18+)
4. API Key 유효성 확인
```

**Q: GitHub 저장소가 보이지 않을 때**
```
A:
1. PAT에 repo 권한 확인
2. PAT 만료 여부 확인 (기본 30일)
3. Claude에게 "내 GitHub 저장소 목록 보여줘" 로 테스트
```

---

*CGD AI Career Platform - instructors/04-MCP운영.md*
