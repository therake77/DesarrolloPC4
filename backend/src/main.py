from contextlib import asynccontextmanager
from users.infrastructure.http.http_controller import router as r1
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from shared.infrastructure.persistence.base.base import engine

@asynccontextmanager
async def lifespan( app : FastAPI ):
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(prefix="/api",router=r1)

