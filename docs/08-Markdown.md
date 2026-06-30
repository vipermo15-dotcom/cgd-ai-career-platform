# 08. Markdown 완전 정복

> Markdown으로 아름다운 포트폴리오 문서를 작성합니다.

---

## 목차

1. [Markdown이란?](#1-markdown이란)
2. [기본 문법](#2-기본-문법)
3. [중급 문법](#3-중급-문법)
4. [고급 활용](#4-고급-활용)
5. [포트폴리오 문서 작성](#5-포트폴리오-문서-작성)
6. [GitHub에서의 Markdown](#6-github에서의-markdown)
7. [Markdown 편집 도구](#7-markdown-편집-도구)

---

## 1. Markdown이란?

Markdown은 2004년 John Gruber가 만든 경량 마크업 언어입니다.

### 특징

- **단순함**: 기호 몇 개만으로 서식 표현
- **범용성**: GitHub, Notion, Claude, VSCode 등 어디서나 사용
- **가독성**: 서식 없이도 텍스트 자체가 읽기 쉬움
- **변환**: HTML, PDF 등으로 쉽게 변환

### 파일 확장자

Markdown 파일의 확장자: `.md` 또는 `.markdown`

### Markdown을 사용하는 곳

- **GitHub**: README, Issues, PR, Wiki
- **Notion**: 모든 콘텐츠
- **Claude**: 대화 출력
- **VSCode**: 문서 작성
- **Jekyll/Hugo**: 정적 사이트 생성
- **포트폴리오**: 텍스트 문서

---

## 2. 기본 문법

### 제목 (Headings)

```markdown
# 제목 1 (H1) - 가장 큰 제목
## 제목 2 (H2)
### 제목 3 (H3)
#### 제목 4 (H4)
##### 제목 5 (H5)
###### 제목 6 (H6) - 가장 작은 제목
```

**렌더링 결과**:
# 제목 1
## 제목 2
### 제목 3

> 팁: `#` 뒤에 반드시 공백 하나를 추가하세요.

### 단락과 줄바꿈

```markdown
이것은 첫 번째 단락입니다.

이것은 두 번째 단락입니다.
(빈 줄 하나로 단락 구분)

이것은 줄바꿈입니다.  
(문장 끝에 공백 2개 + Enter)
```

### 강조 (Emphasis)

```markdown
**굵은 글씨** (Bold)
*기울임* (Italic)
***굵고 기울임*** (Bold + Italic)
~~취소선~~ (Strikethrough)
`인라인 코드` (Inline Code)
```

**결과**: **굵은 글씨** | *기울임* | ***굵고 기울임*** | ~~취소선~~ | `인라인 코드`

### 목록 (Lists)

**순서 없는 목록 (Unordered List)**:
```markdown
- 항목 1
- 항목 2
  - 하위 항목 2-1
  - 하위 항목 2-2
- 항목 3

* 별표로도 가능
+ 플러스로도 가능
```

**순서 있는 목록 (Ordered List)**:
```markdown
1. 첫 번째
2. 두 번째
3. 세 번째
   1. 하위 항목
   2. 하위 항목
```

**체크박스 (Task List)**:
```markdown
- [x] 완료된 항목
- [ ] 미완료 항목
- [x] 또 다른 완료 항목
```

### 링크와 이미지

```markdown
[링크 텍스트](https://example.com)
[링크 + 툴팁](https://example.com "툴팁 텍스트")

![이미지 대체텍스트](이미지URL)
![로컬 이미지](../assets/image.png)

[클릭 가능한 이미지](링크URL)
```

---

## 3. 중급 문법

### 인용문 (Blockquote)

```markdown
> 이것은 인용문입니다.
> 
> 여러 줄의 인용문
>> 중첩 인용문

> **중요**: 인용문 안에서 다른 서식도 사용 가능합니다.
```

**결과**:
> 이것은 인용문입니다.
> 
> 여러 줄의 인용문
>> 중첩 인용문

### 코드 블록

**인라인 코드**:
```markdown
`git commit -m "메시지"` 명령어를 사용하세요.
```

**코드 블록 (펜스)**:
````markdown
```python
def hello():
    print("안녕하세요!")
```

```bash
git add .
git commit -m "커밋 메시지"
```

```javascript
const greeting = "안녕하세요!";
console.log(greeting);
```
````

지원 언어: `python`, `javascript`, `bash`, `html`, `css`, `java`, `json`, `markdown`, `sql` 등

### 표 (Tables)

```markdown
| 헤더 1 | 헤더 2 | 헤더 3 |
|--------|--------|--------|
| 내용 1 | 내용 2 | 내용 3 |
| 내용 4 | 내용 5 | 내용 6 |

| 왼쪽 정렬 | 가운데 정렬 | 오른쪽 정렬 |
|:---------|:-----------:|------------:|
| 내용 | 내용 | 내용 |
```

**결과**:

| 왼쪽 정렬 | 가운데 정렬 | 오른쪽 정렬 |
|:---------|:-----------:|------------:|
| 내용 | 내용 | 내용 |

### 수평선 (Horizontal Rule)

```markdown
---
***
___
```

### 이스케이프 (Escape)

Markdown 기호를 텍스트로 표시하려면 백슬래시 사용:

```markdown
\*별표를 그대로 표시\*
\# 샵을 그대로 표시
```

---

## 4. 고급 활용

### HTML 직접 사용

Markdown 안에서 HTML 태그를 사용할 수 있습니다:

```markdown
<div align="center">
  <h1>가운데 정렬 제목</h1>
  <p>가운데 정렬 텍스트</p>
</div>

<details>
<summary>접기/펼치기 클릭!</summary>

여기에 숨겨진 내용이 들어갑니다.
Markdown 문법도 사용 가능합니다.

</details>
```

### 배지 (Badges)

GitHub README에 자주 사용하는 배지:

```markdown
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![GitHub stars](https://img.shields.io/github/stars/사용자명/저장소명)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

<!-- 기술 스택 배지 -->
![Photoshop](https://img.shields.io/badge/Photoshop-31A8FF?style=flat&logo=adobe-photoshop&logoColor=white)
![Figma](https://img.shields.io/badge/Figma-F24E1E?style=flat&logo=figma&logoColor=white)
```

### 각주 (Footnotes)

```markdown
여기에 각주가 있습니다.[^1]
다른 각주도 있습니다.[^note]

[^1]: 이것이 각주 내용입니다.
[^note]: 이것이 named 각주입니다.
```

### 수식 (Math)

GitHub에서 수식 지원:

```markdown
인라인 수식: $E = mc^2$

블록 수식:
$$
\sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n
$$
```

---

## 5. 포트폴리오 문서 작성

### 포트폴리오 프로젝트 README 템플릿

```markdown
# 🎨 [프로젝트 이름]

[프로젝트 설명 1-2문장]

## 📋 프로젝트 개요

| 항목 | 내용 |
|------|------|
| **프로젝트 유형** | 브랜딩 / 편집 / UI-UX / 영상 |
| **제작 기간** | 2024년 1월 ~ 2024년 2월 |
| **사용 툴** | Adobe Illustrator, Photoshop |
| **역할** | 전체 디자인 / 기획 |

## 🎯 프로젝트 목표

- 목표 1
- 목표 2
- 목표 3

## 🖥️ 작업 결과물

![메인 이미지](images/main.jpg)

### 세부 작업물

| 로고 디자인 | 명함 디자인 |
|:---:|:---:|
| ![로고](images/logo.jpg) | ![명함](images/business-card.jpg) |

## 💡 디자인 프로세스

### 1단계: 리서치
[기획 과정 설명]

### 2단계: 스케치
[초안 작업 과정]

### 3단계: 제작
[실제 제작 과정]

### 4단계: 피드백 및 수정
[수정 과정]

## 🛠️ 사용 기술

- **Adobe Illustrator**: 로고, 아이콘, 벡터 그래픽
- **Adobe Photoshop**: 이미지 편집, 목업
- **Adobe InDesign**: 레이아웃, 인쇄물

## 📚 배운 점

이 프로젝트를 통해 배운 점:
- 배운 점 1
- 배운 점 2

## 📁 파일 목록

```
프로젝트폴더/
├── source/          # 원본 파일 (ai, psd)
├── exports/         # 최종 출력 파일
├── mockups/         # 목업 이미지
└── presentation/    # 프레젠테이션 파일
```
```

---

## 6. GitHub에서의 Markdown

### GitHub Flavored Markdown (GFM)

GitHub는 표준 Markdown에 추가 기능을 제공합니다:

**자동 링크**:
```markdown
https://github.com/cgd-ai  # 자동으로 링크 변환
```

**멘션**:
```markdown
@사용자명  # 사용자 태그
#123      # Issue/PR 번호 링크
```

**이모지**:
```markdown
:rocket: :tada: :art: :pencil: :book:
```

**결과**: 🚀 🎉 🎨 ✏️ 📖

### README.md 프로필 꾸미기

GitHub 통계 카드:

```markdown
![GitHub Stats](https://github-readme-stats.vercel.app/api?username=사용자명&show_icons=true&theme=default)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=사용자명&layout=compact)
```

---

## 7. Markdown 편집 도구

### VSCode에서 Markdown 편집

- **미리보기**: `Ctrl+Shift+V`
- **분할 미리보기**: `Ctrl+K V`
- **자동 완성**: `Ctrl+Space`

**추천 확장 프로그램**:
- `Markdown Preview Enhanced`: 고급 미리보기
- `Markdown All in One`: 단축키, 목차 생성
- `markdownlint`: 문법 오류 체크

### Markdown 목차 자동 생성

VSCode에서 "Markdown All in One" 확장 설치 후:
- `Ctrl+Shift+P` → "Markdown All in One: Create Table of Contents"
- 문서 상단에 자동으로 목차 생성

### Typora (대안 편집기)

[typora.io](https://typora.io) - WYSIWYG Markdown 편집기
- 작성하면서 바로 렌더링 확인
- 이미지 드래그 앤 드롭 지원
- PDF 내보내기

---

## Markdown 치트시트

| 기능 | 문법 |
|------|------|
| H1 제목 | `# 제목` |
| H2 제목 | `## 제목` |
| H3 제목 | `### 제목` |
| 굵게 | `**텍스트**` |
| 기울임 | `*텍스트*` |
| 취소선 | `~~텍스트~~` |
| 인라인 코드 | `` `코드` `` |
| 코드 블록 | ` ```언어\n코드\n``` ` |
| 링크 | `[텍스트](URL)` |
| 이미지 | `![대체텍스트](URL)` |
| 목록 | `- 항목` |
| 번호 목록 | `1. 항목` |
| 체크박스 | `- [x] 항목` |
| 인용 | `> 인용문` |
| 표 | `\| 헤더 \|` |
| 수평선 | `---` |

---

*이전 문서: [07-GitHubProjects.md](07-GitHubProjects.md) | 다음 문서: [09-AI프롬프트.md](09-AI프롬프트.md) →*
