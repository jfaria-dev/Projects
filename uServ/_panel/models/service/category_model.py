from django.db import models
from django.contrib import admin
from colorfield.fields import ColorField

class Category(models.Model):  
    # VALIDATION METHODS 
    def image_path(instance, filename):
    # Cria um caminho baseado no ID do fornecedor e no nome do arquivo
        url = f"panel/images/categories/{filename}"
        print(url)
        return url
    
    # FIELDS
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='parents')
    bg_color = ColorField(default="#ffffff", null=True, blank=True)
    text_color = ColorField(default="#000000", null=True, blank=True)
    photo = models.ImageField(upload_to=image_path, null=True, blank=True)
    active = models.BooleanField(default=True)
    
    class Meta:
      app_label = '_panel'
      db_table = 'category'
    
    # METHODS
    def __str__(self) -> str:
        return self.name
        
    def get_Segments():
        return Category.objects.filter(parent__isnull=True, active=True)
    
    def get_ById(id):
        print(id)
        return Category.objects.filter(pk=id).first()
    
    def get_Children(id):
        return Category.objects.filter(parent=id, active=True)

class CategoryAdmin(admin.ModelAdmin):
    list_filter = [("parent", admin.AllValuesFieldListFilter)]
    