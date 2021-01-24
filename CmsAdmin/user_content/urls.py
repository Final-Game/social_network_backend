from user_content.api.resources.user_account_api import UserAccountApi
from django.urls import path
from user_content.api import account_info_api
from django.conf.urls import url

cms_urlpatterns = [
    url(r"^user_accounts/", UserAccountApi.as_view({"get": "list", "post": "create"}))
]


urlpatterns = [
    url(r"^accounts/(?P<account_id>[\w-]+)/info$", account_info_api)
] + cms_urlpatterns
