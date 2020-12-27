from core.common.base_enum import BaseEnum


class GenderTypeEnum(BaseEnum):
    MALE: int = 0
    FEMALE: int = 1
    UN_KNOWN: int = 2

    def __int__(self) -> int:
        return int(self.value)

    def __str__(self) -> str:
        if self.value == self.MALE:
            return "MALE"
        elif self.value == self.FEMALE:
            return "FEMALE"
        elif self.value == self.UN_KNOWN:
            return "UN_KNOWN"

    @classmethod
    def to_choices(cls):
        return (
            (int(cls.MALE), str(cls.MALE)),
            (int(cls.FEMALE), str(cls.FEMALE)),
            (int(cls.UN_KNOWN), str(cls.UN_KNOWN)),
        )
