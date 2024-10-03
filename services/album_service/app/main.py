from fastapi import FastAPI
from app.routers import albums

app = FastAPI(title="Album Service")

app.include_router(albums.router, prefix="/albums", tags=["albums"])

