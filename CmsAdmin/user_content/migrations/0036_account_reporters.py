# Generated by Django 2.2.16 on 2021-02-08 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_content', '0035_auto_20210208_0648'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='reporters',
            field=models.ManyToManyField(related_name='account_reporter_relate', through='user_content.AccountReport', to='user_content.Account'),
        ),
    ]
