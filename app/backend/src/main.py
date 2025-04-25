from fastapi import FastAPI
from src.router import api_router
from pydantic import BaseModel
import asyncpg
import os


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:Welcome1.@db:5432/shopApp")

app = FastAPI()

app.include_router(api_router)



@app.on_event("startup")
async def startup_db():
    app.state.db = await asyncpg.connect(DATABASE_URL)

@app.on_event("shutdown")
async def shutdown_db():
    await app.state.db.close()
    


class Item(BaseModel):
    id: int
    name: str
    quantity: int

class ItemUpdate(BaseModel):
    name: str
    quantity: int
