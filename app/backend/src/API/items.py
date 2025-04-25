from fastapi import APIRouter, HTTPException, status
from src.dum_db.mock_db import mock_items
from pydantic import BaseModel


router = APIRouter()

# ---------- SCHEMA ----------
class ItemUpdate(BaseModel):
    name: str
    quantity: int




# ---------- Endpoints ----------

# /items (Maria)
#     get
#     post
@router.get("/")
async def get_items():
    return mock_items

# @router.post("/")
# async def create_item(item: Item):
#     for existing_item in mock_items:
#         if existing_item.id == item.id:
#             raise HTTPException(status_code=400, detail="El ID ya existe")
#     mock_items.append(item)
#     return item
#para crear un nuevo item


# /items/{itemID} (Alain)
#     get
#     put
#     delete
@router.get("/{itemId}")
async def get_item_by_id(itemId: int):
    item = mock_items.get(itemId)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{itemId}")
async def update_item(itemId: int, updated_item: ItemUpdate):
    existing_item = mock_items.get(itemId)
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")
    mock_items[itemId].update(updated_item.dict())
    return mock_items[itemId]



@router.delete("/{itemId}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(itemId: int):
    if itemId not in mock_items:
        raise HTTPException(status_code=404, detail="Item not found")
    del mock_items[itemId]
    return

# GET /items/{itemId}
# @router.get("/items/{itemId}")
# async def get_item_by_id(itemId: int, request: Request):
#     query = "SELECT id, name, quantity FROM items WHERE id = $1"
#     item = await request.app.state.db.fetchrow(query, itemId)
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return dict(item)

# PUT /items/{itemId}
# @router.put("/items/{itemId}")
# async def update_item(itemId: int, updated_item: ItemUpdate, request: Request):
#     check_query = "SELECT id FROM items WHERE id = $1"
#     exists = await request.app.state.db.fetchval(check_query, itemId)
#     if not exists:
#         raise HTTPException(status_code=404, detail="Item not found")

#     update_query = (
#         "UPDATE items SET name = $1, quantity = $2 WHERE id = $3 RETURNING id, name, quantity"
#     )
#     item = await request.app.state.db.fetchrow(update_query, updated_item.name, updated_item.quantity, itemId)
#     return dict(item)

# DELETE /items/{itemId}
# @router.delete("/items/{itemId}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_item(itemId: int, request: Request):
#     delete_query = "DELETE FROM items WHERE id = $1"
#     result = await request.app.state.db.execute(delete_query, itemId)
#     if result == "DELETE 0":
#         raise HTTPException(status_code=404, detail="Item not found")
#     return

        
    





