from core.common.base_api_exception import BaseApiException


class RegisterAccountDto:
    username: str
    password: str
    email: str

    def __init__(self, username: str, password: str, email: str = "") -> None:
        self.username = username
        self.password = password
        self.email = email

        self.validate()

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "password": self.password,
            "email": self.email,
        }

    def validate(self):
        if not self.username:
            raise BaseApiException("Username not found")

        if not self.password:
            raise BaseApiException("Password not found")