import random

import pytest


def build_user():
    username = f"user_{random.randint(10000, 99999)}"
    return {
        "id": random.randint(10000, 99999),
        "username": username,
        "firstName": "Leo",
        "lastName": "Test",
        "email": f"{username}@test.com",
        "password": "12345",
        "phone": "11999999999",
        "userStatus": 1,
    }


@pytest.fixture
def new_user(api):
    user = build_user()
    response = api.post("/user", json=user)
    assert response.status_code == 200
    yield user
    api.delete(f"/user/{user['username']}")


def test_create_user(api):
    user = build_user()
    response = api.post("/user", json=user)
    assert response.status_code == 200
    api.delete(f"/user/{user['username']}")


def test_get_user(api, new_user):
    response = api.get(f"/user/{new_user['username']}")
    assert response.status_code == 200
    assert response.json()["username"] == new_user["username"]


def test_update_user(api, new_user):
    new_user["firstName"] = "Updated"
    response = api.put(f"/user/{new_user['username']}", json=new_user)
    assert response.status_code == 200


def test_login(api):
    response = api.get(
        "/user/login", params={"username": "any", "password": "any"}
    )
    assert response.status_code == 200


def test_logout(api):
    response = api.get("/user/logout")
    assert response.status_code == 200


def test_delete_user(api):
    user = build_user()
    api.post("/user", json=user)
    response = api.delete(f"/user/{user['username']}")
    assert response.status_code == 200
