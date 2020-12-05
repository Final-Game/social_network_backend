from django.contrib import admin

from core.admin.utils import linkify
from core.admin import BaseAdmin
from user_content.models import StoryViewer


@admin.register(StoryViewer)
class StoryViewerAdmin(BaseAdmin):
    list_display = [linkify("story"), linkify("viewer"), "react_type"]
    fields = ["story", "viewer", "react_type"]