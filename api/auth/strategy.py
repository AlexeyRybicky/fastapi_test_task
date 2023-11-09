from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend

from api.auth.manager import get_user_manager
from api.auth.transport import cookie_transport
from core.config import SECRET
from core.models.user import User

"""
Creating an instance of the AuthenticationBackend class
to configure the authentication backend for handling 
authentication in the API. 

    Args:
        name (str): the name of the authentication backend.
        transport (Transport): the transport mechanism used 
        for authentication
        get_strategy(Callable): (Callable): function that 
        returns the authentication strategy 
"""


def get_jwt_strategy() -> JWTStrategy:
    """
    Returns:
         an instance of the JWT Strategy class
         with the specified configuration parameters
    """
    return JWTStrategy(
        secret=SECRET,
        lifetime_seconds=3600,
    )


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_active_user = fastapi_users.current_user(active=True)
