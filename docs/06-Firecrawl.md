# 06. Firecrawl 웹 스크래핑 가이드

> Firecrawl로 채용공고와 기업 홈페이지를 자동 수집합니다.

---

## 목차

1. [Firecrawl 소개 및 가입](#1-firecrawl-소개-및-가입)
2. [API Key 발급](#2-api-key-발급)
3. [웹 스크래핑 기본](#3-웹-스크래핑-기본)
4. [채용공고 수집 실습](#4-채용공고-수집-실습)
5. [기업 홈페이지 분석 실습](#5-기업-홈페이지-분석-실습)
6. [Markdown 출력 저장](#6-markdown-출력-저장)
7. [Claude와 연동하여 분석](#7-claude와-연동하여-분석)

---

## 1. Firecrawl 소개 및 가입

### Firecrawl이란?

Firecrawl은 웹사이트의 내용을 자동으로 수집하여 Markdown 형태로 변환해주는 서비스입니다.

**주요 기능**:
- **Scrape**: 단일 URL의 내용 수집
- **Crawl**: 도메인 전체를 순서대로 수집
- **Map**: 사이트맵 생성 (URL 목록)
- **Extract**: 특정 데이터만 추출 (구조화 데이터)

**왜 Firecrawl을 사용하나요?**

일반 웹 복사(Ctrl+C)의 문제점:
- 광고, 메뉴, 불필요한 요소까지 복사됨
- 형식이 망가짐
- 큰 페이지는 일일이 복사하기 어려움

Firecrawl의 장점:
- 불필요한 요소 제거
- 깔끔한 Markdown 형식으로 변환
- API로 자동화 가능
- 동적 페이지(JavaScript 렌더링) 지원

### 가입 방법

1. [firecrawl.dev](https://www.firecrawl.dev) 접속
2. "Get Started" 클릭
3. GitHub 또는 Google 계정으로 가입 (권장)
4. 이메일 인증
5. 대시보드 접속 확인

### 무료 플랜 한도

| 항목 | 무료 한도 |
|------|-----------|
| 스크래핑 횟수 | 500회/월 |
| 크롤링 페이지 | 500페이지/월 |
| 추출 | 100회/월 |

> 교육용 목적으로는 교수자 계정을 활용합니다.

---

## 2. API Key 발급

### API Key 생성

1. Firecrawl 대시보드 로그인
2. 좌측 메뉴 "API Keys" 클릭
3. "Create API Key" 클릭
4. 이름 입력 (예: `CGD-Education`)
5. "Create" 클릭
6. 생성된 키 복사 (`fc-xxxxxxxx` 형태)

### API Key 보안 관리

**절대 하지 말아야 할 것**:
- GitHub 저장소에 API 키 업로드
- 카카오톡, 이메일 등으로 API 키 공유
- 공개 문서에 API 키 포함

**안전한 관리법**:
```bash
# 환경변수로 설정 (macOS/Linux)
export FIRECRAWL_API_KEY="fc-xxxxxxxx"

# .env 파일 사용
echo "FIRECRAWL_API_KEY=fc-xxxxxxxx" > .env
echo ".env" >> .gitignore  # .gitignore에 추가 필수!
```

---

## 3. 웹 스크래핑 기본

### Python으로 스크래핑 (기초)

```python
# 설치: pip install firecrawl-py
from firecrawl import FirecrawlApp
import os

# API 키로 초기화
app = FirecrawlApp(api_key=os.environ.get("FIRECRAWL_API_KEY"))

# 단일 URL 스크래핑
result = app.scrape_url("https://www.wanted.co.kr/wd/12345")

# 결과 출력
print(result['markdown'])  # Markdown 형식
print(result['metadata']['title'])  # 페이지 제목
```

### curl 명령어로 스크래핑 (CLI)

```bash
curl -X POST https://api.firecrawl.dev/v1/scrape \
  -H "Authorization: Bearer fc-xxxxxxxx" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx=12345",
    "formats": ["markdown"]
  }'
```

### JavaScript로 스크래핑 (Node.js)

```javascript
// 설치: npm install @mendable/firecrawl-js
import FirecrawlApp from '@mendable/firecrawl-js';

const app = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY });

const result = await app.scrapeUrl('https://www.wanted.co.kr/wd/12345', {
  formats: ['markdown']
});

console.log(result.markdown);
```

---

## 4. 채용공고 수집 실습

### 실습 1: 사람인 채용공고 수집

```python
from firecrawl import FirecrawlApp
import json

app = FirecrawlApp(api_key="fc-xxxxxxxx")

# 채용공고 URL (실제 공고 URL로 변경)
url = "https://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx=12345"

result = app.scrape_url(url, params={
    'formats': ['markdown', 'extract'],
    'extract': {
        'schema': {
            'type': 'object',
            'properties': {
                'company_name': {'type': 'string', 'description': '회사명'},
                'position': {'type': 'string', 'description': '채용 직무'},
                'deadline': {'type': 'string', 'description': '마감일'},
                'requirements': {'type': 'array', 'items': {'type': 'string'}, 'description': '자격요건'},
                'preferred': {'type': 'array', 'items': {'type': 'string'}, 'description': '우대사항'},
                'salary': {'type': 'string', 'description': '연봉 정보'}
            }
        }
    }
})

# 구조화된 데이터 출력
print(json.dumps(result['extract'], ensure_ascii=False, indent=2))
```

### 실습 2: 여러 채용공고 일괄 수집

```python
from firecrawl import FirecrawlApp
import json
from datetime import datetime

app = FirecrawlApp(api_key="fc-xxxxxxxx")

# 수집할 채용공고 목록
job_urls = [
    "https://www.saramin.co.kr/zf_user/jobs/relay/view?rec_idx=11111",
    "https://www.jobkorea.co.kr/Recruit/GI_Read/11111",
    "https://www.wanted.co.kr/wd/11111",
]

results = []

for url in job_urls:
    try:
        result = app.scrape_url(url, params={'formats': ['markdown']})
        results.append({
            'url': url,
            'title': result.get('metadata', {}).get('title', ''),
            'content': result.get('markdown', ''),
            'scraped_at': datetime.now().isoformat()
        })
        print(f"완료: {url}")
    except Exception as e:
        print(f"오류 ({url}): {e}")

# 결과를 JSON 파일로 저장
with open('채용공고_수집결과.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n총 {len(results)}개 공고 수집 완료")
```

### 실습 3: 원티드(Wanted) 검색 결과 수집

```python
# Wanted 디자이너 검색 페이지 크롤링
app = FirecrawlApp(api_key="fc-xxxxxxxx")

crawl_result = app.crawl_url(
    "https://www.wanted.co.kr/jobs?category=design",
    params={
        'limit': 10,  # 최대 10페이지
        'scrapeOptions': {
            'formats': ['markdown']
        }
    }
)

# 각 페이지의 채용공고 링크 수집
for page in crawl_result['data']:
    print(page['metadata']['url'])
    print(page['markdown'][:500])  # 앞 500자만 출력
    print("---")
```

---

## 5. 기업 홈페이지 분석 실습

### 실습 4: 기업 홈페이지 전체 분석

```python
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-xxxxxxxx")

# 기업 홈페이지 크롤링
company_url = "https://www.kakao.com"

result = app.scrape_url(company_url, params={
    'formats': ['markdown'],
    'includeTags': ['main', 'article', 'section'],  # 주요 콘텐츠만
    'excludeTags': ['nav', 'footer', 'header']  # 제외
})

markdown_content = result['markdown']

# 파일로 저장
with open('기업분석_카카오.md', 'w', encoding='utf-8') as f:
    f.write(f"# 카카오 기업 분석\n")
    f.write(f"수집일: {datetime.now().strftime('%Y-%m-%d')}\n")
    f.write(f"URL: {company_url}\n\n")
    f.write(markdown_content)

print("기업 분석 완료")
```

### 실습 5: 회사 비전·미션 추출

```python
result = app.scrape_url("https://www.company.com/about", params={
    'formats': ['extract'],
    'extract': {
        'schema': {
            'type': 'object',
            'properties': {
                'vision': {'type': 'string', 'description': '회사 비전'},
                'mission': {'type': 'string', 'description': '회사 미션'},
                'core_values': {'type': 'array', 'items': {'type': 'string'}, 'description': '핵심 가치'},
                'history': {'type': 'string', 'description': '회사 연혁'},
                'business': {'type': 'string', 'description': '주요 사업'}
            }
        }
    }
})

print(json.dumps(result['extract'], ensure_ascii=False, indent=2))
```

---

## 6. Markdown 출력 저장

### 수집 결과를 구조화된 파일로 저장

```python
import os
from pathlib import Path

# 저장 폴더 생성
save_dir = Path("기업분석DB")
save_dir.mkdir(exist_ok=True)

def save_company_analysis(company_name, url, content):
    """기업 분석 결과를 Markdown 파일로 저장"""
    
    filename = f"{company_name}_{datetime.now().strftime('%Y%m%d')}.md"
    filepath = save_dir / filename
    
    template = f"""# {company_name} 기업 분석

## 기본 정보
- **수집일**: {datetime.now().strftime('%Y년 %m월 %d일')}
- **출처 URL**: {url}

## 홈페이지 내용

{content}

## 분석 메모
<!-- 여기에 Claude로 분석한 내용을 추가하세요 -->

## 면접 준비 포인트
<!-- 기업 특성을 바탕으로 준비할 내용 -->
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"저장 완료: {filepath}")
    return filepath

# 사용 예시
save_company_analysis("카카오", "https://www.kakao.com", result['markdown'])
```

---

## 7. Claude와 연동하여 분석

### Firecrawl로 수집 후 Claude로 분석하는 워크플로우

**Step 1**: Firecrawl로 채용공고 수집 → Markdown 저장  
**Step 2**: Claude에게 파일 첨부 또는 내용 붙여넣기  
**Step 3**: Claude로 분석 및 자기소개서 작성

### Claude 분석 프롬프트 (기업 분석)

```
아래는 Firecrawl로 수집한 [회사명] 홈페이지 내용이야.

[수집된 Markdown 내용 붙여넣기]

위 내용을 바탕으로 다음을 분석해줘:

1. **기업 개요** (3줄 요약)
2. **사업 분야** (주요 제품/서비스)
3. **기업 문화** (가치관, 일하는 방식)
4. **디자이너 역할** (디자인팀이 하는 일)
5. **면접 준비 포인트** (이 기업에서 중요시하는 것)
6. **예상 면접 질문** 5가지
7. **자기소개서 핵심 키워드** 10개
```

### 자동화 스크립트 (수집 + 분석 + 저장)

```python
# 교수자용 자동화 스크립트
from firecrawl import FirecrawlApp
import anthropic
import json
from datetime import datetime

firecrawl = FirecrawlApp(api_key="fc-xxxxxxxx")
claude = anthropic.Anthropic(api_key="sk-ant-xxxxxxxx")

def analyze_job_posting(job_url):
    """채용공고 URL을 받아 자동으로 분석 리포트 생성"""
    
    # 1. 스크래핑
    print(f"스크래핑 중: {job_url}")
    scraped = firecrawl.scrape_url(job_url, params={'formats': ['markdown']})
    content = scraped['markdown']
    
    # 2. Claude로 분석
    prompt = f"""다음 채용공고를 분석하고 아래 형식으로 정리해줘:

{content}

## 분석 항목
1. 회사명과 직무
2. 주요 업무 (5가지)
3. 필수 자격요건
4. 우대 사항
5. 추정 연봉 범위
6. 자기소개서 핵심 키워드
7. 디자인 포트폴리오 준비 포인트"""

    response = claude.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    )
    
    analysis = response.content[0].text
    
    # 3. 파일 저장
    filename = f"채용분석_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# 채용공고 분석 리포트\n")
        f.write(f"URL: {job_url}\n\n")
        f.write(f"## 분석 결과\n{analysis}\n\n")
        f.write(f"## 원본 내용\n{content}")
    
    print(f"분석 완료: {filename}")
    return filename

# 실행
analyze_job_posting("https://www.wanted.co.kr/wd/12345")
```

---

*이전 문서: [05-MCP.md](05-MCP.md) | 다음 문서: [07-GitHubProjects.md](07-GitHubProjects.md) →*
