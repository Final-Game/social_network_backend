# Generated by Django 2.2.16 on 2020-12-27 05:35

import core.domain.models.base_model
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_management', '0014_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaMessage',
            fields=[
                ('id', models.CharField(default=core.domain.models.base_model.pkgen, max_length=36, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('media_url', models.CharField(max_length=300)),
                ('type', models.IntegerField(blank=True, choices=[(0, 'VIDEO'), (1, 'PHOTO')], default=1, null=True)),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message_related', to='chat_management.Message')),
            ],
            options={
                'db_table': 'cm_media_messages',
            },
        ),
    ]
