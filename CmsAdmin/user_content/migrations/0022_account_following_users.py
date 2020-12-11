# Generated by Django 2.2.16 on 2020-12-11 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_content', '0021_auto_20201205_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='following_users',
            field=models.ManyToManyField(related_name='following_user_relate', through='user_content.UserFollow', to='user_content.Account'),
        ),
    ]
