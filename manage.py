#!/usr/bin/env python
"""Django manage.py — 모든 관리 명령의 진입점."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_compare.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django 를 import 할 수 없습니다. "
            "가상환경을 활성화했는지, pip install django 가 끝났는지 확인하세요."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
