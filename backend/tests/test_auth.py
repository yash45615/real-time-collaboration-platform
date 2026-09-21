from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


TEST_USERNAME = "yash"
TEST_PASSWORD = "Password123!"


def test_login():
    response = client.post(
        "/auth/login",
        json={
            "username": TEST_USERNAME,
            "password": TEST_PASSWORD,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_with_wrong_password():
    response = client.post(
        "/auth/login",
        json={
            "username": TEST_USERNAME,
            "password": "WrongPassword123",
        },
    )

    assert response.status_code == 401

    data = response.json()

    assert data["detail"] == "Invalid username or password"


def test_protected_route_without_token():
    response = client.get("/users/me")

    assert response.status_code == 401

    data = response.json()

    assert data["detail"] == "Not authenticated"


def test_login_and_access_profile():
    login_response = client.post(
        "/auth/login",
        json={
            "username": TEST_USERNAME,
            "password": TEST_PASSWORD,
        },
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    response = client.get(
        "/users/me",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == TEST_USERNAME
    assert data["email"] == "yash@example.com"
    assert data["is_active"] is True
