# views_viewset.py
"""
[Level 3] ModelViewSet + Router 로 Book CRUD 구현

특징
- 한 클래스로 5개 HTTP 동작 (list / create / retrieve / update / partial_update / destroy)
- URL 도 Router 가 자동 생성
- @action 으로 커스텀 액션 추가 가능
- 코드 라인 수: 7 줄 (보너스 @action 포함 시 14 줄)
"""
from rest_framework             import viewsets
from rest_framework.decorators  import action
from rest_framework.response    import Response

from .models      import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    URL 자동 생성 (router.register('books', BookViewSet) 등록 시)
      GET    /api/v3/books/                → list
      POST   /api/v3/books/                → create
      GET    /api/v3/books/<pk>/           → retrieve
      PUT    /api/v3/books/<pk>/           → update
      PATCH  /api/v3/books/<pk>/           → partial_update
      DELETE /api/v3/books/<pk>/           → destroy
      POST   /api/v3/books/<pk>/toggle/    → toggle (커스텀 액션)
    """
    queryset         = Book.objects.all()
    serializer_class = BookSerializer

    # 보너스 — ViewSet 만의 비대칭적 강점
    @action(detail=True, methods=['post'])
    def toggle(self, request, pk=None):
        """ 대출 가능 상태(is_available) 토글 """
        book = self.get_object()
        book.is_available = not book.is_available
        book.save()
        return Response({'id': book.id, 'is_available': book.is_available})
