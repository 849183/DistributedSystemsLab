from fastapi import APIRouter
from src.API import items # <--- different endpoins

api_router = APIRouter()

api_router.include_router(items.router,prefix="/items")


