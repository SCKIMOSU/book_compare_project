# Book Compare Project

**APIView · GenericAPIView · ModelViewSet** 세 가지 DRF 작성법을
한 프로젝트 안에서 비교하는 풀스택서비스컴퓨팅 실습 프로젝트.

같은 `Book` 모델로 세 방식의 API 를 동시에 띄워, 학생이 직접
URL · 응답 · 코드 라인 수를 비교한다.

---

## 빠른 시작 — 5분 안에 실행

```bash
# 1) 가상환경
python -m venv venv
source venv/bin/activate          # macOS / Linux
# venv\Scripts\activate           # Windows PowerShell

# 2) 패키지 설치
pip install -r requirements.txt

# 3) DB 생성
python manage.py makemigrations book_app
python manage.py migrate

# 4) (선택) 관리자 계정
python manage.py createsuperuser

# 5) 실행
python manage.py runserver
```

브라우저로 [http://localhost:8000/](http://localhost:8000/) 접속 →
세 가지 API 링크가 안내된다.

---

## 접근 가능한 URL

| URL | Level | 설명 |
|-----|-------|------|
| [http://localhost:8000/](http://localhost:8000/) | — | 안내 페이지 |
| [http://localhost:8000/api/v1/books/](http://localhost:8000/api/v1/books/) | 1 | **APIView** (직접 작성) |
| [http://localhost:8000/api/v2/books/](http://localhost:8000/api/v2/books/) | 2 | **GenericAPIView** (조합) |
| [http://localhost:8000/api/v3/books/](http://localhost:8000/api/v3/books/) | 3 | **ModelViewSet** (자동) |
| [http://localhost:8000/api/v3/](http://localhost:8000/api/v3/) | 3 | Router API root |
| [http://localhost:8000/api/v3/books/1/toggle/](http://localhost:8000/api/v3/books/1/toggle/) | 3 | `@action` 커스텀 액션 (POST) |
| [http://localhost:8000/admin/](http://localhost:8000/admin/) | — | Django 관리자 |

---

## 디렉토리 구조

```
book_compare_project/         ← 프로젝트 루트 (manage.py 위치)
├── manage.py
├── requirements.txt
├── README.md                 ← 이 파일
│
├── book_compare/             ← 프로젝트 설정 패키지
│   ├── __init__.py
│   ├── settings.py           ← INSTALLED_APPS, DRF 설정 완료
│   ├── urls.py               ← 루트 안내 페이지 + book_app include
│   ├── asgi.py
│   └── wsgi.py
│
└── book_app/                 ← 실습 앱
    ├── models.py             ← Book 모델 (세 방식 공통)
    ├── serializers.py        ← BookSerializer (세 방식 공통)
    ├── views_apiview.py      ← Level 1 (39 줄)
    ├── views_generic.py      ← Level 2 (9 줄)
    ├── views_viewset.py      ← Level 3 (14 줄)
    ├── urls.py               ← v1, v2, v3 모두 라우팅
    ├── apps.py
    ├── tests.sh              ← 세 방식 응답 동일성 검증
    └── migrations/
```

---

## 실습 시나리오

### 시나리오 A — 동일성 검증

세 API 가 정말 같은 응답을 내는지 확인:

```bash
# 도서 1건 등록 (Level 3 로)
curl -X POST http://localhost:8000/api/v3/books/ \
     -H "Content-Type: application/json" \
     -d '{"title":"DRF 실전","author":"홍길동","published_year":2024,"is_available":true}'

# 세 방식 모두로 조회 — 결과 동일해야 정답
curl http://localhost:8000/api/v1/books/
curl http://localhost:8000/api/v2/books/
curl http://localhost:8000/api/v3/books/

# 또는 한방에
bash book_app/tests.sh
```

### 시나리오 B — 라인 수 비교

```bash
# 순수 코드 라인 수 (주석 · docstring 제외)
for f in book_app/views_*.py; do
  echo -n "$f: "
  python3 -c "
import ast
src = open('$f').read()
tree = ast.parse(src)
for node in ast.walk(tree):
    if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)) and ast.get_docstring(node):
        node.body = node.body[1:]
code = ast.unparse(tree)
print(len([l for l in code.splitlines() if l.strip() and not l.strip().startswith('#')]))
"
done
```

예상 결과:
```
book_app/views_apiview.py: 39
book_app/views_generic.py: 9
book_app/views_viewset.py: 14
```

### 시나리오 C — @action 의 강력함

Level 3 만 가능한 커스텀 액션 호출:

```bash
# is_available 토글 (Level 3 전용)
curl -X POST http://localhost:8000/api/v3/books/1/toggle/
```

`Level 1, 2 에서는 이 엔드포인트가 없다` 는 점이 핵심.

---

## 트러블슈팅

**Q. `ModuleNotFoundError: No module named 'rest_framework'`**
→ 가상환경 활성화 안 됨. `source venv/bin/activate` 다시 실행.

**Q. `OperationalError: no such table: book_app_book`**
→ 마이그레이션 안 함. `python manage.py makemigrations book_app && python manage.py migrate`

**Q. POST 시 `CSRF verification failed`**
→ 브라우저 폼이 아니라 curl/Postman 으로 호출. DRF Browsable API 의 폼을 쓰려면 로그인 필요.

**Q. `AssertionError: 'BookViewSet' should ... basename`**
→ `urls.py` 의 `router.register()` 에 `basename='book'` 추가하거나
   ViewSet 에 `queryset` 명시 (이미 되어 있음).

---

## 참고

이 프로젝트는 다음 강의 자료와 함께 사용한다:

- `Django_CBV_to_DRF_Generic_View.pptx` — 24 장 강의 슬라이드
- Slide 13–17 (실습 비교 4 장) 이 이 프로젝트와 직접 대응

---

© 김상철 · 국민대학교 소프트웨어학부 · 풀스택서비스컴퓨팅
