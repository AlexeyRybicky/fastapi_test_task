from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.auth.strategy import current_active_user
from core.models.utils import db_helper
from . import crud
from .schemas import Profile, ProfileCreate, UsersBookCreate

router = APIRouter(tags=["Profile"])


@router.post(
    "/create",
    response_model=Profile,
    status_code=status.HTTP_201_CREATED,
)
async def create_profile_user(
    profile_in: ProfileCreate,
    session: AsyncSession = Depends(
        db_helper.scoped_session_dependency,
    ),
    user=Depends(current_active_user),
):
    """
    The endpoint for adding a book to a user profile

    Args:
        session: database connection session
        profile_in: pedantic scheme for creating user-added books
        dependencies:
            provides a limited session to access the database
            for an authorized user
    """
    return await crud.create_profile(
        session=session,
        profile_in=profile_in,
    )


@router.post(
    "/add",
    response_model=UsersBookCreate,
    status_code=status.HTTP_202_ACCEPTED,
)
async def added_books(
    book_in: UsersBookCreate,
    session: AsyncSession = Depends(
        db_helper.scoped_session_dependency,
    ),
    user=Depends(current_active_user),
):
    """
    The endpoint to create a new user profile

    Args:
        session: database connection session
        book_in: pedantic scheme for creating profile in a database
        dependencies:
            provides a limited session to access the database
            for an authorized user
    """
    return await crud.add_book_in_profile(
        session=session,
        book_in=book_in,
    )


@router.get(
    "/",
    # response_model=list[UsersBook],
)
async def get_profile_books(
    session: AsyncSession = Depends(
        db_helper.scoped_session_dependency,
    ),
    user=Depends(current_active_user),
):
    """
    The endpoint for viewing all books added by the user

    Args:
        session: database connection session
        dependencies:
            provides a limited session to access the database
            for an authorized user
    """
    return await crud.view_added_books(session=session)
