# views_generic.py
"""
[Level 2] GenericAPIView (concrete generic views) 로 Book CRUD 구현

특징
- queryset · serializer_class 만 지정하면 CRUD 자동
- ListCreateAPIView : GET·POST
- RetrieveUpdateDestroyAPIView : GET·PUT·PATCH·DELETE
- 404 처리·페이징·필터 자동
- 코드 라인 수: 12 줄
"""
from rest_framework import generics

from .models      import Book
from .serializers import BookSerializer


class BookListCreate(generics.ListCreateAPIView):
    """ GET / POST  /api/v2/books/ """
    queryset         = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """ GET / PUT / PATCH / DELETE  /api/v2/books/<pk>/ """
    queryset         = Book.objects.all()
    serializer_class = BookSerializer
