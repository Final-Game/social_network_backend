# Generated by Django 2.2.16 on 2021-01-01 09:47

from django.db import migrations
from django.db import transaction


def update_account_mapper(apps, schema_editor):
    Account = apps.get_model("user_content", "Account")
    AccountMapper = apps.get_model("chat_management", "AccountMapper")

    accounts = Account.objects.all()

    with transaction.atomic():
        for account in accounts:
            full_name: str = f"{account.profile and account.profile.first_name or ''} {account.profile and account.profile.last_name or ''}"
            account_mapper_data: dict = {
                "ref": account,
                "avatar": account.profile and account.profile.avatar,
                "birth_date": account.profile and account.profile.birth_date,
                "gender": account.profile and account.profile.gender,
                "full_name": full_name,
            }
            AccountMapper.objects.create(**account_mapper_data)


class Migration(migrations.Migration):

    dependencies = [
        ("chat_management", "0017_accountmapper"),
    ]

    operations = [migrations.RunPython(update_account_mapper)]
