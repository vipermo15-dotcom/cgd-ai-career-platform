# CGD AI Career Platform 기여 가이드

이 문서는 CGD AI Career Platform에 기여하는 방법을 안내합니다.

---

## 기여할 수 있는 방법

### 1. 오탈자·내용 오류 수정
문서에서 오탈자나 잘못된 정보를 발견했다면 PR을 제출해주세요.

### 2. 내용 보완
기존 문서의 내용을 더 명확하게 설명하거나 예시를 추가할 수 있습니다.

### 3. 새로운 프롬프트 추가
취업 준비에 유용한 AI 프롬프트를 `prompt/` 폴더에 추가할 수 있습니다.

### 4. 예제 파일 추가
실제 사용 가능한 예제를 `examples/` 폴더에 추가할 수 있습니다.

### 5. 버그 신고
문서 링크 오류, 내용 불일치 등을 [Issues](https://github.com/cgd-ai/cgd-ai-career-platform/issues)에 등록해주세요.

---

## 기여 절차

### 1단계: 저장소 Fork

GitHub에서 Fork 버튼을 클릭하여 본인 계정으로 복사합니다.

### 2단계: 로컬로 Clone

```bash
git clone https://github.com/[본인계정]/cgd-ai-career-platform.git
cd cgd-ai-career-platform
```

### 3단계: 브랜치 생성

```bash
# 기능 추가
git checkout -b feature/프롬프트-추가

# 버그 수정
git checkout -b fix/오탈자-수정

# 문서 개선
git checkout -b docs/Week05-내용-보완
```

### 4단계: 변경사항 작성

파일을 수정하거나 새 파일을 추가합니다.

### 5단계: 커밋

```bash
git add .
git commit -m "docs: Week05 Firecrawl 실습 내용 보완"
```

### 6단계: Push

```bash
git push origin feature/프롬프트-추가
```

### 7단계: Pull Request 생성

GitHub에서 Pull Request를 생성합니다.

---

## 커밋 메시지 규칙

```
[타입]: [설명]

타입:
- feat: 새로운 기능 추가
- fix: 버그 수정
- docs: 문서 수정
- style: 형식 변경 (내용 변경 없음)
- refactor: 구조 변경
- chore: 기타 변경사항
```

예시:
```
docs: Claude 프롬프트 10개 추가
feat: Week11 면접 질문 예시 추가
fix: 01-Git설치.md 링크 오류 수정
```

---

## 문서 작성 규칙

1. **언어**: 한국어 기본, 기술 용어는 영어 병기 (예: 저장소(Repository))
2. **파일 형식**: Markdown (.md)
3. **인코딩**: UTF-8
4. **줄바꿈**: LF (Unix 스타일)
5. **들여쓰기**: 공백 2칸 또는 4칸
6. **이미지**: `assets/` 폴더에 저장, 상대 경로로 참조

---

## PR 검토 기준

- 내용의 정확성
- 한국어 맞춤법
- 실습 가능 여부 (명령어, 프롬프트 등)
- 기존 문서와의 일관성

---

## 질문이 있다면

[Issues](https://github.com/cgd-ai/cgd-ai-career-platform/issues)에 질문을 등록해주세요.

감사합니다!
