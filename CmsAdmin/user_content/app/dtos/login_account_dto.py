from core.common.base_api_exception import BaseApiException


class LoginAccountDto:
    username: str
    password: str

    def __init__(self, username: str, password: str) -> None:
        self.password = password
        self.username = username

    def to_dict(self) -> dict:
        return {"username": self.username, "password": self.password}

    def validate(self):
        if not self.username:
            raise BaseApiException("Username not found")

        if not self.password:
            raise BaseApiException("Password not found")
