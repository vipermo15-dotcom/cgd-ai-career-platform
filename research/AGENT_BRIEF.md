# 교육생별 채용공고 리서치 브리프 (기준일 2026-09-30)

대상 교육생마다 **현재 접수 중인 채용공고 정확히 10건**을 조사해 `research/data/<이름>.json`에 저장한다.

## 절차
1. `docs/<이름>/` 의 모든 .md를 읽고 프로필(희망직무, 업종, 툴, 근무형태, 희망지역, 추천직무/취업처, 부족한 점)을 파악한다. 문서에 없는 정보는 추측하지 않는다.
2. Firecrawl 검색/스크랩(mcp__Firecrawl__firecrawl_search, firecrawl_scrape; 필요 시 ToolSearch로 로드)으로 사람인·잡코리아·원티드·잡플래닛·캐치·기업 채용페이지에서 공고를 찾는다.
3. 각 공고는 URL을 실제로 스크랩해 **존재·마감 전(또는 상시채용)·직무 내용**을 확인한다. 확인 못 한 항목은 넣지 않는다. 마감 지난 공고, 경력 3년 이상 요구 공고는 제외(신입/경력무관/1~2년 위주). 회사 중복을 최소화하고 직무 다양성을 둔다.
4. 절대 지어내지 않는다. 급여·마감일 등 확인 못 하면 `null`. 10건을 못 채우면 채운 만큼만 저장하고 `shortfall` 사유를 적는다.

## JSON 스키마
{
 "name": "이름",
 "profile_summary": "2~3문장, 문서 근거",
 "target_roles": ["..."],
 "researched_at": "2026-09-30",
 "shortfall": null,
 "jobs": [{
  "rank": 1,
  "company": "", "title": "", "location": "", "employment_type": "",
  "experience": "", "salary": null, "deadline": "YYYY-MM-DD 또는 상시 또는 null",
  "required": ["..."], "preferred": ["..."], "tools": ["..."],
  "url": "확인한 공고 URL", "source": "사람인 등",
  "match_score": 0-100, "match_reason": "프로필 근거 1~2문장",
  "gap": "부족/보완할 점", "prep_tip": "지원 전 준비 포인트"
 }]
}
rank는 지원 우선순위(1이 최우선). 파일 저장 후 `python3 -c "import json;json.load(open(...))"`로 유효성 확인.
git 커밋/푸시는 하지 않는다(부모 세션이 처리).
