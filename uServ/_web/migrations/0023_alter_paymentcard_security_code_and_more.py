# Generated by Django 4.2.7 on 2024-02-18 00:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_web', '0022_supplierdetails_segment_alter_screen_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentcard',
            name='security_code',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='screen',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 17, 21, 46, 43, 628896)),
        ),
        migrations.AlterField(
            model_name='supplierorder',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 16, 21, 46, 43, 772934)),
        ),
    ]