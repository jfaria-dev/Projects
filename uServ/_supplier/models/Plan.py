from django.db import models

class Plan(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.FloatField(null=False, blank=False, verbose_name="Valor")
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
       return self.name
    
    class Meta:
      app_label = '_supplier'
      db_table = 'plan'
      