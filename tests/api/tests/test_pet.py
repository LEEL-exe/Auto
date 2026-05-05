import random

import pytest


def build_pet(name="Rex", status="available"):
    return {
        "id": random.randint(100000, 999999),
        "name": name,
        "category": {"id": 1, "name": "dog"},
        "photoUrls": ["http://example.com/photo.jpg"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": status,
    }


@pytest.fixture
def new_pet(api):
    pet = build_pet()
    response = api.post("/pet", json=pet)
    assert response.status_code == 200
    yield pet
    api.delete(f"/pet/{pet['id']}")


def test_create_pet(api):
    pet = build_pet(name="Buddy")
    response = api.post("/pet", json=pet)
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Buddy"
    assert body["status"] == "available"
    api.delete(f"/pet/{pet['id']}")


def test_get_pet_by_id(api, new_pet):
    response = api.get(f"/pet/{new_pet['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == new_pet["id"]


def test_update_pet(api, new_pet):
    new_pet["name"] = "Rex Updated"
    new_pet["status"] = "sold"
    response = api.put("/pet", json=new_pet)
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Rex Updated"
    assert body["status"] == "sold"


def test_find_pet_by_status(api):
    response = api.get("/pet/findByStatus", params={"status": "available"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_delete_pet(api):
    pet = build_pet(name="ToDelete")
    api.post("/pet", json=pet)
    response = api.delete(f"/pet/{pet['id']}")
    assert response.status_code == 200
