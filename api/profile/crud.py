from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.profile.schemas import ProfileCreate, UsersBookCreate
from core.logger import func_logging
from core.models import Profile, UsersBook


@func_logging
async def create_profile(
    session: AsyncSession,
    profile_in: ProfileCreate,
) -> Profile:
    """
    Creates a new user profile in the database.
    Args:
        session: database connection session
        profile_in: pedantic scheme for creating profile in a database

    Returns:
        Profile: an instance of the created user profile
    """
    profile = Profile(**profile_in.model_dump())
    session.add(profile)
    await session.commit()
    return profile


@func_logging
async def add_book_in_profile(
    session: AsyncSession,
    book_in: UsersBookCreate,
) -> UsersBook:
    """
    Adds the selected book to the user profile
    Args:
        session: database connection session
        book_in: pedantic scheme for creating user-added books

    Returns:
        UsersBook:
    """
    user_book = UsersBook(**book_in.model_dump())
    session.add(user_book)
    await session.commit()
    return user_book


@func_logging
async def view_added_books(
    session: AsyncSession,
) -> list[UsersBook]:
    """
    Returns a list of all user-added books,
    sorted by ascending id
    Args:
        session: database connection session

    Returns:
        list of "users_book" objects in a database

    """
    stmt = select(UsersBook).order_by(UsersBook.book_id)
    result: Result = await session.execute(stmt)
    users_book = result.scalars().all()
    return list(users_book)
