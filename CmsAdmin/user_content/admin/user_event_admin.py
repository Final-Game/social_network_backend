from django.contrib import admin

from core.admin.utils import linkify
from core.admin.base_admin import BaseAdmin

from user_content.models import UserEvent


@admin.register(UserEvent)
class UserEventAdmin(BaseAdmin):
    list_display = [linkify("account"), linkify("event"), "start_date", "end_date"]
    fields = ["account", "event", "start_date", "end_date"]