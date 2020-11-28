from jose import jwt
from django.conf import settings

from .authentication_failed_exception import AuthenticaticationFailedException


class BaseAuthentication(object):
    def __init__(self) -> None:
        return

    @classmethod
    def decode_token(cls, auth_token) -> dict:
        try:
            payload: dict = jwt.decode(
                auth_token,
                settings.JWT_PRIVATE_SIGNATURE,
                algorithms=["HS256"],
            )
        except Exception as ex:
            raise AuthenticaticationFailedException("Invalid Token")

        return payload

    @classmethod
    def check_permission(cls, auth_token: str, account_id: str = ""):
        raise NotImplementedError()
