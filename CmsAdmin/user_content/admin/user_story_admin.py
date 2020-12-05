from django.contrib import admin

from core.admin.utils import linkify
from core.admin.base_admin import BaseAdmin

from user_content.models import UserStory


@admin.register(UserStory)
class UserStoryAdmin(BaseAdmin):
    list_display = [linkify("account"), "content", "media_url", "status"]
    fields = ["account", "content", "media_url", "status"]