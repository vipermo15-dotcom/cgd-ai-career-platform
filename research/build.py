#!/usr/bin/env python3
"""research/data/<이름>.json -> research/out/<이름>_추천채용공고.html (단독 실행, 외부 의존 없음)."""
import json, glob, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
E = html.escape
EXCLUDE = {"장아름", "김규연", "박민서"}  # 배포 제외 대상(요청). 조사 원본 data/는 보존

CSS = """
:root{--bg:#f6f7f9;--card:#fff;--ink:#1c2230;--sub:#5d6675;--line:#e3e6ec;--acc:#2f5bea;--ok:#12805c;--warn:#b45309}
@media(prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#12151b;--card:#1b2029;--ink:#e8ebf1;--sub:#9aa3b2;--line:#2b3240;--acc:#7c9cff;--ok:#4cc79a;--warn:#f0a955;color-scheme:dark}}
:root[data-theme=dark]{--bg:#12151b;--card:#1b2029;--ink:#e8ebf1;--sub:#9aa3b2;--line:#2b3240;--acc:#7c9cff;--ok:#4cc79a;--warn:#f0a955;color-scheme:dark}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 -apple-system,'Apple SD Gothic Neo','Malgun Gothic',sans-serif}
.wrap{max-width:860px;margin:0 auto;padding:24px 16px 64px;min-width:0}dd{min-width:0;overflow-wrap:anywhere}
h1{font-size:22px;margin:0 0 4px}.meta{color:var(--sub);font-size:13px}
.box{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;margin:16px 0}
.tools{display:flex;gap:8px;flex-wrap:wrap;margin:16px 0}
.tools input,.tools select{padding:8px 10px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink);font:inherit}
.tools input{flex:1;min-width:160px}
.job{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;margin:12px 0}
.top{display:flex;justify-content:space-between;gap:12px;align-items:flex-start}
.rank{font-size:12px;color:var(--acc);font-weight:700}.co{font-weight:700;font-size:17px}.tt{color:var(--sub)}
.score{font-weight:700;color:var(--ok);white-space:nowrap}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}.chip{font-size:12px;border:1px solid var(--line);border-radius:999px;padding:2px 9px;color:var(--sub)}
dl{display:grid;grid-template-columns:96px 1fr;gap:4px 12px;margin:10px 0;font-size:14px}dt{color:var(--sub)}dd{margin:0}
.gap{color:var(--warn)}a.btn{display:inline-block;margin-top:8px;padding:7px 14px;border-radius:8px;background:var(--acc);color:#fff;text-decoration:none;font-size:14px}
label.done{font-size:13px;color:var(--sub);margin-left:12px}
.job.applied{opacity:.6}.foot{color:var(--sub);font-size:12px;margin-top:32px}
@media print{.tools,label.done{display:none}.job{break-inside:avoid}}
"""

JS = """
const KEY=document.querySelector('[data-key]').dataset.key;let st={};
try{st=JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){}
const jobs=[...document.querySelectorAll('.job')];
function save(){try{localStorage.setItem(KEY,JSON.stringify(st))}catch(e){}}
jobs.forEach(j=>{const c=j.querySelector('input[type=checkbox]');c.checked=!!st[j.dataset.i];j.classList.toggle('applied',c.checked);
c.onchange=()=>{st[j.dataset.i]=c.checked;j.classList.toggle('applied',c.checked);save()}});
const q=document.getElementById('q'),s=document.getElementById('s');
function f(){jobs.forEach(j=>{const ok=j.textContent.toLowerCase().includes(q.value.toLowerCase());j.style.display=ok?'':'none'});
const arr=jobs.slice().sort((a,b)=>s.value=='score'?b.dataset.score-a.dataset.score:a.dataset.i-b.dataset.i);arr.forEach(x=>x.parentNode.appendChild(x))}
q.oninput=f;s.onchange=f;
"""


def li(items):
    return ", ".join(E(str(x)) for x in items) if items else "-"


def job_html(j):
    i = j.get("rank", 0)
    url = j.get("url") or ""
    link = f'<a class="btn" href="{E(url)}" target="_blank" rel="noopener noreferrer">공고 보러가기 ({E(j.get("source") or "출처")})</a>' if url.startswith("http") else ""
    dl = [
        ("근무지", j.get("location")), ("고용형태", j.get("employment_type")), ("경력", j.get("experience")),
        ("급여", j.get("salary") or "공고 확인"), ("마감", j.get("deadline") or "공고 확인"),
        ("필수", li(j.get("required"))), ("우대", li(j.get("preferred"))), ("툴", li(j.get("tools"))),
        ("추천 이유", j.get("match_reason")), ("보완할 점", j.get("gap")), ("준비 팁", j.get("prep_tip")),
    ]
    rows = "".join(
        f'<dt>{k}</dt><dd class="{"gap" if k=="보완할 점" else ""}">{v if k in ("필수","우대","툴") else E(str(v or "-"))}</dd>'
        for k, v in dl
    )
    return f"""<article class="job" data-i="{i}" data-score="{j.get('match_score',0)}">
<div class="top"><div><div class="rank">우선순위 {i}</div><div class="co">{E(j.get('company',''))}</div><div class="tt">{E(j.get('title',''))}</div></div>
<div class="score">적합도 {j.get('match_score','-')}</div></div>
<dl>{rows}</dl>{link}<label class="done"><input type="checkbox"> 지원 완료</label></article>"""


def build(path):
    d = json.load(open(path, encoding="utf-8"))
    name = d["name"]
    jobs = "\n".join(job_html(j) for j in sorted(d["jobs"], key=lambda x: x.get("rank", 99)))
    note = f'<div class="box gap">참고: {E(d["shortfall"])}</div>' if d.get("shortfall") else ""
    doc = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>{E(name)} 추천 채용공고</title><style>{CSS}</style></head>
<body data-key="cgd-jobs-{E(name)}"><div class="wrap">
<h1>{E(name)} 님 추천 채용공고 {len(d['jobs'])}선</h1>
<div class="meta">조사 기준일 {E(d.get('researched_at',''))} · 서울시기술교육원 컴퓨터그래픽디자인과 · 본인 전용 자료</div>
<div class="box"><b>프로필 요약</b><br>{E(d.get('profile_summary',''))}<div class="chips">{''.join(f'<span class="chip">{E(r)}</span>' for r in d.get('target_roles',[]))}</div></div>
{note}
<div class="tools"><input id="q" placeholder="회사·직무·툴 검색"><select id="s"><option value="rank">우선순위순</option><option value="score">적합도순</option></select></div>
{jobs}
<div class="foot">공고는 수시로 마감·변경됩니다. 지원 전 반드시 원문 공고에서 마감일과 조건을 다시 확인하세요. 이 파일은 개인 진로 정보를 포함하므로 타인에게 공유하지 마세요. 지원 완료 체크는 이 브라우저에만 저장됩니다.</div>
</div><script>{JS}</script></body></html>"""
    body = doc[doc.index('<div class="wrap">'):doc.index('</script>') + 9]
    frag = f'<title>{E(name)} 추천 채용공고</title><style>{CSS}body{{background:var(--bg);color:var(--ink)}}</style>\n<div data-key="cgd-jobs-{E(name)}">{body}</div>'
    os.makedirs(os.path.join(HERE, "artifact"), exist_ok=True)
    open(os.path.join(HERE, "artifact", f"{name}.html"), "w", encoding="utf-8").write(frag)
    out = os.path.join(HERE, "out", f"{name}_추천채용공고.html")
    open(out, "w", encoding="utf-8").write(doc)
    return out, len(d["jobs"])


if __name__ == "__main__":
    for p in sorted(glob.glob(os.path.join(HERE, "data", "*.json"))):
        if json.load(open(p, encoding="utf-8"))["name"] in EXCLUDE:
            continue
        print(build(p))
