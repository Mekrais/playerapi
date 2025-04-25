from fastapi import FastAPI
from .routers import events, players
from contextlib import asynccontextmanager
from .database import create_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating database...")
    create_db()
    yield
    print("Closing database...")


app = FastAPI(lifespan=lifespan)

app.include_router(events.router)
app.include_router(players.router)
