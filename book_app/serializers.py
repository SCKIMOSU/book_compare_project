# serializers.py
"""
BookSerializer — 세 방식 공통 사용.
ModelForm 의 자리에 ModelSerializer 가 들어선다.
"""
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Book
        fields = ['id', 'title', 'author', 'published_year', 'is_available']
        read_only_fields = ['id']
