# Generated by Django 4.2.7 on 2024-02-18 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_panel', '0019_delete_unitofexecution'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='unit_for_execution',
            new_name='unit_of_execution',
        ),
    ]
