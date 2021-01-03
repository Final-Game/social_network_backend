from django.urls import path
from user_content.api import account_info_api
from django.conf.urls import url

urlpatterns = [url(r"^accounts/(?P<account_id>[\w-]+)/info$", account_info_api)]
