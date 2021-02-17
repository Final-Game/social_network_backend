from dataclasses import dataclass


@dataclass
class AccountVerifyDto:
    front_photo_url: str = ""
    back_photo_url: str = ""
