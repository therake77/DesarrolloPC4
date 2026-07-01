from contextlib import asynccontextmanager
from alerts.domain.alert_event_dispatcher import AlertNewMissingPetSubject
from alerts.infraestructure.adapters.new_missing_pet_handler import SQLNewMissinPetHandler
from users.infrastructure.http.http_controller import router as r1
from alerts.infraestructure.http.http_controller import router as r2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from shared.infrastructure.persistence.base.base import engine
from sqlalchemy.ext.asyncio import async_sessionmaker

@asynccontextmanager
async def lifespan( app : FastAPI ):
    session_factory = async_sessionmaker(engine,expire_on_commit=False)
    subject = AlertNewMissingPetSubject()

    await subject.attach(
        SQLNewMissinPetHandler(
            session_factory
        )
    )
    
    app.state.alert_event_dispatcher = subject

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
app.include_router(prefix="/api",router=r2)
