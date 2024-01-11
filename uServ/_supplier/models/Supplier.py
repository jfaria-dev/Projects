from django.db import models
from .Address import Address


class Supplier(models.Model):
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=16) # +55(00)00000-0000
    password = models.CharField(max_length=128)
        
    doc_number = models.CharField(max_length=18, null=True) # 00.000.000/00000-00
    name = models.CharField(max_length=150, null=True)
    fantasy_name = models.CharField(max_length=150, null=True)
    
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    class Meta:
      app_label = '_supplier'
      db_table = 'supplier'
      