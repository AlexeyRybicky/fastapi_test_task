from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import BookAuthor
from core.models.book import Book
from core.logger import func_logging

from .schemas import BookCreate, BookUpdate, BookUpdatePartial


@func_logging
async def get_books(session: AsyncSession) -> list[Book]:
    """
    Returns a list of all books sorted by ascending id
    Args:
        session: database connection session

    Returns:
        list of "Book" objects in a database

    Note:
        - Before using this function, make sure that you have a
        valid database connection and the necessary tables and objects.

    """
    stmt = select(Book).order_by(Book.id)
    result: Result = await session.execute(stmt)
    books = result.scalars().all()
    return list(books)


@func_logging
async def get_book(
    session: AsyncSession,
    book_id: int,
) -> Book | None:
    """
    Returns an instance of a book from the database using the book ID.
        Args:
        session: database connection session
        book_id:the ID of the book in the database

        Returns:
            Book | None: an instance of the book, by the specified ID,
            or None if the book is not found
    """
    return await session.get(Book, book_id)


@func_logging
async def create_book(
    session: AsyncSession,
    book_in: BookCreate,
) -> Book:
    """
    Creates a new book in the database.
    Args:
        session: database connection session
        book_in: pedantic scheme for creating a book in a database

    Returns:
        Book: an instance of the created book

    Note:
        Нужно ли описывать то что происходит в функции
    """
    book_dict = book_in.model_dump()
    author_ids = book_dict["author_ids"]
    del book_dict["author_ids"]
    book = Book(**book_dict)
    session.add(book)
    await session.commit()

    session.add_all(
        [
            BookAuthor(
                author_id=author_id,
                book_id=book.id,
            )
            for author_id in author_ids
        ]
    )
    await session.commit()
    return book


@func_logging
async def update_book(
    session: AsyncSession,
    book: Book,
    book_update: BookUpdate | BookUpdatePartial,
    partial: bool = False,
) -> Book:
    """
    Updates the book data in the database.
    Args:
        session: database connection session
        book: an instance that needs to be updated
        book_update: pedantic scheme for updated a book in a database
        partial: a flag is the update partial

    Returns:
        Book: an instance updated book

    """
    for name, value in book_update.model_dump(exclude_unset=partial).items():
        setattr(book, name, value)
    await session.commit()
    return book


@func_logging
async def delete_book(
    session: AsyncSession,
    book: Book,
) -> None:
    """
    Deletes the book from the database.
    Args:
        session: database connection session
        book: an instance to delete

    """
    await session.delete(book)
    await session.commit()
