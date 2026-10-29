from contextlib import asynccontextmanager

from fastapi import FastAPI

from library_api.database.library_database import Base, engine
from library_api.routers.library_router import router as books_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(books_router)