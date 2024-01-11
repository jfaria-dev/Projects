# Generated by Django 4.2.7 on 2024-01-03 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'services',
            },
        ),
        migrations.CreateModel(
            name='Unity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'unity',
            },
        ),
        migrations.CreateModel(
            name='SupplierService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('service_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('delivery_time', models.DurationField(blank=True, null=True)),
                ('warranty', models.BooleanField(default=False)),
                ('requirements', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='_dashboard.service')),
            ],
            options={
                'db_table': 'supplier_service',
            },
        ),
    ]
