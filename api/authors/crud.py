from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.authors.schemas import AuthorCreate
from core.models.author import Author
from core.logger import func_logging


@func_logging
async def get_authors(session: AsyncSession) -> list[Author]:
    """
    Returns a list of all authors sorted by ascending id
    Args:
        session: database connection session

    Returns:
        list of "Author" objects in a database

    Note:
        - Before using this function, make sure that you have a
        valid database connection and the necessary tables and objects.
    """
    stmt = select(Author).order_by(Author.id)
    result: Result = await session.execute(stmt)
    authors = result.scalars().all()
    return list(authors)


@func_logging
async def get_author(
    session: AsyncSession,
    author_id: int,
) -> Author | None:
    """
    Returns an instance of author from the database using the author ID.
        Args:
        session: database connection session
        author_id:the ID of the author in the database

        Returns:
            Author | None: an instance of the author, by the specified ID,
            or None if the author is not found
    """
    return await session.get(Author, author_id)


@func_logging
async def create_author(
    session: AsyncSession,
    author_in: AuthorCreate,
) -> Author:
    """
    Creates a new author in the database.
    Args:
        session: database connection session
        author_in: pedantic scheme for creating author in a database

    Returns:
        Author: an instance of the created author
    """
    author = Author(**author_in.model_dump())
    session.add(author)
    await session.commit()
    return author
