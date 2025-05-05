from fastapi import FastAPI, HTTPException, status, Request
from src.router import api_router
from pydantic import BaseModel
import asyncpg
import os


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:Welcome1.@db:5432/shopApp")

app = FastAPI()

app.include_router(api_router)

for route in app.routes:
    print(f"{route.path} -> {route.endpoint}")


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
