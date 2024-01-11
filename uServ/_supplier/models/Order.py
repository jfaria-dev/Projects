from django.db import models
from datetime import datetime, timedelta


class Order(models.Model):
    plan = models.ForeignKey('Plan', on_delete=models.DO_NOTHING)
    supplier = models.ForeignKey('Supplier', related_name='orders', on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField(auto_now_add=True)
    expirate_date = models.DateTimeField(default= datetime.now() + timedelta(days=365))
    value = models.DecimalField(max_digits=10, decimal_places=2)    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
      app_label = '_supplier'
      db_table = 'order'
      
      
    @classmethod
    def get_next_id(cls):
      id = cls.objects.order_by('-pk').first()
      highest_id = id.pk if not id is None else 0
      return highest_id + 1