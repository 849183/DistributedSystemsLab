from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_dict_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_dict_one_item_200():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert isinstance(response.json(),dict)

def test_dict_one_item_404():
    response = client.get("/items/49")
    assert response.status_code == 404

def test_update_existing_item():
    update_data = {"name": "Monitor UltraWide", "quantity": 7}
    response = client.put("/items/3", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Monitor UltraWide"
    assert data["quantity"] == 7

def test_update_nonexistent_item():
    update_data = {"name": "Fake", "quantity": 1}
    response = client.put("/items/999", json=update_data)
    assert response.status_code == 404

def test_delete_existing_item():
    response = client.delete("/items/2")
    assert response.status_code == 204

def test_delete_nonexistent_item():
    response = client.delete("/items/999")
    assert response.status_code == 404

# test maria

def test_get_items_empty():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_item_success():
    item_data = {"name": "Monitor UltraWide", "quantity": 7}
    response = client.post("/", json=item_data)
    assert response.status_code == 200
    assert response.json() == item_data

def test_get_items_after_create():
    response = client.get("/")
    assert response.status_code == 200
    expected_items = [{"id": 1, "name": "Test Item", "description": "This is a test item"}]
    assert response.json() == expected_items