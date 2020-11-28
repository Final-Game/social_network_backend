from datetime import date
import inspect
from user_content.domain.enums.marital_status_enum import MaritalStatusEnum
from core.common.base_api_exception import BaseApiException

from user_content.domain.enums.account_gender_enum import AccountGenderEnum


class UpdateAccountProfileDto(object):
    avatar_url: str
    cover_url: str
    email: str
    phone_number: str
    first_name: str
    last_name: str
    gender: str
    marital_status: str
    birth_date: date
    school: str
    address: str
    bio: str

    def __init__(self, *args, **kwargs) -> None:
        for prop in self.get_props():
            setattr(self, prop, kwargs[prop] or None)

        self.validate()

    @classmethod
    def get_props(cls):
        attributes = inspect.getmembers(cls, lambda a: not (inspect.isroutine(a)))

        # props
        return attributes[0][1].keys()

    def to_dict(self) -> dict:
        result_data: dict = {}
        for prop in self.get_props():
            result_data.update({prop: getattr(self, prop) or None})

        return result_data

    def validate(self):
        if self.gender and self.gender not in list(
            AccountGenderEnum.to_dict().values()
        ):
            raise BaseApiException("Invalid gender")

        if self.marital_status and self.marital_status not in list(
            MaritalStatusEnum.to_dict().values()
        ):
            raise BaseApiException("Invalid marital status")

    def map_to_profile_model_data(self) -> dict:
        data: dict = self.to_dict().copy()

        data.update({"avatar": data["avatar_url"], "cover": data["cover_url"]})
        data.pop("cover_url")
        data.pop("avatar_url")

        data.update({"gender": AccountGenderEnum.from_value(data.get("gender"))})
        data.update(
            {"marital_status": MaritalStatusEnum.from_value(data.get("marital_status"))}
        )

        return data
