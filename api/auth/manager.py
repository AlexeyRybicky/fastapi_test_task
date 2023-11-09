from typing import Optional
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin


from core.config import SECRET
from core.models.user import User
from core.models.utils import db_helper


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    """
    User manager who is responsible for managing users in the system.

    Attribute:
        reset_password_token_secret: token for resetting user passwords
        verification_token_secret: token for user verification

    Methods:
        on_after_register: called after a successful user registration
    """

    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(
        self,
        user: User,
        request: Optional[Request] = None,
    ):
        """
        Args:
            user: object that was registered
            request: that was sent during registration

        Returns:
              message that a user with id has been registered
        """
        print(f"User {user.id} has registered.")


async def get_user_manager(user_db=Depends(db_helper.get_user_db)):
    """
    Args:
        user_db: user database object
    Yields:
        object UserManager
    """
    yield UserManager(user_db)
