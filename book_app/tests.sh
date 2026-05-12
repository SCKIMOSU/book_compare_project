#!/usr/bin/env bash
# tests.sh
# 세 방식이 모두 동일한 응답을 내는지 검증한다.
# 사용법: bash tests.sh  (Django 서버가 http://localhost:8000 에서 실행 중이어야 함)

set -e
BASE="http://localhost:8000"

echo "==================================================================="
echo "  Level 1 (APIView) · Level 2 (Generic) · Level 3 (ViewSet) 비교"
echo "==================================================================="

# ---------- 1. POST: 새 도서 등록 ----------
echo
echo "[1] POST 새 도서 등록 (Level 1 / 2 / 3 모두 201 Created 여야 함)"
echo
for V in v1 v2 v3; do
  echo "  ── $V ──"
  curl -s -o /dev/null -w "    status: %{http_code}\n"  \
       -X POST "$BASE/api/$V/books/"                    \
       -H "Content-Type: application/json"              \
       -d "{\"title\":\"DRF 실전 ($V)\",\"author\":\"이몽룡\",\"published_year\":2024,\"is_available\":true}"
done

# ---------- 2. GET 목록 ----------
echo
echo "[2] GET 목록 (응답 구조 비교)"
for V in v1 v2 v3; do
  echo
  echo "  ── $V ──"
  curl -s "$BASE/api/$V/books/" | python3 -m json.tool | head -n 20
done

# ---------- 3. PATCH 부분 수정 ----------
echo
echo "[3] PATCH /api/vX/books/1/  is_available 토글"
for V in v1 v2 v3; do
  echo "  ── $V ──"
  curl -s -X PATCH "$BASE/api/$V/books/1/"   \
       -H "Content-Type: application/json"   \
       -d '{"is_available": false}'          \
       | python3 -c "import sys, json; d=json.load(sys.stdin); print(f'    is_available = {d.get(\"is_available\")}')"
done

# ---------- 4. ModelViewSet 만의 커스텀 액션 ----------
echo
echo "[4] @action — ViewSet 전용 (Level 1 / 2 에는 존재하지 않는 엔드포인트)"
curl -s -X POST "$BASE/api/v3/books/1/toggle/" | python3 -m json.tool

echo
echo "==================================================================="
echo "  v1 / v2 / v3 모두 동일한 JSON 응답을 내야 정답"
echo "==================================================================="
