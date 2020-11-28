from core.common import BaseApiException


class ChangeAccountPasswordDto(object):
    old_password: str
    new_password: str

    def __init__(self, old_password: str, new_password: str) -> None:
        self.old_password = old_password
        self.new_password = new_password

        self.validate()

    def validate(self):

        if not (self.old_password or self.new_password):
            raise BaseApiException("Password not found")

        if len(self.new_password) < 6:
            raise BaseApiException("Password must be large 6 characters.")
