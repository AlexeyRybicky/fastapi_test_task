from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    """
    Base class for database models
    this table should not be in the database
    """

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """Automatic generation of the table name"""
        return f"{cls.__name__.lower()}s"

    __abstract__ = True
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
