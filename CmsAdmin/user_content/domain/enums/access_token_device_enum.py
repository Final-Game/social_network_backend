from core.common.base_enum import BaseEnum


class AccessTokenDeviceEnum(BaseEnum):
    IOS: str = "IOS"
    ANDROID: str = "ANDROID"
    WEB: str = "WEB"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def to_choices(cls):
        return (
            (str(cls.IOS), "Ios"),
            (str(cls.WEB), "Web"),
            (str(cls.ANDROID), "Android"),
        )
