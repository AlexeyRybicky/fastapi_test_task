from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


from .base import Base


class BookAuthor(Base):
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    # book: Mapped["Book"] = relationship(
    #     back_populates="authors",
    # )
