"""
Django settings for book_compare project.

풀스택서비스컴퓨팅 강의 실습용 — APIView · GenericAPIView · ModelViewSet 비교
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------
# 개발용 설정 (실제 배포 시에는 반드시 변경)
# --------------------------------------------------------------------
SECRET_KEY = 'django-insecure-CHANGE-ME-IN-PRODUCTION'
DEBUG = True
ALLOWED_HOSTS = ['*']

# --------------------------------------------------------------------
# 앱 등록
# --------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'rest_framework',

    # 실습 앱
    'book_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'book_compare.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'book_compare.wsgi.application'

# --------------------------------------------------------------------
# DB — SQLite (학습용)
# --------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --------------------------------------------------------------------
# 비밀번호 검증
# --------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------------------------------------------------
# 국제화
# --------------------------------------------------------------------
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = True

# --------------------------------------------------------------------
# 정적 파일
# --------------------------------------------------------------------
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --------------------------------------------------------------------
# DRF 설정 (학습용 — 인증 없이 접근 가능)
# --------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    # 페이징은 의도적으로 끔 — v1/v2/v3 응답을 동일하게 보여주기 위함
    # (활성화하면 GenericAPIView 가 자동으로 페이징하는 것을 v1 과 비교 가능)
    # 'DEFAULT_PAGINATION_CLASS':
    #     'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10,
}
