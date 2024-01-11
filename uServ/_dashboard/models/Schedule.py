
from _user.models import User
from _supplier.models import SupplierUser
from .SupplierService import SupplierService
from django.db import models

class Schedule(models.Model):
    user = models.ForeignKey(User, related_name="schedules", null=True, blank=True, on_delete=models.SET_NULL)
    supplier_service = models.ForeignKey(SupplierService, related_name='schedules', null=True, blank=True, on_delete=models.SET_NULL)
    date_time = models.DateTimeField()
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    confirmation_date = models.DateTimeField()
    supplier_confirmation = models.ForeignKey(SupplierUser, related_name='schedules', null=True, blank=True, on_delete=models.SET_NULL)
        
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
      app_label = '_user'
      db_table = 'schedule'