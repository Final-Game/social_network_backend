from django.contrib import admin

from core.admin.utils import linkify
from core.admin.base_admin import BaseAdmin

from chat_management.models import UserRoom


@admin.register(UserRoom)
class UserRoomAdmin(BaseAdmin):
    list_display = [
        linkify("room"),
        linkify("account"),
        "nick_name",
    ]
    fields = [
        "room",
        "account",
        "nick_name",
    ]
