# Generated by Django 4.2.7 on 2024-02-15 22:55

import _web.models.supplier.details_model
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_web', '0017_alter_screen_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 15, 19, 55, 29, 383086)),
        ),
        migrations.AlterField(
            model_name='supplierdetails',
            name='birthdate',
            field=models.DateField(blank=True, null=True, validators=[_web.models.supplier.details_model.SupplierDetails.date_is_valid]),
        ),
        migrations.AlterField(
            model_name='supplierorder',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 14, 19, 55, 29, 501119)),
        ),
    ]