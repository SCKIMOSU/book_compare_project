# `book_app` — APIView · GenericAPIView · ModelViewSet 비교 예제

풀스택서비스컴퓨팅 강의 실습 자료.
**같은 Book CRUD API 를 세 가지 추상화 레벨로 구현**하여 직접 비교한다.

## 파일 구조

```
book_app/
├── models.py            ← Book 모델 (공통)
├── serializers.py       ← BookSerializer (공통)
├── views_apiview.py     ← Level 1 : APIView          (47줄)
├── views_generic.py     ← Level 2 : GenericAPIView   (12줄)
├── views_viewset.py     ← Level 3 : ModelViewSet     ( 7줄)
├── urls.py              ← 세 방식을 v1 / v2 / v3 로 동시 라우팅
├── apps.py
├── tests.sh             ← 세 방식 응답 동일성 검증 스크립트
└── README.md            ← 이 파일
```

## 라인 수 비교

| Level | View 클래스 | views.py 라인 | URL 등록 | 직접 작성해야 하는 메서드 |
|-------|------------|---------------|----------|--------------------------|
| 1     | `APIView`           | **47**  | `path()` × 2 | `get, post, get, put, patch, delete` (7개) |
| 2     | `GenericAPIView`    | **12**  | `path()` × 2 | 없음 (queryset, serializer_class 만) |
| 3     | `ModelViewSet`      | **7**   | `router.register()` × 1 | 없음 |

## 설치 (기존 Django 프로젝트에 추가)

1. 이 폴더를 프로젝트 루트에 복사.
2. `settings.py` 의 `INSTALLED_APPS` 에 추가:
    ```python
    INSTALLED_APPS = [
        ...
        'rest_framework',
        'book_app',
    ]
    ```
3. 프로젝트 `urls.py` 에 include:
    ```python
    from django.urls import path, include
    urlpatterns = [
        ...
        path('', include('book_app.urls')),
    ]
    ```
4. 마이그레이션:
    ```bash
    python manage.py makemigrations book_app
    python manage.py migrate
    ```

## 실행 및 검증

```bash
python manage.py runserver
bash book_app/tests.sh          # 세 방식 동일 응답 확인
```

브라우저로 확인:

| URL                                       | Level | 설명 |
|-------------------------------------------|-------|------|
| http://localhost:8000/api/v1/books/       | 1     | APIView Browsable API |
| http://localhost:8000/api/v2/books/       | 2     | GenericAPIView Browsable API |
| http://localhost:8000/api/v3/books/       | 3     | ModelViewSet Browsable API |
| http://localhost:8000/api/v3/             | 3     | Router 가 자동 생성한 API root |

## 학습 포인트

1. **Level 1 의 7 개 메서드가 Level 3 에서는 사라진다** — 추상화의 위력.
2. **Level 3 만 가능한 일**:
    - `router.register()` 한 줄로 6 개 URL 자동 생성
    - `@action` 으로 `/books/<pk>/toggle/` 같은 커스텀 액션 추가
    - API root UI 자동 제공
3. **응답 JSON 은 셋 다 동일** — 학생이 직접 `tests.sh` 로 확인.
4. **자유도는 반비례** — 자동화가 강해질수록 관례를 따라야 한다.

## 함정 문제

> Q. `views_viewset.py` 에서 `queryset` 을 지우면 어떤 오류가 나는가?

A. Router 가 `basename` 을 추론하기 위해 `queryset.model` 을 참조하므로
   ```
   AssertionError: 'BookViewSet' should either include a `queryset` attribute,
   or use the `get_queryset()` method.
   ```
   에러가 발생한다. 회피하려면 `router.register(..., basename='book')` 처럼
   `basename` 을 명시해야 한다.

---

© 김상철 · 국민대학교 소프트웨어학부 · 풀스택서비스컴퓨팅
