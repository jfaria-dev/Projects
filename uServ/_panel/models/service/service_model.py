from django.db import models

class Service(models.Model):
    def supplier_service_image_path(instance, filename):
    # Cria um caminho baseado no ID do fornecedor e no nome do arquivo
        url = f"panel/images/{instance.supplier.id}/services/{filename}"
        print(url)
        return url

    supplier = models.ForeignKey('_web.Supplier', on_delete=models.CASCADE, related_name='offered_services')
    general_service = models.ForeignKey('GeneralService', on_delete=models.CASCADE, related_name='services')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)
    service_image = models.ImageField(upload_to=supplier_service_image_path, null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    execution_time = models.TimeField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label = '_panel'
        db_table = 'service'
        
    
    # ---------------------- METHODS ----------------------
    def get_BySupplierId(supplier_id):
        return Service.objects.filter(supplier_id=supplier_id)
    
    def get_ById(service_id):
        return Service.objects.filter(id=service_id).first()