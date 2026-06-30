# Firecrawl 활용 프롬프트/명령어 모음

## 사용 방법
Python 코드 또는 Claude Desktop MCP를 통해 실행하세요.
API Key는 반드시 .env 파일에 저장하세요.

---

## 기본 설정

```python
from firecrawl import FirecrawlApp
from dotenv import load_dotenv
import os

load_dotenv()
app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
```

---

## 1. 채용공고 수집 명령어 (8개)

### FC-J01: 사람인 채용공고 수집
```python
# 사람인 그래픽 디자이너 채용공고 검색
results = app.search(
    query="그래픽 디자이너 신입 채용 site:saramin.co.kr",
    params={'limit': 10, 'lang': 'ko'}
)
```

### FC-J02: 잡코리아 채용공고 수집
```python
results = app.search(
    query="UI UX 디자이너 신입 서울 채용 site:jobkorea.co.kr",
    params={'limit': 10, 'lang': 'ko'}
)
```

### FC-J03: 원티드 채용공고 수집
```python
result = app.scrape_url(
    url="https://www.wanted.co.kr/wdList?jobGroupId=5",
    params={'formats': ['markdown'], 'onlyMainContent': True, 'waitFor': 3000}
)
```

### FC-J04: 링크드인 채용공고 수집
```python
results = app.search(
    query="graphic designer entry level Korea site:linkedin.com/jobs",
    params={'limit': 5, 'lang': 'en'}
)
```

### FC-J05: 채용공고 상세 정보 추출
```python
detail = app.extract(
    urls=["https://채용공고URL"],
    params={
        'prompt': '회사명, 직무, 마감일, 필수조건, 우대조건, 복리후생을 JSON으로 추출'
    }
)
```

### FC-J06: 다중 키워드 검색
```python
keywords = ["그래픽디자이너", "브랜드디자이너", "콘텐츠디자이너", "영상편집"]
all_results = []
for kw in keywords:
    r = app.search(query=f"{kw} 신입 채용 2026", params={'limit': 5})
    all_results.extend(r.get('data', []))
```

### FC-J07: 주간 신규 공고 수집
```python
# 이번 주 올라온 신규 공고만
results = app.search(
    query="그래픽디자이너 채용 2026년 1월",
    params={'limit': 20, 'lang': 'ko'}
)
```

### FC-J08: 채용공고 변동 감지
```python
import hashlib
def check_job_changes(url):
    result = app.scrape_url(url, params={'formats': ['markdown']})
    content_hash = hashlib.md5(result.get('markdown', '').encode()).hexdigest()
    return content_hash
```

---

## 2. 기업분석 명령어 (6개)

### FC-C01: 기업 채용 페이지 수집
```python
company_info = app.scrape_url(
    url="https://careers.kakao.com",
    params={'formats': ['markdown'], 'onlyMainContent': True, 'waitFor': 3000}
)
```

### FC-C02: 기업 전체 사이트 크롤링
```python
crawl = app.crawl_url(
    url="https://www.company.com",
    params={
        'crawlerOptions': {'maxDepth': 2, 'limit': 20, 'includes': ['careers/*', 'about/*']},
        'pageOptions': {'onlyMainContent': True}
    },
    wait_until_done=True
)
```

### FC-C03: 기업 정보 구조화 추출
```python
extracted = app.extract(
    urls=["https://company.com/about"],
    params={
        'prompt': '회사명, 설립연도, 직원수, 주요서비스, 인재상을 JSON으로 추출해주세요'
    }
)
```

### FC-C04: 여러 기업 일괄 수집
```python
companies = [
    "https://careers.kakao.com",
    "https://recruit.navercorp.com",
    "https://toss.im/career"
]
results = {}
for url in companies:
    results[url] = app.scrape_url(url, params={'formats': ['markdown']})
```

### FC-C05: 기업 SNS 수집
```python
# 기업 인스타그램 피드 수집 (공개 계정)
insta = app.scrape_url(
    url="https://www.instagram.com/company_name/",
    params={'formats': ['markdown'], 'waitFor': 5000}
)
```

### FC-C06: 경쟁사 비교 수집
```python
competitor_urls = ["https://company-a.com", "https://company-b.com"]
for url in competitor_urls:
    data = app.scrape_url(url, params={'formats': ['markdown']})
    print(f"URL: {url}")
    print(data.get('markdown', '')[:1000])
    print("---")
```

---

## 3. 포트폴리오 트렌드 수집 명령어 (6개)

### FC-T01: Behance 트렌드 수집
```python
behance = app.scrape_url(
    url="https://www.behance.net/galleries/graphic-design",
    params={'formats': ['markdown'], 'waitFor': 3000}
)
```

### FC-T02: Pinterest 디자인 트렌드
```python
results = app.search(
    query="graphic design portfolio 2026 trends site:pinterest.com",
    params={'limit': 10}
)
```

### FC-T03: Awwwards 우수 디자인 수집
```python
awwwards = app.scrape_url(
    url="https://www.awwwards.com/nominees/",
    params={'formats': ['markdown'], 'onlyMainContent': True}
)
```

### FC-T04: 색상 트렌드 수집
```python
color_trends = app.search(
    query="pantone color of the year 2026 graphic design trends",
    params={'limit': 5}
)
```

### FC-T05: 폰트 트렌드 수집
```python
font_trends = app.search(
    query="typography trends 2026 graphic design fonts",
    params={'limit': 5}
)
```

### FC-T06: 한국 디자인 트렌드
```python
kr_trends = app.search(
    query="한국 그래픽 디자인 트렌드 2026 포트폴리오",
    params={'limit': 10, 'lang': 'ko'}
)
```

---

## Claude MCP에서 사용하는 방법

Claude Desktop에서 Firecrawl MCP가 설정된 경우:

```
사용자: "사람인에서 그래픽 디자이너 신입 채용공고 5개 찾아줘"
Claude: [Firecrawl 도구 호출] → 결과 반환 → 분석

사용자: "카카오 채용 페이지에서 디자이너 관련 정보 수집해줘"
Claude: [Firecrawl scrape 호출] → 마크다운 반환 → 분석 요약
```

---

*CGD AI Career Platform - prompt/firecrawl.md*
