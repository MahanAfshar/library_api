from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status

from library_api.database.library_database import get_db
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
def get_all_books(db: Session = Depends(get_db)):
    return get_books(db)


@router.get("/books/{book_id}", status_code=status.HTTP_200_OK)
def get_single_book(book_id: int, db: Session = Depends(get_db)):
    return get_book(book_id, db)


@router.post("/books", status_code=status.HTTP_201_CREATED)
def post_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(book, db)


@router.patch("/books/{book_id}", status_code=status.HTTP_200_OK)
def patch_book(
    book_id: int,
    book: BookUpdate,
    db: Session = Depends(get_db),
):
    return update_book(book_id, book, db)


@router.delete("/books/{book_id}", status_code=status.HTTP_200_OK)
def remove_book(book_id: int, db: Session = Depends(get_db)):
    return delete_book(book_id, db)