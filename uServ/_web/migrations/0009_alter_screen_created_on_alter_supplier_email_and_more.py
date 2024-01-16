# Generated by Django 4.2.7 on 2024-01-15 18:47

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_web', '0008_supplier_company_phone_alter_screen_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 15, 15, 47, 40, 15606)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='owner_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone',
            field=models.CharField(blank=True, max_length=19, null=True, validators=[django.core.validators.RegexValidator(code='invalid_registration', message='Informe um telefone válido.', regex='^[(]\\d{2}[)] \\d{5}[-]\\d{4}$')]),
        ),
        migrations.AlterField(
            model_name='supplieraddress',
            name='postal_code',
            field=models.CharField(max_length=10),
        ),
    ]
