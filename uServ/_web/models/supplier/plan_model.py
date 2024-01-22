from django.db import models

class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    # Add any additional fields as per your requirements

    class Meta:
        app_label = '_web'
        db_table = 'plan'
