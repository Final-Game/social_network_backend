from core.common.base_api_exception import BaseApiException

class UcDomainException(BaseApiException):
    def __init__(self, msg: str) -> None:
        super(UcDomainException, self).__init__(msg, error_code="cm_domain_exception")