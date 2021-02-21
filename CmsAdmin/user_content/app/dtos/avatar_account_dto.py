from dataclasses import dataclass


@dataclass
class AvatarAccountDto:
    media_url: str
    type: str