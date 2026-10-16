from fastapi import FastAPI
from library_api.routers.library_router import router as books_router

app = FastAPI()

app.include_router(books_router)