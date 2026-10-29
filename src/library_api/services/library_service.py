from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from library_api.models.library_model import Book
from library_api.schemas.library_schema import BookCreate, BookUpdate


def get_books(db: Session):
    return db.scalars(select(Book)).all()


def get_book(book_id: int, db: Session):
    book = db.get(Book, book_id)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )

    return book


def create_book(book_data: BookCreate, db: Session):
    new_book = Book(**book_data.model_dump())

    db.add(new_book)

    try:
        db.commit()
        db.refresh(new_book)
    except Exception:
        db.rollback()
        raise

    return new_book


def update_book(book_id: int, book_data: BookUpdate, db: Session):
    book = db.get(Book, book_id)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )

    updates = book_data.model_dump(exclude_unset=True)

    if any(value is None for value in updates.values()):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Book fields cannot be null",
        )

    for field, value in updates.items():
        setattr(book, field, value)

    try:
        db.commit()
        db.refresh(book)
    except Exception:
        db.rollback()
        raise

    return book


def delete_book(book_id: int, db: Session):
    book = db.get(Book, book_id)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )

    try:
        db.delete(book)
        db.commit()
    except Exception:
        db.rollback()
        raise

    return {
        "message": "Book deleted successfully",
        "book": {
            "id": book.id,
            "title": book.title,
            "author": book.author,
        },
    }