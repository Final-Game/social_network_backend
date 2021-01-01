from django.contrib import admin
from core.admin.utils import linkify
from core.admin.base_admin import BaseAdmin

from chat_management.models import AccountMapper


@admin.register(AccountMapper)
class AccountMapperAdmin(BaseAdmin):
    list_display = [linkify("ref"), "full_name", "gender"]
    list_display_links = ["full_name"]
    fields = ["ref", "avatar", "birth_date", "gender", "full_name"]
