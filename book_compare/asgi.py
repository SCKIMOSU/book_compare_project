"""ASGI config for book_compare project."""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_compare.settings')
application = get_asgi_application()
