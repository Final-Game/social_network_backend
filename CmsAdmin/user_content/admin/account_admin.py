from core.admin.utils import linkify
from core.admin.base_admin import BaseAdmin
from typing import Sequence
from django.http import HttpRequest
from django.contrib import admin

from user_content.models import Account


@admin.register(Account)
class AccountAdmin(BaseAdmin):
    list_display = [
        "username",
        linkify("connection"),
        linkify("profile"),
        "type",
        "status",
    ]
    search_fields = ["username", "id"]
    list_filter = ["type", "status"]
    list_display_links = ["username"]
    fields = ["username", "password", "connection", "profile", "type", "status"]
