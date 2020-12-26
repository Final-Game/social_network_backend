# Generated by Django 2.2.16 on 2020-12-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_management', '0011_message_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='type',
            field=models.IntegerField(choices=[(0, 'NORMAL'), (1, 'SMART'), (2, 'MATCH')], default=0),
        ),
    ]
