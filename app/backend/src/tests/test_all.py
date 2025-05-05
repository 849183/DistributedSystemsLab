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

def test_create_item():
    create_item = {"name": "Monitor HD", "quantity": 7}
    initial_response = client.get("/items/")
    initial_items = initial_response.json()
    initial_count = len(initial_items)

    create_response = client.post("/items/", json=create_item)
    assert create_response.status_code == 201, f"Expected status code 201, got {create_response.status_code}"
    created_item = create_response.json()

    assert "id" in created_item, "Created item response does not contain an 'id' field"
    assert created_item["name"] == create_item["name"], f"Expected name '{create_item['name']}', got '{created_item['name']}'"
    assert created_item["quantity"] == create_item["quantity"], f"Expected quantity {create_item['quantity']}, got {created_item['quantity']}"

    new_item_id = created_item["id"]

    updated_response = client.get("/items/")
    updated_items = updated_response.json()
    assert len(updated_items) == initial_count + 1, f"Expected {initial_count + 1} items, got {len(updated_items)}"
    
    item_response = client.get(f"/items/{new_item_id}")
    assert item_response.status_code == 200, f"Expected status code 200, got {item_response.status_code}"
    
    retrieved_item = item_response.json()
    assert retrieved_item["name"] == create_item["name"], f"Retrieved item has name '{retrieved_item['name']}', expected '{create_item['name']}'"
    assert retrieved_item["quantity"] == create_item["quantity"], f"Retrieved item has quantity {retrieved_item['quantity']}, expected {create_item['quantity']}"
    
    assert str(new_item_id) in updated_items or new_item_id in updated_items, f"Item with ID {new_item_id} not found in the complete items list"



