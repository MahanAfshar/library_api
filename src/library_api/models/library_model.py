from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from library_api.database.library_database import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    author: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    year: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )