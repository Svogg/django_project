# Generated by Django 3.2 on 2022-11-15 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20221116_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personfilmwork',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='personfilmwork',
            name='role',
        ),
    ]
