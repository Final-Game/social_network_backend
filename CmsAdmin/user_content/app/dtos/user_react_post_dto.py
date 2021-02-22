from core.common.base_api_exception import BaseApiException


class UserReactPostDto(object):
    type: str

    def __init__(self, type: str) -> None:
        self.type = type

        self.validate()

    def validate(self):
        if self.type not in ["LIKE", "LOVE", "HAHA"]:
            raise BaseApiException("Invalid react type")