# Generated by Django 3.2.23 on 2023-12-12 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_event_saved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(default='event', max_length=250, unique=True),
        ),
    ]
