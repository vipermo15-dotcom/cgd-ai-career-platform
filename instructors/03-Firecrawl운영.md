# Firecrawl 운영 가이드 - 교수자용

## 개요
교수자가 Firecrawl을 활용하여 채용공고를 자동 수집하고 기업 정보를 모니터링하는 방법입니다.

---

## 1. Firecrawl API 운영 가이드

### 1.1 계정 및 크레딧 관리

```
관리 URL: https://firecrawl.dev/dashboard
API Key 위치: Dashboard > API Keys

크레딧 소모량 예상:
- 단일 페이지 스크래핑: 1 크레딧
- 검색 (10건): 5 크레딧
- 사이트 크롤링 (페이지당): 1 크레딧
- Extract (구조화): 3 크레딧

월간 운영 계획:
- 주간 채용공고 수집 (주 2회 × 50건): 500 크레딧
- 기업 DB 업데이트 (월 1회 × 50기업): 200 크레딧
- 모니터링 (일 1회 × 10기업 × 30일): 300 크레딧
- 여유분: 500 크레딧

권장 월간 크레딧: 1500+ (유료 플랜 필요)
```

### 1.2 API Key 보안 관리

```bash
# .env 파일 (로컬 개발용)
FIRECRAWL_API_KEY=fc-your-key-here

# GitHub Secrets (자동화용)
# Settings > Secrets > FIRECRAWL_API_KEY 등록

# 절대 코드에 직접 입력 금지!
# 절대 GitHub에 .env 파일 업로드 금지!
```

---

## 2. 월간 채용공고 수집 루틴

### 2.1 자동 수집 스케줄

GitHub Actions로 자동화된 수집 루틴:

```yaml
# .github/workflows/weekly-jobs.yml
on:
  schedule:
    - cron: '0 8 * * 1'   # 매주 월요일 오전 8시
    - cron: '0 8 * * 4'   # 매주 목요일 오전 8시
```

### 2.2 수동 수집 명령어

```bash
# 전체 키워드 채용공고 수집
python scripts/collect_jobs.py --keywords "그래픽디자이너 UI디자이너 영상편집" --pages 5

# 특정 플랫폼만 수집
python scripts/collect_jobs.py --platform saramin --keyword "그래픽디자이너"

# 결과 확인
ls data/jobs/
cat data/jobs/$(ls -t data/jobs/ | head -1)
```

### 2.3 수집 결과 검증

매주 월요일 수집 후 확인 사항:
```
[ ] data/jobs/ 폴더에 새 파일 생성 확인
[ ] 수집 건수 확인 (최소 30건 이상)
[ ] 수집 내용 샘플 검토 (오류 데이터 없는지)
[ ] CGD 플랫폼에 반영 확인 (채용공고 메뉴)
```

---

## 3. 자동화 스케줄 설정

### 3.1 GitHub Actions 스케줄 관리

```yaml
# 전체 자동화 스케줄
jobs:
  # 월요일/목요일 - 채용공고 수집
  collect-jobs:
    schedule: '0 8 * * 1,4'
  
  # 매일 밤 11시 - 기업 변동 모니터링
  monitor-companies:
    schedule: '0 23 * * *'
  
  # 매월 1일 - 월간 리포트 생성
  monthly-report:
    schedule: '0 9 1 * *'
  
  # 매주 금요일 - GitHub Pages 빌드
  build-docs:
    schedule: '0 18 * * 5'
```

### 3.2 알림 설정

```yaml
# 수집 완료 시 이메일 알림
- name: 완료 알림
  uses: dawidd6/action-send-mail@v3
  with:
    subject: "[CGD] 채용공고 수집 완료 - ${{ github.run_id }}"
    to: instructor@cgd.edu
    body: |
      채용공고 자동 수집이 완료되었습니다.
      수집일: ${{ github.event.schedule }}
      수집 건수: ${{ steps.collect.outputs.count }}건
      확인: https://cgdplatform-pm7dnqip.manus.space/jobs
```

---

## 4. 오류 대응 가이드

### 4.1 자주 발생하는 오류

| 오류 코드 | 원인 | 해결 |
|---------|------|------|
| 401 | API Key 만료 또는 오류 | 새 키 발급 후 Secrets 업데이트 |
| 402 | 크레딧 소진 | firecrawl.dev에서 충전 |
| 429 | 요청 한도 초과 | 딜레이 추가 (time.sleep(5)) |
| 503 | 서버 오류 | 30분 후 재시도 |
| 빈 결과 | 페이지 로딩 실패 | waitFor 값 증가 |

---

*CGD AI Career Platform - instructors/03-Firecrawl운영.md*
