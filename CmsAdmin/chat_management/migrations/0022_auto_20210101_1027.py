# Generated by Django 2.2.16 on 2021-01-01 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_management', '0021_auto_20210101_1025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='receiver_mapper',
            new_name='receiver',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='sender_mapper',
            new_name='sender',
        ),
        migrations.RenameField(
            model_name='matchsetting',
            old_name='account_mapper',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='userroom',
            old_name='account_mapper',
            new_name='account',
        ),
        migrations.AlterUniqueTogether(
            name='match',
            unique_together={('sender', 'receiver')},
        ),
    ]
