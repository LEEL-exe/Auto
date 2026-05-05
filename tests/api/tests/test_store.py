import random

import pytest


def build_order():
    return {
        "id": random.randint(1, 10),
        "petId": random.randint(1, 1000),
        "quantity": 1,
        "status": "placed",
        "complete": True,
    }


@pytest.fixture
def new_order(api):
    order = build_order()
    response = api.post("/store/order", json=order)
    assert response.status_code == 200
    yield order
    api.delete(f"/store/order/{order['id']}")


def test_create_order(api):
    order = build_order()
    response = api.post("/store/order", json=order)
    assert response.status_code == 200
    assert response.json()["status"] == "placed"
    api.delete(f"/store/order/{order['id']}")


def test_get_order(api, new_order):
    response = api.get(f"/store/order/{new_order['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == new_order["id"]


def test_delete_order(api):
    order = build_order()
    api.post("/store/order", json=order)
    response = api.delete(f"/store/order/{order['id']}")
    assert response.status_code == 200


def test_inventory(api):
    response = api.get("/store/inventory")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
