from fastapi_users.authentication import CookieTransport

"""
Creating an instance of the CookieTransport class 
to configure cookie transport for processing 
cookies in API requests and responses.

    Args:
        cookie_name(str): the name of the cookie used for transport
        cookie_max_age()int: the maximum time (in seconds) of 
        a cookie after which it will expire.
"""

cookie_transport = CookieTransport(
    cookie_name="library",
    cookie_max_age=3600,
)
