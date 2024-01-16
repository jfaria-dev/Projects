from django.db import models

class SupplierAddress(models.Model):
    
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=200, null=True, blank=True)
    neighborhood = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=10)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def get_bySupplierId(supplier_id):
        return SupplierAddress.objects.filter(supplier_id=supplier_id).first()
    
    class Meta:
        app_label = '_web'
        db_table = 'address'