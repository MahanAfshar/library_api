from fastapi import APIRouter, status

from library_api.schemas.library_schema import BookCreate, BookUpdate
from library_api.services.library_service import (
    get_books,
    get_book,
    create_book,
    update_book,
    delete_book,
)

router = APIRouter()


@router.get("/books", status_code=status.HTTP_200_OK)
def get_all_books():
    return get_books()


@router.get("/books/{book_id}", status_code=status.HTTP_200_OK)
def get_single_book(book_id: int):
    return get_book(book_id)


@router.post("/books", status_code=status.HTTP_201_CREATED)
def post_book(book: BookCreate):
    return create_book(book)


@router.patch("/books/{book_id}", status_code=status.HTTP_200_OK)
def patch_book(book_id: int, book: BookUpdate):
    return update_book(book_id, book)


@router.delete("/books/{book_id}", status_code=status.HTTP_200_OK)
def remove_book(book_id: int):
    return delete_book(book_id)