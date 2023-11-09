from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.auth.strategy import current_active_user
from core.models.utils import db_helper
from .dependencies import author_by_id
from . import crud
from .schemas import AuthorCreate, Author

router = APIRouter(tags=["Authors"])


@router.get(
    "/",
    response_model=list[Author],
)
async def get_authors(
    session: AsyncSession = Depends(
        db_helper.scoped_session_dependency,
    ),
):
    """
    The endpoint for getting a list of authors.

    Args:
        session: database connection session
        dependencies: provides a limited session to access the database.

    Returns:
        a list of authors obtained from the database.
    """
    return await crud.get_authors(session=session)


@router.post(
    "/",
    response_model=Author,
    status_code=status.HTTP_201_CREATED,
)
async def create_author(
    author_in: AuthorCreate,
    session: AsyncSession = Depends(
        db_helper.scoped_session_dependency,
    ),
    user=Depends(current_active_user),
):
    """
    The endpoint to create a new author

    Args:
        session: database connection session
        author_in: pedantic scheme for creating author in a database
        dependencies:
            provides a limited session to access the database
            for an authorized user
    """
    return await crud.create_author(
        session=session,
        author_in=author_in,
    )


@router.get(
    "/{author_id}",
    response_model=Author,
)
async def get_author(
    author: Author = Depends(author_by_id),
):
    """
    The endpoint returns the author by id

    Args:
        author: an instance of author
        dependency: author_by_id

    Returns:
        the author instance.
    """
    return author
