# Generated by Django 4.2.7 on 2024-02-15 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_web', '0012_alter_screen_created_on_alter_supplierdetails_cnd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 15, 13, 41, 7, 514982)),
        ),
        migrations.AlterField(
            model_name='supplierorder',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 14, 13, 41, 7, 632951)),
        ),
    ]