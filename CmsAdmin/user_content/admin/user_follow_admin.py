from django.contrib import admin

from core.admin.base_admin import BaseAdmin
from core.admin.utils import linkify

from user_content.models import UserFollow


@admin.register(UserFollow)
class UserFollowAdmin(BaseAdmin):
    list_display = [linkify("source"), linkify("target")]
    fields = ["source", "target"]