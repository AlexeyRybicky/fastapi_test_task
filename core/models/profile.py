from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String

from .base import Base


class Profile(Base):
    first_name: Mapped[str] = mapped_column(String(32))
    last_name: Mapped[str] = mapped_column(String(32))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
