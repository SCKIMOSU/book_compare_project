# apps.py
from django.apps import AppConfig


class BookAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book_app'
    verbose_name = '도서 CRUD 비교 예제'
