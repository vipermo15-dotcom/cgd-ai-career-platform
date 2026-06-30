# 19. Firecrawl 자동화 심화

## 학습 목표
- Firecrawl API 심화 기능 이해 및 활용
- 채용공고 자동 수집 파이프라인 구축
- Claude MCP와 연동하여 분석 자동화
- 실제 사람인, 잡코리아 데이터 수집 실습

---

## 1. Firecrawl API 심화 활용

### 1.1 기본 vs 심화 활용 비교

| 기능 | 기본 활용 | 심화 활용 |
|------|----------|----------|
| 스크래핑 | 단일 URL | 전체 사이트 크롤링 |
| 데이터 형식 | Markdown | JSON 구조화 데이터 |
| 실행 방식 | 수동 | 스케줄 자동화 |
| 분석 | 없음 | Claude API 연동 |
| 저장 | 없음 | GitHub 자동 커밋 |

### 1.2 Firecrawl SDK 설치 및 설정

```bash
# Python SDK 설치
pip install firecrawl-py

# Node.js SDK 설치
npm install @mendable/firecrawl-js
```

```python
# 기본 설정
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-your-api-key-here")

# 환경변수로 관리 (권장)
import os
from dotenv import load_dotenv

load_dotenv()
app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
```

### 1.3 주요 메서드 정리

```python
# 1. 단일 페이지 스크래핑
result = app.scrape_url(
    url="https://www.saramin.co.kr/zf_user/jobs/view?rec_idx=12345",
    params={
        'formats': ['markdown', 'html'],  # 반환 형식
        'onlyMainContent': True,           # 광고 등 제거
        'waitFor': 2000,                   # 페이지 로딩 대기 (ms)
    }
)

# 2. 전체 사이트 크롤링
crawl_result = app.crawl_url(
    url="https://company.com",
    params={
        'crawlerOptions': {
            'excludes': ['blog/*', 'news/*'],  # 제외 경로
            'includes': ['careers/*', 'jobs/*'], # 포함 경로
            'maxDepth': 3,                      # 최대 깊이
            'limit': 100,                       # 최대 페이지 수
        },
        'pageOptions': {
            'onlyMainContent': True
        }
    }
)

# 3. 구조화 데이터 추출 (Extract)
extracted = app.extract(
    urls=["https://company.com/about"],
    params={
        'prompt': '회사 이름, 설립연도, 직원수, 주요 사업 분야를 추출해주세요',
        'schema': {
            'company_name': 'string',
            'founded_year': 'number',
            'employee_count': 'string',
            'business_areas': 'array'
        }
    }
)

# 4. 검색 (Search)
search_results = app.search(
    query="그래픽 디자이너 채용 서울",
    params={
        'limit': 10,
        'lang': 'ko',
        'country': 'kr'
    }
)
```

---

## 2. 채용공고 자동 수집 스크립트

### 2.1 전체 수집 파이프라인 구조

```
Firecrawl API
    │
    ▼
채용공고 목록 페이지 수집
    │
    ▼
개별 공고 상세 스크래핑
    │
    ▼
데이터 정제 및 구조화
    │
    ▼
JSON/CSV 저장
    │
    ▼
Claude API 분석 (선택)
    │
    ▼
Markdown 보고서 생성
```

### 2.2 사람인 채용공고 수집 스크립트

```python
# scripts/collect_saramin.py
import os
import json
import time
from datetime import datetime
from firecrawl import FirecrawlApp
from dotenv import load_dotenv

load_dotenv()

class SaraminCollector:
    def __init__(self):
        self.app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
        self.jobs = []
        
    def collect_job_list(self, keyword="그래픽디자이너", pages=3):
        """채용공고 목록 페이지 수집"""
        print(f"[수집 시작] 키워드: {keyword}, 페이지: {pages}")
        
        for page in range(1, pages + 1):
            url = f"https://www.saramin.co.kr/zf_user/search/recruit?searchType=search&searchword={keyword}&recruitPage={page}"
            
            try:
                result = self.app.scrape_url(
                    url=url,
                    params={
                        'formats': ['markdown'],
                        'onlyMainContent': True,
                        'waitFor': 3000,
                    }
                )
                
                if result and 'markdown' in result:
                    self.parse_job_list(result['markdown'], page)
                    print(f"  - 페이지 {page} 수집 완료")
                
                time.sleep(2)  # 서버 부하 방지
                
            except Exception as e:
                print(f"  - 페이지 {page} 오류: {e}")
                
    def parse_job_list(self, markdown_text, page):
        """Markdown에서 채용공고 정보 파싱"""
        lines = markdown_text.split('\n')
        
        for line in lines:
            if '채용' in line or '디자이너' in line or '모집' in line:
                if len(line) > 10 and '[' in line:
                    # 기본 정보 추출 (실제로는 더 정교한 파싱 필요)
                    job_entry = {
                        'title': line.strip(),
                        'source_page': page,
                        'collected_at': datetime.now().isoformat(),
                        'platform': 'saramin'
                    }
                    self.jobs.append(job_entry)
    
    def collect_job_detail(self, job_url):
        """개별 채용공고 상세 정보 수집"""
        try:
            result = self.app.extract(
                urls=[job_url],
                params={
                    'prompt': '''
                    다음 정보를 JSON 형태로 추출해주세요:
                    - 회사명 (company_name)
                    - 직무명 (job_title)
                    - 마감일 (deadline)
                    - 요구 경력 (experience)
                    - 요구 학력 (education)
                    - 근무지 (location)
                    - 급여 (salary)
                    - 주요 업무 (responsibilities) - 리스트
                    - 자격 요건 (requirements) - 리스트
                    - 우대 사항 (preferred) - 리스트
                    - 복리후생 (benefits) - 리스트
                    '''
                }
            )
            return result
        except Exception as e:
            print(f"상세 수집 오류: {e}")
            return None
    
    def save_results(self, output_dir="data/jobs"):
        """결과 저장"""
        os.makedirs(output_dir, exist_ok=True)
        
        date_str = datetime.now().strftime("%Y%m%d")
        output_file = f"{output_dir}/saramin_{date_str}.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                'collected_at': datetime.now().isoformat(),
                'total_count': len(self.jobs),
                'jobs': self.jobs
            }, f, ensure_ascii=False, indent=2)
        
        print(f"\n[저장 완료] {output_file} ({len(self.jobs)}건)")
        return output_file

# 실행
if __name__ == "__main__":
    collector = SaraminCollector()
    collector.collect_job_list(keyword="그래픽디자이너", pages=5)
    collector.collect_job_list(keyword="UI디자이너", pages=3)
    collector.collect_job_list(keyword="영상편집", pages=3)
    output_file = collector.save_results()
    print(f"수집 완료: {output_file}")
```

### 2.3 잡코리아 수집 스크립트

```python
# scripts/collect_jobkorea.py
import os
import json
import time
from datetime import datetime
from firecrawl import FirecrawlApp

class JobKoreaCollector:
    def __init__(self):
        self.app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
        
    def search_jobs(self, keywords):
        """키워드 검색으로 채용공고 수집"""
        all_jobs = []
        
        for keyword in keywords:
            print(f"검색 중: {keyword}")
            
            # Firecrawl Search 활용
            results = self.app.search(
                query=f"잡코리아 {keyword} 채용 신입",
                params={
                    'limit': 5,
                    'lang': 'ko'
                }
            )
            
            for result in results.get('data', []):
                if 'jobkorea.co.kr' in result.get('url', ''):
                    job_info = self.extract_job_info(result)
                    if job_info:
                        all_jobs.append(job_info)
            
            time.sleep(1)
        
        return all_jobs
    
    def extract_job_info(self, search_result):
        """검색 결과에서 채용공고 정보 추출"""
        return {
            'title': search_result.get('title', ''),
            'url': search_result.get('url', ''),
            'description': search_result.get('description', '')[:500],
            'platform': 'jobkorea',
            'collected_at': datetime.now().isoformat()
        }
    
    def crawl_company_jobs(self, company_careers_url):
        """기업 채용 페이지 크롤링"""
        result = self.app.crawl_url(
            url=company_careers_url,
            params={
                'crawlerOptions': {
                    'maxDepth': 2,
                    'limit': 20,
                },
                'pageOptions': {
                    'onlyMainContent': True
                }
            },
            wait_until_done=True,
            timeout=60
        )
        return result

if __name__ == "__main__":
    collector = JobKoreaCollector()
    
    keywords = [
        "그래픽디자이너 신입",
        "UI/UX 디자이너",
        "영상 편집자",
        "콘텐츠 디자이너",
        "브랜드 디자이너"
    ]
    
    jobs = collector.search_jobs(keywords)
    
    # 저장
    with open(f"data/jobs/jobkorea_{datetime.now().strftime('%Y%m%d')}.json", 'w', encoding='utf-8') as f:
        json.dump(jobs, f, ensure_ascii=False, indent=2)
    
    print(f"총 {len(jobs)}건 수집 완료")
```

---

## 3. 기업 홈페이지 모니터링

### 3.1 채용 페이지 변경 감지 시스템

```python
# scripts/monitor_companies.py
import os
import json
import hashlib
from datetime import datetime
from firecrawl import FirecrawlApp

class CompanyMonitor:
    def __init__(self, companies_file="data/companies.json"):
        self.app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
        self.companies = self.load_companies(companies_file)
        self.changes = []
    
    def load_companies(self, file_path):
        """모니터링할 기업 목록 로드"""
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        # 기본 기업 목록 (예시)
        return [
            {
                "name": "카카오",
                "careers_url": "https://careers.kakao.com",
                "last_hash": ""
            },
            {
                "name": "네이버",
                "careers_url": "https://recruit.navercorp.com",
                "last_hash": ""
            },
            {
                "name": "쿠팡",
                "careers_url": "https://www.coupang.jobs",
                "last_hash": ""
            }
        ]
    
    def get_content_hash(self, url):
        """페이지 콘텐츠의 해시값 계산"""
        try:
            result = self.app.scrape_url(
                url=url,
                params={
                    'formats': ['markdown'],
                    'onlyMainContent': True
                }
            )
            content = result.get('markdown', '')
            return hashlib.md5(content.encode()).hexdigest(), content
        except Exception as e:
            print(f"스크래핑 오류 ({url}): {e}")
            return None, None
    
    def check_changes(self):
        """모든 기업 채용 페이지 변경 확인"""
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] 기업 채용 페이지 모니터링 시작")
        
        for company in self.companies:
            print(f"  확인 중: {company['name']}")
            
            new_hash, content = self.get_content_hash(company['careers_url'])
            
            if new_hash and new_hash != company.get('last_hash', ''):
                print(f"  ⚠️ 변경 감지: {company['name']}")
                
                self.changes.append({
                    'company': company['name'],
                    'url': company['careers_url'],
                    'detected_at': datetime.now().isoformat(),
                    'content_preview': content[:500] if content else ''
                })
                
                # 해시 업데이트
                company['last_hash'] = new_hash
        
        self.save_companies()
        self.save_changes_report()
        
        return self.changes
    
    def save_companies(self):
        """업데이트된 기업 목록 저장"""
        os.makedirs("data", exist_ok=True)
        with open("data/companies.json", 'w', encoding='utf-8') as f:
            json.dump(self.companies, f, ensure_ascii=False, indent=2)
    
    def save_changes_report(self):
        """변경 리포트 저장"""
        if self.changes:
            date_str = datetime.now().strftime("%Y%m%d_%H%M")
            with open(f"data/changes_{date_str}.json", 'w', encoding='utf-8') as f:
                json.dump(self.changes, f, ensure_ascii=False, indent=2)
            print(f"  변경 리포트 저장: data/changes_{date_str}.json")
        else:
            print("  변경사항 없음")

if __name__ == "__main__":
    monitor = CompanyMonitor()
    changes = monitor.check_changes()
    
    if changes:
        print(f"\n총 {len(changes)}개 기업 채용 페이지 변경 감지!")
```

---

## 4. Claude MCP와 연동하여 자동 분석

### 4.1 Claude API를 활용한 채용공고 분석

```python
# scripts/analyze_with_claude.py
import os
import json
import anthropic
from datetime import datetime

class JobAnalyzer:
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        self.model = "claude-opus-4-5"
    
    def analyze_job(self, job_data):
        """채용공고 분석"""
        job_text = json.dumps(job_data, ensure_ascii=False, indent=2)
        
        message = self.client.messages.create(
            model=self.model,
            max_tokens=2000,
            messages=[
                {
                    "role": "user",
                    "content": f"""
다음 채용공고를 분석해주세요. 컴퓨터그래픽디자인 전공 신입생 관점에서 분석합니다.

=== 채용공고 ===
{job_text}

=== 분석 항목 ===
1. 직무 요약 (3줄 이내)
2. 필수 스킬 목록 (우선순위 순)
3. 우대 스킬 목록
4. CGD 졸업생 지원 가능성 (상/중/하 + 이유)
5. 포트폴리오 준비 포인트 (3가지)
6. 자기소개서 핵심 키워드 (5개)
7. 예상 연봉 범위
8. 지원 추천 여부 + 이유

JSON 형식으로 답변해주세요.
                    """
                }
            ]
        )
        
        return message.content[0].text
    
    def batch_analyze(self, jobs_file, output_file=None):
        """여러 채용공고 일괄 분석"""
        with open(jobs_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        jobs = data.get('jobs', [])
        results = []
        
        print(f"총 {len(jobs)}건 분석 시작...")
        
        for i, job in enumerate(jobs[:10]):  # 최대 10건
            print(f"  분석 중 ({i+1}/{min(len(jobs), 10)}): {job.get('title', '')[:40]}")
            
            try:
                analysis = self.analyze_job(job)
                results.append({
                    'job': job,
                    'analysis': analysis,
                    'analyzed_at': datetime.now().isoformat()
                })
            except Exception as e:
                print(f"  오류: {e}")
        
        # 결과 저장
        if not output_file:
            date_str = datetime.now().strftime("%Y%m%d")
            output_file = f"data/analysis_{date_str}.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"\n분석 완료: {output_file}")
        return results
    
    def generate_summary_report(self, analysis_results):
        """분석 결과 요약 리포트 생성"""
        all_skills = []
        for result in analysis_results:
            try:
                analysis = json.loads(result['analysis'])
                all_skills.extend(analysis.get('필수_스킬_목록', []))
            except:
                pass
        
        # 스킬 빈도 분석
        from collections import Counter
        skill_counts = Counter(all_skills)
        top_skills = skill_counts.most_common(20)
        
        report = f"""# 채용공고 분석 요약 리포트
생성일: {datetime.now().strftime("%Y년 %m월 %d일")}
분석 건수: {len(analysis_results)}건

## 가장 많이 요구되는 스킬 TOP 20
"""
        for i, (skill, count) in enumerate(top_skills, 1):
            report += f"{i}. {skill} ({count}건)\n"
        
        with open("reports/skills_trend.md", 'w', encoding='utf-8') as f:
            f.write(report)
        
        print("요약 리포트 생성 완료: reports/skills_trend.md")
        return report

if __name__ == "__main__":
    analyzer = JobAnalyzer()
    
    import glob
    latest_file = sorted(glob.glob("data/jobs/*.json"))[-1]
    results = analyzer.batch_analyze(latest_file)
    analyzer.generate_summary_report(results)
```

### 4.2 Claude MCP 설정으로 연동

```json
// Claude Desktop - claude_desktop_config.json
{
  "mcpServers": {
    "job-analyzer": {
      "command": "python",
      "args": ["/path/to/cgd-platform/scripts/mcp_server.py"],
      "env": {
        "FIRECRAWL_API_KEY": "fc-your-key",
        "ANTHROPIC_API_KEY": "sk-ant-your-key"
      }
    }
  }
}
```

---

## 5. 실습: 사람인/잡코리아 채용공고 수집

### 실습 순서

**준비물**
- Firecrawl API 키 (https://firecrawl.dev)
- Python 3.10 이상
- VS Code

### Step 1: 환경 설정

```bash
# 프로젝트 폴더 생성
mkdir job-collector
cd job-collector

# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate    # Windows

# 패키지 설치
pip install firecrawl-py python-dotenv anthropic pandas

# .env 파일 생성
echo "FIRECRAWL_API_KEY=fc-your-key-here" > .env
echo "ANTHROPIC_API_KEY=sk-ant-your-key-here" >> .env
```

### Step 2: 첫 번째 수집 실행

```python
# test_collect.py - 처음 실행해보는 간단한 버전
from firecrawl import FirecrawlApp
from dotenv import load_dotenv
import os
import json

load_dotenv()
app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

# 사람인 검색
print("사람인 그래픽디자이너 채용공고 검색...")
results = app.search(
    query="그래픽디자이너 신입 채용 site:saramin.co.kr",
    params={'limit': 5, 'lang': 'ko'}
)

print(f"검색 결과: {len(results.get('data', []))}건")

for i, job in enumerate(results.get('data', []), 1):
    print(f"\n{i}. {job.get('title', '제목 없음')}")
    print(f"   URL: {job.get('url', '')}")
    print(f"   설명: {job.get('description', '')[:100]}...")

# JSON 저장
with open("test_results.json", 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\n결과가 test_results.json에 저장되었습니다.")
```

### Step 3: 수집 결과 분석

```python
# analyze_results.py
import json
import pandas as pd

# 결과 로드
with open("test_results.json", 'r') as f:
    data = json.load(f)

jobs = data.get('data', [])

# DataFrame으로 변환
df = pd.DataFrame([{
    'title': job.get('title', ''),
    'url': job.get('url', ''),
    'description': job.get('description', '')[:200]
} for job in jobs])

print("=== 수집된 채용공고 ===")
print(df.to_string(index=False))

# CSV 저장
df.to_csv("jobs_result.csv", index=False, encoding='utf-8-sig')
print("\njobs_result.csv로 저장 완료!")
```

### Step 4: 전체 파이프라인 실행

```bash
# 1. 수집
python scripts/collect_saramin.py

# 2. 분석
python scripts/analyze_with_claude.py

# 3. 보고서 확인
cat reports/skills_trend.md
```

---

## 6. 고급 활용: 실시간 채용 알림 시스템

```python
# scripts/job_alert.py
# 새로운 채용공고 발견 시 이메일 또는 슬랙으로 알림

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(new_jobs, recipient_email):
    """새 채용공고 이메일 알림"""
    if not new_jobs:
        return
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"[CGD 채용알림] 새 채용공고 {len(new_jobs)}건"
    msg['From'] = os.getenv("EMAIL_FROM")
    msg['To'] = recipient_email
    
    # HTML 이메일 본문
    html_content = "<h2>새로운 채용공고가 등록되었습니다</h2><ul>"
    for job in new_jobs:
        html_content += f"<li><a href='{job['url']}'>{job['title']}</a></li>"
    html_content += "</ul>"
    
    msg.attach(MIMEText(html_content, 'html'))
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASSWORD"))
        server.send_message(msg)
    
    print(f"알림 이메일 발송 완료: {recipient_email}")
```

---

## 핵심 요약

1. **Firecrawl 심화** = scrape(단일) + crawl(전체) + extract(구조화) + search(검색)
2. **자동화 파이프라인** = 수집 → 정제 → 분석 → 저장 → 알림
3. **Claude 연동** = API 또는 MCP를 통해 분석 자동화
4. **모니터링** = 해시값 비교로 페이지 변경 감지
5. **윤리적 수집** = robots.txt 준수, 적절한 딜레이, 서버 부하 고려

---

*CGD AI Career Platform - docs/19-Firecrawl자동화.md*
