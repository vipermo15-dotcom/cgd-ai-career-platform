# 18. GitHub Actions - 자동화 워크플로우

## 학습 목표
- GitHub Actions의 개념과 CI/CD 파이프라인 이해
- YAML 워크플로우 파일 작성 능력 습득
- 취업지원 플랫폼에서 실무 자동화 구현

---

## 1. GitHub Actions란?

GitHub Actions는 GitHub 저장소에서 직접 소프트웨어 개발 워크플로우를 자동화하는 도구입니다. 코드 변경, 이슈 생성, PR 제출 등의 이벤트가 발생할 때 자동으로 작업을 실행할 수 있습니다.

### 핵심 개념

| 용어 | 설명 |
|------|------|
| **Workflow** | 자동화된 프로세스 전체 (.yml 파일) |
| **Event** | 워크플로우를 시작시키는 트리거 (push, PR, schedule 등) |
| **Job** | 워크플로우 안에서 실행되는 작업 단위 |
| **Step** | Job 안에서 순서대로 실행되는 개별 명령 |
| **Action** | 재사용 가능한 작업 단위 (Marketplace에서 가져오거나 직접 작성) |
| **Runner** | Job을 실행하는 서버 환경 (ubuntu-latest, macos-latest 등) |

### GitHub Actions 무료 플랜 한도
- Public 저장소: 무제한 무료
- Private 저장소: 월 2,000분 무료
- 저장 공간: 500MB 무료

---

## 2. YAML 파일 기본 구조

GitHub Actions 워크플로우는 `.github/workflows/` 폴더에 `.yml` 파일로 작성합니다.

### 기본 구조 템플릿

```yaml
# 워크플로우 이름 (GitHub UI에 표시됨)
name: 워크플로우 이름

# 트리거 이벤트 설정
on:
  push:                    # push 이벤트 발생 시
    branches: [ main ]     # main 브랜치에서만
  pull_request:            # PR 이벤트 발생 시
    branches: [ main ]
  schedule:                # 스케줄 실행
    - cron: '0 9 * * 1'   # 매주 월요일 오전 9시
  workflow_dispatch:       # 수동 실행 버튼 추가

# 환경 변수 (전체 워크플로우에서 사용)
env:
  MY_VAR: "값"

# 작업 정의
jobs:
  job-이름:                          # Job ID
    name: "보기 좋은 Job 이름"        # UI 표시 이름
    runs-on: ubuntu-latest           # 실행 환경

    # 단계별 작업
    steps:
      - name: 저장소 체크아웃
        uses: actions/checkout@v4    # 공식 Action 사용

      - name: Node.js 설정
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: 패키지 설치
        run: npm install

      - name: 테스트 실행
        run: npm test
```

### 주요 이벤트 트리거

```yaml
on:
  # 특정 파일 변경 시에만 실행
  push:
    paths:
      - 'docs/**'
      - '*.md'

  # 수동 실행 + 입력값 받기
  workflow_dispatch:
    inputs:
      company_name:
        description: '분석할 기업명'
        required: true
        default: '삼성전자'
      report_type:
        description: '보고서 유형'
        type: choice
        options:
          - 기본분석
          - 심화분석

  # 다른 워크플로우 완료 시
  workflow_run:
    workflows: ["채용공고 수집"]
    types: [completed]
```

---

## 3. 취업지원 플랫폼 활용 예시

### 3.1 채용공고 자동 수집 워크플로우

```yaml
name: 채용공고 자동 수집

on:
  schedule:
    - cron: '0 8 * * 1,3,5'  # 월, 수, 금 오전 8시
  workflow_dispatch:
    inputs:
      keyword:
        description: '검색 키워드'
        required: false
        default: '그래픽디자인'

jobs:
  collect-jobs:
    runs-on: ubuntu-latest
    
    steps:
      - name: 저장소 체크아웃
        uses: actions/checkout@v4

      - name: Python 설정
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: 의존성 설치
        run: |
          pip install requests python-dotenv

      - name: Firecrawl로 채용공고 수집
        env:
          FIRECRAWL_API_KEY: ${{ secrets.FIRECRAWL_API_KEY }}
          SEARCH_KEYWORD: ${{ github.event.inputs.keyword || '그래픽디자인' }}
        run: |
          python scripts/collect_jobs.py

      - name: 결과 커밋 및 푸시
        run: |
          git config --global user.name 'CGD Bot'
          git config --global user.email 'bot@cgd-platform.com'
          git add data/jobs/
          git commit -m "채용공고 자동 업데이트 $(date '+%Y-%m-%d')" || echo "변경사항 없음"
          git push
```

### 3.2 포트폴리오 리뷰 알림 워크플로우

```yaml
name: 포트폴리오 PR 리뷰 알림

on:
  pull_request:
    types: [opened, ready_for_review]
    paths:
      - 'students/*/portfolio/**'

jobs:
  notify-review:
    runs-on: ubuntu-latest
    
    steps:
      - name: PR 정보 추출
        id: pr-info
        run: |
          echo "author=${{ github.event.pull_request.user.login }}" >> $GITHUB_OUTPUT
          echo "title=${{ github.event.pull_request.title }}" >> $GITHUB_OUTPUT

      - name: 슬랙 알림 발송
        uses: 8398a7/action-slack@v3
        with:
          status: custom
          custom_payload: |
            {
              "text": "새 포트폴리오 리뷰 요청!\n작성자: ${{ steps.pr-info.outputs.author }}\n제목: ${{ steps.pr-info.outputs.title }}"
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

---

## 4. 자동 Markdown 생성 워크플로우

학생이 데이터를 입력하면 자동으로 Markdown 보고서를 생성하는 워크플로우입니다.

```yaml
name: 기업분석 보고서 자동 생성

on:
  workflow_dispatch:
    inputs:
      company_url:
        description: '기업 홈페이지 URL'
        required: true
      company_name:
        description: '기업명'
        required: true
      student_name:
        description: '학생 이름'
        required: true

jobs:
  generate-report:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4

      - name: Python 환경 설정
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: 필요 패키지 설치
        run: pip install requests jinja2 python-dateutil

      - name: 기업 정보 수집 (Firecrawl)
        id: scrape
        env:
          FIRECRAWL_API_KEY: ${{ secrets.FIRECRAWL_API_KEY }}
          COMPANY_URL: ${{ github.event.inputs.company_url }}
        run: |
          python scripts/scrape_company.py
          echo "data_file=data/companies/${{ github.event.inputs.company_name }}.json" >> $GITHUB_OUTPUT

      - name: Claude API로 분석
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          COMPANY_NAME: ${{ github.event.inputs.company_name }}
        run: |
          python scripts/analyze_company.py

      - name: Markdown 보고서 생성
        run: |
          python scripts/generate_report.py \
            --company "${{ github.event.inputs.company_name }}" \
            --student "${{ github.event.inputs.student_name }}" \
            --output "reports/${{ github.event.inputs.student_name }}-${{ github.event.inputs.company_name }}.md"

      - name: 보고서 커밋
        run: |
          git config user.name 'CGD Auto Reporter'
          git config user.email 'bot@cgd.edu'
          git add reports/
          git commit -m "기업분석 보고서: ${{ github.event.inputs.company_name }} (by ${{ github.event.inputs.student_name }})"
          git push

      - name: PR 생성
        uses: peter-evans/create-pull-request@v6
        with:
          title: "[보고서] ${{ github.event.inputs.company_name }} 기업분석"
          body: |
            ## 기업분석 보고서
            - **기업명**: ${{ github.event.inputs.company_name }}
            - **작성자**: ${{ github.event.inputs.student_name }}
            - **생성일**: ${{ github.run_started_at }}
            
            자동 생성된 보고서입니다. 검토 후 승인해주세요.
          labels: |
            auto-generated
            company-analysis
```

---

## 5. 자동 Release 워크플로우

교육 자료를 버전별로 관리하고 자동으로 Release를 생성합니다.

```yaml
name: 교육 자료 자동 릴리즈

on:
  push:
    tags:
      - 'v*.*.*'        # v1.0.0, v2.1.3 형식의 태그 푸시 시

permissions:
  contents: write

jobs:
  create-release:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # 전체 히스토리 가져오기

      - name: 변경 로그 생성
        id: changelog
        run: |
          # 이전 태그부터 현재까지 커밋 로그 추출
          PREV_TAG=$(git describe --tags --abbrev=0 HEAD^ 2>/dev/null || echo "")
          if [ -z "$PREV_TAG" ]; then
            CHANGES=$(git log --pretty=format:"- %s" HEAD)
          else
            CHANGES=$(git log --pretty=format:"- %s" ${PREV_TAG}..HEAD)
          fi
          echo "changes<<EOF" >> $GITHUB_OUTPUT
          echo "$CHANGES" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT

      - name: 교육 자료 패키징
        run: |
          mkdir -p release-package
          cp -r docs/ release-package/
          cp -r template/ release-package/
          cp -r prompt/ release-package/
          cp README.md release-package/
          zip -r cgd-education-${{ github.ref_name }}.zip release-package/

      - name: GitHub Release 생성
        uses: softprops/action-gh-release@v2
        with:
          name: "CGD AI Career Platform ${{ github.ref_name }}"
          body: |
            ## 변경 사항
            ${{ steps.changelog.outputs.changes }}
            
            ## 다운로드
            아래 첨부 파일에서 전체 교육 자료를 다운로드하세요.
            
            ## 사용 방법
            1. zip 파일 다운로드
            2. 압축 해제
            3. docs/ 폴더부터 학습 시작
          files: |
            cgd-education-${{ github.ref_name }}.zip
          draft: false
          prerelease: false

  # 릴리즈 후 학생 알림 (선택)
  notify-students:
    needs: create-release
    runs-on: ubuntu-latest
    
    steps:
      - name: 이메일 알림 발송
        uses: dawidd6/action-send-mail@v3
        with:
          server_address: smtp.gmail.com
          server_port: 587
          username: ${{ secrets.GMAIL_USER }}
          password: ${{ secrets.GMAIL_PASSWORD }}
          subject: "[CGD 플랫폼] 새 교육 자료 ${{ github.ref_name }} 업데이트"
          to: students@cgd.edu
          body: |
            안녕하세요, CGD 취업지원 플랫폼 업데이트 알림입니다.
            
            새 버전(${{ github.ref_name }})이 출시되었습니다.
            플랫폼에서 최신 교육 자료를 확인하세요.
            
            https://cgdplatform-pm7dnqip.manus.space
```

---

## 6. 고급 워크플로우 패턴

### 6.1 Matrix 전략 (병렬 실행)

```yaml
jobs:
  test-multiple-versions:
    strategy:
      matrix:
        python-version: ['3.9', '3.10', '3.11']
        os: [ubuntu-latest, macos-latest]
    
    runs-on: ${{ matrix.os }}
    
    steps:
      - uses: actions/checkout@v4
      - name: Python ${{ matrix.python-version }} 설정
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
```

### 6.2 시크릿 관리

저장소 Settings > Secrets and variables > Actions에서 관리:

```yaml
env:
  # 시크릿 사용
  API_KEY: ${{ secrets.FIRECRAWL_API_KEY }}
  
  # 환경 변수 사용 (공개 가능한 값)
  PLATFORM_URL: ${{ vars.PLATFORM_URL }}
```

### 6.3 캐시 활용으로 속도 향상

```yaml
- name: pip 캐시
  uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

---

## 7. 실습: 첫 번째 Action 만들기

### 실습 목표
Markdown 파일이 push될 때마다 자동으로 목차(TOC)를 업데이트하는 Action을 만들어봅니다.

### Step 1: 워크플로우 파일 생성

저장소에서 `.github/workflows/update-toc.yml` 파일을 생성합니다.

```yaml
name: Markdown TOC 자동 업데이트

on:
  push:
    branches: [ main ]
    paths:
      - 'docs/**/*.md'
      - 'students/**/*.md'

permissions:
  contents: write

jobs:
  update-toc:
    runs-on: ubuntu-latest
    
    steps:
      - name: 저장소 체크아웃
        uses: actions/checkout@v4

      - name: Node.js 설정
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: markdown-toc 설치
        run: npm install -g markdown-toc

      - name: TOC 업데이트
        run: |
          for file in $(find docs -name "*.md"); do
            markdown-toc -i "$file"
            echo "TOC 업데이트 완료: $file"
          done

      - name: 변경사항 커밋
        run: |
          git config user.name 'github-actions[bot]'
          git config user.email 'github-actions[bot]@users.noreply.github.com'
          git add docs/
          git diff --staged --quiet || git commit -m "docs: TOC 자동 업데이트"
          git push
```

### Step 2: 테스트

1. `docs/` 폴더에 아무 Markdown 파일을 수정하고 push
2. GitHub 저장소 > Actions 탭에서 워크플로우 실행 확인
3. 실행 로그에서 각 Step 결과 확인

### Step 3: 결과 확인

```
Actions 탭 > 최신 워크플로우 실행 클릭
  ├── Setup Job ✅
  ├── 저장소 체크아웃 ✅
  ├── Node.js 설정 ✅
  ├── markdown-toc 설치 ✅
  ├── TOC 업데이트 ✅
  └── 변경사항 커밋 ✅
```

### Step 4: 배지 추가

README.md에 워크플로우 상태 배지를 추가합니다:

```markdown
![TOC Update](https://github.com/사용자명/저장소명/actions/workflows/update-toc.yml/badge.svg)
```

---

## 8. 자주 발생하는 오류 해결

| 오류 | 원인 | 해결 방법 |
|------|------|-----------|
| `Permission denied` | 쓰기 권한 없음 | `permissions: contents: write` 추가 |
| `Nothing to commit` | 변경사항 없을 때 오류 | `git diff --staged --quiet \|\| git commit ...` |
| `Secret not found` | 시크릿 미설정 | Settings > Secrets에서 추가 |
| `Rate limit exceeded` | API 호출 한도 초과 | 캐시 사용 또는 호출 간격 조정 |
| `Workflow not triggered` | 이벤트 설정 오류 | `on:` 섹션 YAML 문법 확인 |

---

## 9. 실무 워크플로우 모음

### 월간 취업 현황 리포트 자동 생성

```yaml
name: 월간 취업 현황 리포트

on:
  schedule:
    - cron: '0 9 1 * *'  # 매월 1일 오전 9시

jobs:
  monthly-report:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Python 설정
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install pandas matplotlib
      - name: 리포트 생성
        run: python scripts/monthly_report.py
      - name: 리포트 커밋
        run: |
          git config user.name 'CGD Reporter'
          git config user.email 'reporter@cgd.edu'
          git add reports/monthly/
          git commit -m "월간 리포트 자동 생성 $(date '+%Y-%m')"
          git push
```

---

## 핵심 요약

1. **GitHub Actions** = 코드 저장소 안에서 동작하는 자동화 엔진
2. **YAML 파일** = `.github/workflows/` 폴더에 작성
3. **트리거** = push, PR, schedule, workflow_dispatch 등
4. **Jobs > Steps** 구조로 작업을 순서대로 정의
5. **Secrets** = API 키 등 민감 정보는 반드시 시크릿으로 관리
6. **Marketplace** = https://github.com/marketplace/actions 에서 다양한 Action 검색 가능

---

*CGD AI Career Platform - docs/18-GitHubActions.md*
