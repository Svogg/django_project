# Generated by Django 3.2 on 2022-12-04 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_add_time_stamped_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genrefilmwork',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='personfilmwork',
            name='created_at',
        ),
    ]
