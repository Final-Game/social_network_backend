# Generated by Django 2.2.16 on 2020-12-05 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media_content', '0002_auto_20201128_0839'),
        ('user_content', '0011_post_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userreact',
            name='target_react_id',
        ),
        migrations.AddField(
            model_name='post',
            name='medias',
            field=models.ManyToManyField(through='media_content.MediaPost', to='media_content.Media'),
        ),
        migrations.AddField(
            model_name='userreact',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user_content.Post'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='userreact',
            table='user_react_post',
        ),
    ]
