from django.contrib import admin

from core.admin.utils import linkify
from core.admin.base_admin import BaseAdmin

from user_content.models import UserCommentPost


@admin.register(UserCommentPost)
class UserCommentPostAdmin(BaseAdmin):
    list_display = [linkify("post"), linkify("sender"), linkify("base")]
    fields = ["post", "content", "sender", "base"]