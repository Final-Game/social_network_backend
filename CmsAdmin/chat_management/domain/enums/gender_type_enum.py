from core.common.base_enum import BaseEnum


class GenderTypeEnum(BaseEnum):
    MALE: int = 0
    FEMALE: int = 1
    UN_KNOWN: int = 2

    def __int__(self) -> int:
        return int(self.value)

    def __str__(self) -> str:
        return self.name

    @classmethod
    def to_choices(cls):
        return (
            (int(cls.MALE), str(cls.MALE)),
            (int(cls.FEMALE), str(cls.FEMALE)),
            (int(cls.UN_KNOWN), str(cls.UN_KNOWN)),
        )
