# Generated by Django 4.2.7 on 2024-02-08 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('_panel', '0003_alter_service_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='general_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='_panel.generalservice'),
        ),
    ]
