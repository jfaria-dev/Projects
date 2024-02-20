from django.db import models
from _panel.models import Service

class Event(models.Model):    
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='events')    
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pendente'), ('confirmed', 'Confirmado'), ('canceled', 'Cancelado')])

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = '_schedule'
        db_table = 'event'