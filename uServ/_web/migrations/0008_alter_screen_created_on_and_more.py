# Generated by Django 5.0.2 on 2024-03-06 22:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_web', '0007_alter_screen_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 6, 19, 10, 45, 742216)),
        ),
        migrations.AlterField(
            model_name='supplierorder',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 6, 19, 10, 45, 857509)),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='expired_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 7, 19, 10, 45, 866496)),
        ),
    ]
