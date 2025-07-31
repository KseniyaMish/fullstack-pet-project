import requests
import allure

from tests.test_auth_flow import test_login_success
from utils.allure_helpers import attach_response, step_request, step_check_status, step_validate_body

BASE_URL = "http://localhost:8000"

@allure.feature("Posts Cleanup")
@allure.title("Cleanup keeps only the latest post after exceeding limit")
def test_cleanup_after_20_posts():
    with allure.step("Login and get access token"):
        token = test_login_success()
    headers = {"Authorization": f"Bearer {token}"}

    with step_request("GET /posts-db/ — get current posts"):
        r = requests.get(f"{BASE_URL}/posts-db/", headers=headers, timeout=5)
        attach_response(r)
        existing = r.json()
        count = len(existing)

    with step_validate_body():
        assert count <= 21, f"Слишком много записей в базе: {count}. Очистка не работает."

    if count < 20:
        to_create = 20 - count
        for i in range(to_create):
            requests.post(f"{BASE_URL}/posts-db/", headers=headers,
                          json={"title": f"Filler {i}", "content": "..."}, timeout=5)

    with step_request("POST 21-й пост → триггер очистку"):
        r = requests.post(f"{BASE_URL}/posts-db/", headers=headers,
                          json={"title": "Survivor", "content": "Will remain"}, timeout=5)
        attach_response(r)
        assert r.status_code == 200

    with step_request("GET /posts-db/ — validate cleanup"):
        r = requests.get(f"{BASE_URL}/posts-db/", headers=headers, timeout=5)
        attach_response(r)
        posts = r.json()

    with step_validate_body():
        assert len(posts) == 1, "После очистки должен остаться только один пост"
        assert posts[0]["title"] == "Survivor"