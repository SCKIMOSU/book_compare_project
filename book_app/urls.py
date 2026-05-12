# urls.py
"""
세 방식 모두를 동시에 라우팅한다.
같은 데이터에 대해 v1 / v2 / v3 응답이 동일한지 학생이 직접 확인할 수 있다.

    /api/v1/books/         APIView         (Level 1)
    /api/v2/books/         GenericAPIView  (Level 2)
    /api/v3/books/         ModelViewSet    (Level 3, Router 로 자동)
"""
from django.urls            import path, include
from rest_framework.routers import DefaultRouter

# Level 1, 2 — path() 로 직접 등록
from .views_apiview import (
    BookListCreate as APIViewListCreate,
    BookDetail     as APIViewDetail,
)
from .views_generic import (
    BookListCreate as GenericListCreate,
    BookDetail     as GenericDetail,
)
# Level 3 — Router 가 자동 등록
from .views_viewset import BookViewSet


# Level 3 — Router 구성 (이 한 줄로 6개 URL 자동 생성)
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')


urlpatterns = [
    # ---------- Level 1 : APIView ----------
    path('api/v1/books/',           APIViewListCreate.as_view(), name='v1-book-list'),
    path('api/v1/books/<int:pk>/',  APIViewDetail.as_view(),     name='v1-book-detail'),

    # ---------- Level 2 : GenericAPIView ----------
    path('api/v2/books/',           GenericListCreate.as_view(), name='v2-book-list'),
    path('api/v2/books/<int:pk>/',  GenericDetail.as_view(),     name='v2-book-detail'),

    # ---------- Level 3 : ModelViewSet + Router ----------
    path('api/v3/', include(router.urls)),
]
