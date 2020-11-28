class LoginAccountResponseDto(object):
    auth_token: str
    refresh_token: str

    def __init__(self, auth_token: str, refresh_token: str) -> None:
        self.auth_token = auth_token
        self.refresh_token = refresh_token

    def to_dict(self):
        return {"auth_token": self.auth_token, "refresh_token": self.refresh_token}
