
class BaseApiException(Exception):
    def __init__(self, msg: str, error_code: str = "base_api_exception"):
        self.error_code = error_code
        self.msg = msg
        super(BaseApiException, self).__init__(msg)