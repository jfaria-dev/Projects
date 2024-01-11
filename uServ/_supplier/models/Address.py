from django.db import models

class Address(models.Model):
    supplier = models.ForeignKey('Supplier', related_name='addresses', on_delete=models.CASCADE)
    street = models.CharField(max_length=300)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=100)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=8)
    
    class Meta:
      app_label = '_supplier'
      db_table = 'address'