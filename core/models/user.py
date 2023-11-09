from datetime import datetime
from sqlalchemy import String, Boolean, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    """
    Model, user tables in the database.

    Attributes:
        user_name: User name
        email: User's email address
        hashed_password: Hashed user password
        date_registration: Date of user registration.
        is_active: A flag indicating whether the user is active.
        is_superuser: A flag indicating whether the user is a superuser.
        is_verified: Flag indicating whether the user is verified.

    """

    user_name: Mapped[str] = mapped_column(
        String(length=50),
        unique=True,
    )
    email: Mapped[str] = mapped_column(
        String(length=320),
        unique=True,
        index=True,
        nullable=False,
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024),
        nullable=False,
    )
    date_registration: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP,
        default=datetime.utcnow,
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )
