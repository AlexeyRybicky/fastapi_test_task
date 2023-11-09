from pydantic import BaseModel, ConfigDict


class BookBase(BaseModel):
    """Pydentic book basic scheme"""

    title: str
    # TODO: Помеять тип поля!!! TIMESTAMP не читается в pydentic
    # release: datetime
    description: str

    class Config:
        orm_mode = True


class BookCreate(BookBase):
    """Object book to crate"""

    author_ids: list[int]
    pass


class BookUpdate(BookCreate):
    """Object book to update"""

    pass


class BookUpdatePartial(BookCreate):
    """Object book to partial update"""

    author: list | None = None
    title: str | None = None
    description: str | None = None


class Book(BookBase):
    """Object book to return"""

    model_config = ConfigDict(from_attributes=True)

    id: int
