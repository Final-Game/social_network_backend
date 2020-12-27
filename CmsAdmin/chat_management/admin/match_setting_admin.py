from django.contrib import admin

from core.admin.base_admin import BaseAdmin
from core.admin.utils import linkify
from chat_management.models import MatchSetting


@admin.register(MatchSetting)
class MatchSettingAdmin(BaseAdmin):
    list_display = [linkify("account"), "target_gender"]
    fields = ["account", "target_gender", "max_distance", "min_age", "max_age"]