from django.db import models
from _web.models import Supplier

class Team(models.Model):
    # METHODS
    def get_ById(id):
        return Team.objects.get(id=id)
    
    def team_image_path(instance, filename):
    # Cria um caminho baseado no ID do fornecedor e no nome do arquivo
        url = f"supplier/{instance.supplier.id}/team/{instance.id}/{filename}"
        print(url)
        return url
    
    supplier = models.ForeignKey('_web.Supplier', on_delete=models.CASCADE, related_name='teams')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to=team_image_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        app_label = '_panel'
        db_table = 'team'