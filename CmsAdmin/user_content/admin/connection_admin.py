from django.contrib import admin

from core.admin.base_admin import BaseAdmin
from user_content.models import Connection


@admin.register(Connection)
class ConnectionAdmin(BaseAdmin):
    list_display = ["google_token", "microsoft_token"]
    fields = ["google_token", "microsoft_token"]