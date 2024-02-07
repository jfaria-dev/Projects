from django.db import models
from django.contrib import admin

class Category(models.Model):   
    def image_path(instance, filename):
    # Cria um caminho baseado no ID do fornecedor e no nome do arquivo
        url = f"panel/images/categories/{filename}"
        print(url)
        return url
    
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='parents')
    photo = models.ImageField(upload_to=image_path, null=True, blank=True)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
      app_label = '_panel'
      db_table = 'category'
    
    def get_Segment():
        return Category.objects.filter(parent__isnull=True)
    
    


class CategoryAdmin(admin.ModelAdmin):
    list_filter = [("parent", admin.AllValuesFieldListFilter)]
    