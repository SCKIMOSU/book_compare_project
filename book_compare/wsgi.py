"""WSGI config for book_compare project."""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_compare.settings')
application = get_wsgi_application()
