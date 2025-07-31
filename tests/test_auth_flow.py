import requests
import allure
from utils.allure_helpers import attach_response, step_request, step_check_status, step_validate_body

BASE_URL = "http://localhost:8000"

@allure.feature("Auth")
@allure.title("Successful login returns token")
def test_login_success():
    payload = {"username": "user1", "password": "hashed_password"}

    with step_request("POST /auth/login"):
        response = requests.post(f"{BASE_URL}/auth/login", json=payload)
        attach_response(response)

    with step_check_status():
        assert response.status_code == 200

    with step_validate_body():
        data = response.json()
        assert "access_token" in data

    return data["access_token"]


@allure.feature("Users")
@allure.title("Authorized user receives list of users from DB")
def test_get_users():
    with allure.step("Login and get access token"):
        token = test_login_success()

    headers = {"Authorization": f"Bearer {token}"}

    with step_request("GET /users/"):
        response = requests.get(f"{BASE_URL}/users/", headers=headers)
        attach_response(response)

    with step_check_status():
        assert response.status_code == 200

    with step_validate_body():
        users = response.json()
        assert isinstance(users, list)
        assert len(users) >= 10
        for user in users:
            assert isinstance(user["username"], str)
            assert isinstance(user["email"], str)
            assert "@" in user["email"]

@allure.feature("Posts")
@allure.title("Authorized user can create a post")
def test_create_post():
    with allure.step("Login and get access token"):
        token = test_login_success()

    headers = {"Authorization": f"Bearer {token}"}

    # 🔍 Проверка, что пользователь есть в БД
    with step_request("GET /users/ — убедиться, что user1 есть в списке"):
        r = requests.get(f"{BASE_URL}/users/", headers=headers)
        attach_response(r)
        assert r.status_code == 200
        users = r.json()
        usernames = [u["username"] for u in users]
        assert "user1" in usernames, "user1 не найден в базе пользователей"

    # 📬 Создание поста
    post_data = {"title": "Test Post", "content": "Some content"}
    with step_request("POST /posts-db/ — создание поста"):
        response = requests.post(f"{BASE_URL}/posts-db/", headers=headers, json=post_data)
        attach_response(response)

    with step_check_status():
        assert response.status_code == 200

    with step_validate_body():
        result = response.json()
        assert result["title"] == post_data["title"]
        assert result["content"] == post_data["content"]
        assert "user_id" in result
