class LoginAccountResponseDto(object):
    account_id: str
    auth_token: str
    refresh_token: str

    def __init__(self, auth_token: str, refresh_token: str, account_id: str) -> None:
        self.auth_token = auth_token
        self.refresh_token = refresh_token
        self.account_id = account_id

    def to_dict(self):
        return {
            "auth_token": self.auth_token,
            "refresh_token": self.refresh_token,
            "account_id": self.account_id,
        }
