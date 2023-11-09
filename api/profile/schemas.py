from pydantic import BaseModel, ConfigDict


class ProfileBase(BaseModel):
    """Pydentic profile basic scheme"""

    first_name: str
    last_name: str
    user_id: int

    class Config:
        orm_mode = True


class ProfileCreate(ProfileBase):
    """Object profile to create"""

    pass


class Profile(ProfileBase):
    """Object profile to return"""

    model_config = ConfigDict(from_attributes=True)


class UsersBookCreate(BaseModel):
    """Object for creating user-added books"""

    profile_id: int
    book_id: int

    class Config:
        orm_mode = True
