# Generated by Django 5.0.2 on 2024-03-13 22:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_web', '0009_alter_screen_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 13, 19, 17, 24, 795255)),
        ),
        migrations.AlterField(
            model_name='supplierorder',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 13, 19, 17, 24, 943976)),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='expired_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 14, 19, 17, 24, 952058)),
        ),
    ]
