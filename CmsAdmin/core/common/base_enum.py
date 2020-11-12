from enum import Enum


class BaseEnum(Enum):
    def __eq__(self, value):
        if isinstance(self.value, value.__class__):
            return self.value == value

        return super().__eq__(value)
