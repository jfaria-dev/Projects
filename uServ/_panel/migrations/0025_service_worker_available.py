# Generated by Django 4.2.7 on 2024-02-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_panel', '0024_alter_service_execution_time_alter_service_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='worker_available',
            field=models.BooleanField(default=False),
        ),
    ]