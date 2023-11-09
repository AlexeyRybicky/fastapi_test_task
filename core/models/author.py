from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Author(Base):
    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    # birth: Mapped[TIMESTAMP] = mapped_column(
    #     TIMESTAMP,
    #     nullable=False,
    # )
    # death: Mapped[TIMESTAMP] = mapped_column(
    #     TIMESTAMP,
    # )
    description: Mapped[str] = mapped_column(
        String(length=500),
        nullable=False,
    )
    biography: Mapped[str] = mapped_column(
        String(length=1000),
        nullable=False,
    )
