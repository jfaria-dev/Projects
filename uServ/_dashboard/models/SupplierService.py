from django.db import models
from _supplier.models import Supplier, SupplierUser

class Service(models.Model):
    description = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, related_name='services', null=True)
    
    class Meta:
      app_label = '_dashboard'
      db_table = 'services'



class SupplierService(models.Model):
  def supplier_service_image_path(instance, filename):
    # Cria um caminho baseado no ID do fornecedor e no nome do arquivo
    url = f"dashboard/images/{instance.supplier.id}/services/{instance.id}_{filename}"
    print(url)
    return url
  
  supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='services')
  service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='services')
  unit = models.ForeignKey('Unity', on_delete=models.CASCADE, null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  service_image = models.ImageField(upload_to=supplier_service_image_path, null=True, blank=True)
  requirements = models.TextField(null=True, blank=True)
  active = models.BooleanField(default=True)
  user = models.ForeignKey(SupplierUser, on_delete=models.SET_NULL, null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(null=True, blank=True)
  
  class Meta:
    app_label = '_dashboard'
    db_table = 'supplier_service'






