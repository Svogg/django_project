# Generated by Django 3.2 on 2022-11-15 21:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20221116_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmwork',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 11, 15, 21, 55, 4, 406667, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filmwork',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 11, 15, 21, 55, 21, 421465, tzinfo=utc), verbose_name='modified'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genre',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 11, 15, 21, 55, 28, 249246, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genre',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 11, 15, 21, 55, 40, 795930, tzinfo=utc), verbose_name='modified'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 11, 15, 21, 55, 47, 823643, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 11, 15, 21, 55, 55, 257377, tzinfo=utc), verbose_name='modified'),
            preserve_default=False,
        ),
    ]