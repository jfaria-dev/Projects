from django.db import models
from datetime import datetime, timedelta

class Order(models.Model):
    # FUNCTIONS
    def get_ById(id):
        return Order.objects.filter(id=id).first()
        
    def get_BySupplierId(supplier_id):
        return Order.objects.filter(supplier_id=supplier_id)
    
    def get_BySupplierHasOrderValid(supplier_id):
        orders = Order.objects.filter(supplier_id=supplier_id)
        order = orders.filter(expires_at__lte=datetime.now()).first()
        return order
       
    
    # FIELDS
    supplier = models.ManyToManyField('Supplier', related_name='orders_supplier')
    plan = models.ManyToManyField('Plan', related_name='orders_plan')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default= datetime.now() + timedelta(days=365))
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        app_label = '_web'
        db_table = 'order'