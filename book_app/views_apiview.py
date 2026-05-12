# views_apiview.py
"""
[Level 1] APIView 로 Book CRUD 직접 구현

특징
- HTTP 메서드(get·post·put·patch·delete)를 모두 직접 작성
- queryset · serializer 가 강제되지 않음 (자유도 최고)
- URL 도 path() 로 명시 등록 필요
- 코드 라인 수: 약 47 줄
"""
from rest_framework.views    import APIView
from rest_framework.response import Response
from rest_framework          import status
from django.shortcuts        import get_object_or_404

from .models      import Book
from .serializers import BookSerializer


class BookListCreate(APIView):
    """ GET  /api/v1/books/      목록 조회
        POST /api/v1/books/      새 도서 등록 """

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    """ GET    /api/v1/books/<pk>/     단일 조회
        PUT    /api/v1/books/<pk>/     전체 수정
        PATCH  /api/v1/books/<pk>/     부분 수정
        DELETE /api/v1/books/<pk>/     삭제 """

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return Response(BookSerializer(book).data)

    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
