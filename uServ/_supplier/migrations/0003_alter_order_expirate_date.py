# Generated by Django 4.2.7 on 2024-01-12 19:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_supplier', '0002_alter_order_expirate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expirate_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 11, 16, 21, 41, 752332)),
        ),
    ]