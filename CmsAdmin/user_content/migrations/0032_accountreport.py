# Generated by Django 2.2.16 on 2021-02-08 04:45

import core.domain.models.base_model
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_content', '0031_account_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountReport',
            fields=[
                ('id', models.CharField(default=core.domain.models.base_model.pkgen, max_length=36, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_account', to='user_content.Account')),
                ('related_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_content.Post')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_account', to='user_content.Account')),
            ],
            options={
                'db_table': 'uc_account_reports',
            },
        ),
    ]
