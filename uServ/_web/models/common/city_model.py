from django.db import models

class City(models.Model):
    city = models.CharField(max_length=250)
    code = models.CharField(max_length=10)
    state = models.ForeignKey('State', on_delete=models.CASCADE, related_name='cities')
    
    class Meta:
        app_label = '_web'
        db_table = 'city'