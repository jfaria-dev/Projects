# Generated by Django 4.2.7 on 2024-02-18 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_panel', '0012_team_created_at_team_updated_at_worker_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='unit',
            new_name='unit_for_price',
        ),
        migrations.AddField(
            model_name='service',
            name='unit_for_execution',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='execution_time',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]