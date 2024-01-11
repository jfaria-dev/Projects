
from django.db import models

class Unity(models.Model):
    unit = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.unit
    
    class Meta:
      app_label = '_dashboard'
      db_table = 'unity'   