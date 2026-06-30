# 자동화 시스템 - CGD AI Career Platform

## 개요

CGD AI Career Platform의 자동화 시스템은 채용공고 수집, 기업 모니터링, 교육 자료 업데이트를 자동으로 처리합니다.

---

## 자동화 구성 요소

```
automation/
├── README.md                    ← 이 파일
└── scripts/
    ├── auto-update.yml          ← GitHub Actions 메인 워크플로우
    ├── collect_jobs.py          ← 채용공고 수집 스크립트
    ├── analyze_company.py       ← 기업 분석 스크립트
    ├── generate_report.py       ← 보고서 생성 스크립트
    └── monitor_companies.py     ← 기업 모니터링 스크립트
```

---

## 자동화 워크플로우 목록

| 워크플로우 | 파일 | 스케줄 | 목적 |
|-----------|------|--------|------|
| 채용공고 수집 | auto-update.yml | 월/목 오전 8시 | 채용공고 DB 업데이트 |
| 기업 모니터링 | company-monitor.yml | 매일 밤 11시 | 기업 채용 변동 감지 |
| 월간 리포트 | monthly-report.yml | 매월 1일 | 취업 현황 자동 리포트 |
| 문서 업데이트 | update-docs.yml | 매주 금요일 | 교육 자료 업데이트 |

---

## 시작하기

### 1. GitHub Secrets 설정

저장소 Settings > Secrets and variables > Actions에서 설정:

```
FIRECRAWL_API_KEY    - Firecrawl API 키
ANTHROPIC_API_KEY    - Claude API 키
PLATFORM_ADMIN_TOKEN - CGD 플랫폼 관리자 토큰
SLACK_WEBHOOK_URL    - 슬랙 알림 (선택)
GMAIL_USER           - 이메일 알림 (선택)
GMAIL_PASSWORD       - 이메일 비밀번호 (선택)
```

### 2. 수동 실행 방법

GitHub > Actions > 원하는 워크플로우 > "Run workflow" 버튼

### 3. 로컬 실행 방법

```bash
# 환경 설정
pip install firecrawl-py anthropic python-dotenv

# .env 파일 설정
cp .env.example .env
# .env 파일에 API 키 입력

# 실행
python automation/scripts/collect_jobs.py
```

---

## 자동화 결과물 위치

```
data/
├── jobs/
│   ├── saramin_20260115.json     ← 사람인 채용공고
│   ├── jobkorea_20260115.json    ← 잡코리아 채용공고
│   └── combined_20260115.json    ← 통합 데이터
│
├── companies/
│   ├── companies.json            ← 전체 기업 DB
│   └── raw/                      ← 수집 원본
│
└── reports/
    ├── monthly_2026-01.md        ← 월간 리포트
    └── skills_trend.md           ← 스킬 트렌드 분석
```

---

## 트러블슈팅

| 문제 | 원인 | 해결 |
|------|------|------|
| 워크플로우 실패 | API 키 오류 | Secrets 확인 |
| 빈 결과 | 크레딧 소진 | firecrawl.dev에서 충전 |
| 커밋 실패 | 권한 오류 | `permissions: contents: write` 추가 |

---

*CGD AI Career Platform - automation/README.md*
