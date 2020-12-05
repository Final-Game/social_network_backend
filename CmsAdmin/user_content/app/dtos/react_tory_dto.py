from core.common.base_api_exception import BaseApiException
from user_content.domain.enums.react_type_enum import ReactTypeEnum


class ReactStoryDto(object):
    type: str

    def __init__(self, type: str = None) -> None:
        self.type = type

    def validate(self):
        if self.type and self.type not in ReactTypeEnum.values():
            raise BaseApiException("Invalid data")
