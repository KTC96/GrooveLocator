# Generated by Django 3.2.23 on 2023-11-14 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_auto_20231114_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_venue',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
