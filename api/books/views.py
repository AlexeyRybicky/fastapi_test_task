from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.auth.strategy import current_active_user
from core.models.utils import db_helper
from .dependencies import book_by_id
from . import crud
from .schemas import Book, BookCreate, BookUpdate, BookUpdatePartial


router = APIRouter(tags=["Books"])


@router.get(
    "/",
    response_model=list[Book],
)
async def get_books(
    session: AsyncSession = Depends(
        db_helper.scoped_session_dependency,
    ),
):
    """
    The endpoint for getting a list of books.

    Args:
        session: database connection session
        dependencies: provides a limited session to access the database.

    Returns:
        a list of books obtained from the database.
    """
    return await crud.get_books(session=session)


@router.get(
    "/{book_id}",
    response_model=Book,
)
async def get_book(
    book: Book = Depends(book_by_id),
):
    """
    The endpoint returns the book by id

    Args:
        book: an instance of a book
        dependency: book_by_id

    Returns:
        the book instance.
    """
    return book


@router.post(
    "/",
    response_model=Book,
    status_code=status.HTTP_201_CREATED,
)
async def create_book(
    book_in: BookCreate,
    session: AsyncSession = Depends(
        db_helper.scoped_session_dependency,
    ),
    user=Depends(current_active_user),
):
    """
    The endpoint to create a new book

    Args:
        session: database connection session
        book_in: pedantic scheme for creating a book in a database
        dependencies: provides a limited session to access the database.
    """
    return await crud.create_book(
        session=session,
        book_in=book_in,
    )


@router.put("/{book_id}")
async def update_book(
    book_update: BookUpdate,
    book: Book = Depends(book_by_id),
    session: AsyncSession = Depends(
        db_helper.scoped_session_dependency,
    ),
    user=Depends(current_active_user),
):
    """
    The endpoint for updating the book

    Args:
        book_update: pedantic scheme for updating a book in a database
        book: pedantic scheme a book in a database
        session: database connection session
        dependencies:
            book_by_id: retrieves the book instance
            db_helper.scoped_session_dependency: provides a limited
            session to access the database

    Returns:
        the updated book with the specified `book_id`.
    """
    return await crud.update_book(
        session=session,
        book=book,
        book_update=book_update,
    )


# TODO: Здесь какая то ошибка, проверь почему не рабоает изминение одного свойства
@router.patch("/{book_id}")
async def update_book_partial(
    book_update: BookUpdatePartial,
    book: Book = Depends(book_by_id),
    session: AsyncSession = Depends(
        db_helper.scoped_session_dependency,
    ),
    user=Depends(current_active_user),
):
    """
    This endpoint for a partial book update

    Args:
        book_update: pedantic scheme for updating a book in a database
        book: pedantic scheme a book in a database
        session: database connection session
        dependencies:
            book_by_id: retrieves the book instance
            db_helper.scoped_session_dependency: provides a limited
            session to access the database

    Returns:
        the partially updated book

    """
    return await crud.update_book(
        session=session,
        book=book,
        book_update=book_update,
        partial=True,
    )


@router.delete(
    "/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_book(
    book: Book = Depends(book_by_id),
    session: AsyncSession = Depends(
        db_helper.scoped_session_dependency,
    ),
    user=Depends(current_active_user),
) -> None:
    """
    This endpoint of deleting a book

    Args:
        book: pedantic scheme a book in a database
        session: database connection session
        dependencies:
            book_by_id: retrieves the book instance
            db_helper.scoped_session_dependency: provides a limited
            session to access the database


    """
    await crud.delete_book(
        session=session,
        book=book,
    )
