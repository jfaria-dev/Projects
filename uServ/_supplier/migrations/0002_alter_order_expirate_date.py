# Generated by Django 4.2.7 on 2024-01-03 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_supplier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expirate_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 2, 16, 30, 34, 364326)),
        ),
    ]
