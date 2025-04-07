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

def test_dict_items():
    response = client.get("/items/")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)

    mock_items = {
    1: {"name": "Teclado", "quantity" : "2"},
    2: {"name": "Mouse", "quantity" : "3"},
    3: {"name": "Monitor", "quantity" : "4"}
    }
    assert len(data) == len(mock_items)

    for item_id, item_data in mock_items.items():
        str_id = str(item_id)
        assert str_id in data
        assert data[str_id]["name"] == item_data["name"]
        assert data[str_id]["quantity"] == item_data["quantity"]

def test_create_item():
   
    # Datos de prueba
    payload = {
        "name": "Teclat",
        "quantity": 3,
    }

    response = client.post("/items/", json=payload)
    
    assert response.status_code == 201
    data = response.json()
    
    assert "id" in data
    assert data["name"] == "Teclat"
    assert data["quantity"] == 3