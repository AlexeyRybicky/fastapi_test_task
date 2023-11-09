from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession


from core.models import Book
from core.models.utils import db_helper
from . import crud


async def book_by_id(
    book_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Book:
    """
    Returns an instance of a book from the database using the book ID.
        Args:
             book_id: id of the book from the database,
             retrieved from the request path
             session: database connection session, uses dependency
        Returns:
            an instance of the book by ID
        Raise:
            HTTPException 404 with the message book not found
    """
    book = await crud.get_book(session=session, book_id=book_id)
    if book is not None:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Книга {book_id} не найдена!",
    )
