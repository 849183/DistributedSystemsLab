from fastapi import APIRouter
from src.dum_db.mock_db import mock_items

router = APIRouter()

# /items (Maria)
#     get
#     post
@router.get("/")
async def get_items():
    return mock_items

# @router.post("/")
# async def create_item(item: Item):
#   for existing_item in mock_items:
#       if existing_item.id == item.id:
#           raise HTTPException(status_code=400, detail="El ID ya existe")
#   mock_items.append(item)
#   return item

#para crear un nuevo item


# /items/{itemID} (Alain)
#     get
#     put
#     delete


        
    





