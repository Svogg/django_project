# Generated by Django 3.2 on 2022-11-15 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20221116_0055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genrefilmwork',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='personfilmwork',
            old_name='created',
            new_name='created_at',
        ),
    ]