# Generated by Django 2.2.16 on 2020-12-05 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_content', '0012_auto_20201205_0536'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserReact',
            new_name='UserReactPost',
        ),
    ]