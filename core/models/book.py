from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from .base import Base


class Book(Base):
    """Создание модели книги"""

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
    # release: Mapped[TIMESTAMP] = mapped_column(
    #     TIMESTAMP,
    # )
    description: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )
