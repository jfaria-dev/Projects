from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

class SupplierOrder(models.Model):
    # FUNCTIONS
    def get_ById(id):
        return SupplierOrder.objects.filter(id=id).first()
        
    def get_BySupplierId(supplier_id):
        return SupplierOrder.objects.filter(supplier_id=supplier_id).first()
    
    def get_SupplierHasOrderValid(supplier):
        # orders = SupplierOrder.objects.filter(supplier=supplier)
        orders = supplier.orders_supplier.filter(expires_at__gt=timezone.now())
        if orders.count() > 0:
            return orders
        return None
    
    # FIELDS
    supplier = models.ForeignKey('Supplier', related_name='orders_supplier', on_delete=models.DO_NOTHING)
    plan = models.ForeignKey('Plan', related_name='orders_plan', on_delete=models.DO_NOTHING)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default= datetime.now() + timedelta(days=365))
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        app_label = '_web'
        db_table = 'supplier_order'           