from core.admin.utils import linkify
from core.admin.base_admin import BaseAdmin
from django.contrib import admin
from user_content.models import UserReactComment


@admin.register(UserReactComment)
class UserReactCommentAdmin(BaseAdmin):
    list_display = [linkify("sender"), linkify("comment"), "type"]
    fields = ["sender", "comment", "type"]