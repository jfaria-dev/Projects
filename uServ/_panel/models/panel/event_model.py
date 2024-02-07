from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    
    class Meta:
        app_label = '_panel'
        db_table = 'event'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'