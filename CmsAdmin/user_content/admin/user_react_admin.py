from django.contrib import admin

from core.admin.base_admin import BaseAdmin
from core.admin.utils import linkify

from user_content.models import UserReact


@admin.register(UserReact)
class UserReactAdmin(BaseAdmin):
    list_display = ["target_react_id", "type", linkify("sender")]
    fields = ["target_react_id", "type", "sender"]