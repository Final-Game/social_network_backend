from django.contrib import admin

from core.admin.base_admin import BaseAdmin
from core.admin.utils import linkify

from user_content.models import Post


@admin.register(Post)
class PostAdmin(BaseAdmin):
    list_display = [
        "own_reaction",
        linkify("account"),
        "content",
        "type",
        linkify("base"),
        "status",
    ]
    fields = ["own_reaction", "account", "content", "type", "base", "status"]
    list_filter = ["status"]
