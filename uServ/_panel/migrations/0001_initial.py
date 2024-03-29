# Generated by Django 5.0.2 on 2024-03-02 18:56

import _panel.models.service.category_model
import _panel.models.service.service_model
import _panel.models.team.team_model
import _panel.models.team.worker_model
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=_panel.models.team.team_model.Team.team_image_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'team',
            },
        ),
        migrations.CreateModel(
            name='UnitForService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'unit_for_service',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('document', models.CharField(max_length=20, validators=[_panel.models.team.worker_model.Worker.company_document_is_valid])),
                ('position', models.CharField(max_length=100)),
                ('employment_date', models.DateField(validators=[_panel.models.team.worker_model.Worker.date_is_valid])),
                ('photo', models.ImageField(blank=True, upload_to=_panel.models.team.worker_model.Worker.worker_image_path)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'worker',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=_panel.models.service.category_model.Category.image_path)),
                ('active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parents', to='_panel.category')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='GeneralService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services', to='_panel.category')),
            ],
            options={
                'db_table': 'general_service',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('service_image', models.ImageField(blank=True, null=True, upload_to=_panel.models.service.service_model.Service.supplier_service_image_path)),
                ('requirements', models.TextField(blank=True, null=True)),
                ('execution_time', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('unit_of_execution', models.CharField(blank=True, max_length=50, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('general_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='_panel.generalservice')),
            ],
            options={
                'db_table': 'service',
            },
        ),
    ]
