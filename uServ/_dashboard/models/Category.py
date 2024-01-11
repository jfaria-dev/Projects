from django.db import models

class Category(models.Model):   
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='parents')
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
      app_label = '_dashboard'
      db_table = 'category'