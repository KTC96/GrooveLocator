# Generated by Django 3.2.23 on 2023-11-15 12:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('map', '0008_auto_20231115_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='saved',
            field=models.ManyToManyField(blank=True, related_name='saved', to=settings.AUTH_USER_MODEL),
        ),
    ]