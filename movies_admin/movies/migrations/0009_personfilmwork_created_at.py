# Generated by Django 3.2 on 2022-11-15 22:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_personfilmwork_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='personfilmwork',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 11, 15, 22, 22, 7, 727917, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
