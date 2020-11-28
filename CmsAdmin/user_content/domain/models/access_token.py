import time
import json
from user_content.domain.enums.access_token_status_enum import AccessTokenStatusEnum
from jose import jwt
from user_content.domain.enums.access_token_device_enum import AccessTokenDeviceEnum

from django.db import models
from django.conf import settings

from core.domain.models.base_model import BaseModel

# Menu Model
def token_expiry():
    return int(time.time()) + settings.TOKEN_EXPIRATION_DURATION


def current_time():
    return int(time.time())


class AccessToken(BaseModel):
    scopes = models.CharField(max_length=250, blank=True, null=True, default="[]")
    sub = models.ForeignKey(
        "user_content.Account",
        blank=False,
        null=False,
        db_constraint=False,
        on_delete=models.CASCADE,
    )
    iss = models.CharField(
        max_length=100, blank=True, null=True, default="network-social"
    )
    exp = models.BigIntegerField(blank=True, null=True, default=token_expiry)
    iat = models.BigIntegerField(blank=True, null=True, default=current_time)
    nbf = models.BigIntegerField(blank=True, null=True, default=current_time)

    device_name = models.CharField(max_length=250, blank=True, null=True)
    os = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=AccessTokenDeviceEnum.to_choices(),
        default=str(
            AccessTokenDeviceEnum.WEB,
        ).upper(),
    )
    os_version = models.CharField(max_length=10, blank=True, null=True)

    status = models.IntegerField(
        null=False,
        blank=False,
        default=int(AccessTokenStatusEnum.ACTIVE),
        choices=AccessTokenStatusEnum.to_choices(),
    )

    def generate_token(self, is_refresh: bool = False):
        exp_time: int = self.exp
        if is_refresh:
            exp_time += 30 * 86400
        return jwt.encode(
            {
                "jti": str(self.id),
                "scopes": json.loads(self.scopes),
                "sub": str(self.sub_id),
                "iss": self.iss,
                "exp": exp_time,
                "iat": self.iat,
                "user_type": self.sub.type,
            },
            settings.JWT_PRIVATE_SIGNATURE,
            algorithm="HS256",
        )
