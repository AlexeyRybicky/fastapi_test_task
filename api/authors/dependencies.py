from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Author
from core.models.utils import db_helper
from . import crud


async def author_by_id(
    author_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Author:
    """
    Returns an instance of author from the database using the book ID.
        Args:
             author_id: id of the author from the database,
             retrieved from the request path
             session: database connection session, uses dependency
        Returns:
            an instance of the author by ID
        Raise:
            HTTPException 404 with the message author not found
    """
    author = await crud.get_author(
        session=session,
        author_id=author_id,
    )
    if author is not None:
        return author
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Автор {author_id} не найден!"
    )
