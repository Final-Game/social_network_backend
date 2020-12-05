from django.contrib import admin

from core.admin.base_admin import BaseAdmin
from core.admin.utils import linkify

from user_content.models import UserReactPost


@admin.register(UserReactPost)
class UserReactPostAdmin(BaseAdmin):
    list_display = ["short_id", linkify("post"), "type", linkify("sender")]
    fields = ["post", "type", "sender"]
    list_display_links = ["short_id"]