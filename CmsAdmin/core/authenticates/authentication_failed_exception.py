from core.common.base_api_exception import BaseApiException


class AuthenticaticationFailedException(BaseApiException):
    def __init__(self, msg: str) -> None:
        super(AuthenticaticationFailedException, self).__init__(
            msg, error_code="authentication_failed"
        )