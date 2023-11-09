from asyncio import current_task
from typing import Generator
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)

from core.config import settings
from core.models.user import User


"""
Creating an instance of the DatabaseHelper class 
by calling the class constructor.

    Args:
    url (string): database URL
    echo (boolean value): flag indicating whether 
    to output debugging information when executing queries.

An instance of the DatabaseHelper class is stored in the db_helper 
variable and can be used to access methods and properties of the class.
"""


class DatabaseHelper:
    """
    Used to work with the database.
    This is a DatabaseService

    Attribute:
        engine(тип): represents the SQLAlchemy engine for working with a database.
        session_factory(тип): represents the SQLAlchemy session factory for working with the database.

    Methods:
        get_scoped_session(self) -> async_scoped_session:
        Creating a factory-based session.

        session_dependency(self) -> Generator[AsyncSession]:
        It is an asynchronous generator that creates a session and
        connects to the database during queries.


        scoped_session_dependency(self) -> Generator[AsyncSession]:
        It is an asynchronous generator that creates a session and
        connects to a database with a scope.


        get_user_db(self) -> Generator[AsyncSession]:
        It is an asynchronous generator that creates a session and
        retrieves an instance of a custom SQLAlchemy database class
        to work with a custom table in a database.


    """

    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self) -> async_scoped_session:
        """
        Creating a factory-based session.

        Returns:
            async_scoped_session: AsyncSession database object with scope
        """
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(
        self,
    ) -> Generator[AsyncSession, None, None]:
        """
        It is an asynchronous generator that creates a session and
        connects to the database during queries.

        Yields:
            AsyncSession database object
        """
        async with self.session_factory() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(
        self,
    ) -> Generator[AsyncSession, None, None]:
        """
        It is an asynchronous generator that creates a session and
        connects to a database with a scope.

        Yields:
            AsyncSession database object
        """
        session = self.get_scoped_session()
        yield session
        await session.close()

    async def get_user_db(
        self,
    ) -> Generator[SQLAlchemyUserDatabase, None, None]:
        """
        It is an asynchronous generator that creates a session and
        retrieves an instance of a custom SQLAlchemy database class
        to work with a custom table in a database.

        Yields:
            SQLAlchemyUserDatabase: Instance to work with a User table
        """
        session = self.get_scoped_session()
        yield SQLAlchemyUserDatabase(session, User)
        await session.close()


db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.db_echo,
)
