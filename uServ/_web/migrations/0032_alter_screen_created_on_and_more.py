# Generated by Django 4.2.7 on 2024-02-18 18:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_web', '0031_alter_screen_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 18, 15, 53, 48, 811647)),
        ),
        migrations.AlterField(
            model_name='supplierorder',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 17, 15, 53, 48, 909647)),
        ),
    ]
