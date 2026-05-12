"""
프로젝트 루트 URL 설정.

book_app/urls.py 가 /api/v1/, /api/v2/, /api/v3/ 세 가지 방식을 모두 라우팅한다.
"""
from django.contrib import admin
from django.urls    import path, include
from django.http    import HttpResponse


def home(request):
    """루트 페이지 — 사용 가능한 URL 안내"""
    return HttpResponse("""
        <html><head><meta charset="utf-8"><title>Book API 비교</title>
        <style>
          body {font-family: -apple-system, sans-serif; max-width: 700px;
                margin: 60px auto; padding: 0 20px; color: #333;}
          h1 {color: #0D9488;}
          h2 {margin-top: 32px;}
          a {color: #0D9488; text-decoration: none; font-family: monospace;}
          a:hover {text-decoration: underline;}
          .level {padding: 16px; border-left: 4px solid #0D9488;
                  background: #f8fafc; margin: 12px 0;}
          .level h2 {margin: 0; font-size: 18px;}
          .badge {display: inline-block; padding: 2px 8px; border-radius: 4px;
                  color: white; font-size: 12px; font-weight: bold;}
        </style></head><body>
        <h1>📚 Book API — APIView / GenericAPIView / ModelViewSet 비교</h1>
        <p>풀스택서비스컴퓨팅 강의 실습</p>

        <div class="level">
          <h2><span class="badge" style="background:#64748B">Level 1</span> APIView (직접 작성)</h2>
          <p><a href="/api/v1/books/">/api/v1/books/</a></p>
        </div>

        <div class="level">
          <h2><span class="badge" style="background:#0D9488">Level 2</span> GenericAPIView (조합)</h2>
          <p><a href="/api/v2/books/">/api/v2/books/</a></p>
        </div>

        <div class="level">
          <h2><span class="badge" style="background:#A30000">Level 3</span> ModelViewSet (자동)</h2>
          <p><a href="/api/v3/books/">/api/v3/books/</a> &nbsp;|&nbsp;
             <a href="/api/v3/">/api/v3/</a> (Router API root)</p>
        </div>

        <h2>관리자 페이지</h2>
        <p><a href="/admin/">/admin/</a> (superuser 생성 후 접근)</p>

        <p style="margin-top: 40px; color: #999; font-size: 12px;">
          © 김상철 · 국민대학교 소프트웨어학부</p>
        </body></html>
    """)


urlpatterns = [
    path('',         home,                      name='home'),
    path('admin/',   admin.site.urls),
    path('',         include('book_app.urls')),  # /api/v1/, v2/, v3/ 모두
]
