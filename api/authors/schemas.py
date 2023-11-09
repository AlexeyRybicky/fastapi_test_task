from pydantic import BaseModel, ConfigDict


class AuthorBase(BaseModel):
    """Pydentic author basic scheme"""

    name: str
    # birth: TIMESTAMP
    # death: TIMESTAMP
    description: str
    biography: str

    class Config:
        orm_mode = True


class AuthorCreate(AuthorBase):
    """Object author to crate"""

    pass


class Author(AuthorBase):
    """Object author to return"""

    model_config = ConfigDict(from_attributes=True)

    id: int
