# Generated by Django 3.2.23 on 2023-11-15 11:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('map', '0007_event_event_venue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='saved_by',
        ),
        migrations.AddField(
            model_name='event',
            name='saved',
            field=models.ManyToManyField(blank=True, related_name='saved_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
