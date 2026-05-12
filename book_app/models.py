# models.py
"""
Book 모델 — 세 방식(APIView / GenericAPIView / ModelViewSet)이 공통으로 사용.
"""
from django.db import models


class Book(models.Model):
    title          = models.CharField(max_length=100)
    author         = models.CharField(max_length=100)
    published_year = models.IntegerField()
    is_available   = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']
        verbose_name = '도서'
        verbose_name_plural = '도서 목록'

    def __str__(self):
        return f"{self.title} ({self.author})"
