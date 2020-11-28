from core.authenticates.authentication_failed_exception import (
    AuthenticaticationFailedException,
)
from core.authenticates import BaseAuthentication


class AccountAuthentication(BaseAuthentication):
    
    @classmethod
    def check_permission(cls, auth_token: str, account_id: str = ""):
        account_payload: dict = cls.decode_token(auth_token)

        if account_id and account_id != account_payload["sub"]:
            raise AuthenticaticationFailedException("Account not permission!")

        return True
