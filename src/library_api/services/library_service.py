from fastapi import HTTPException, status

from library_api.data.library_data import books
from library_api.schemas.library_schema import BookCreate, BookUpdate

next_book_id = max(books.keys(), default=0) + 1


def get_books():
    return list(books.values())


def get_book(book_id: int):
    book = books.get(book_id)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )

    return book


def create_book(book_data: BookCreate):
    global next_book_id

    new_book = {
        "id": next_book_id,
        **book_data.model_dump(),
    }

    books[next_book_id] = new_book
    next_book_id += 1

    return new_book


def update_book(book_id: int, book_data: BookUpdate):
    book = books.get(book_id)

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

    book.update(updates)

    return book


def delete_book(book_id: int):
    deleted_book = books.pop(book_id, None)

    if deleted_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )

    return {
        "message": "Book deleted successfully",
        "book": deleted_book,
    }