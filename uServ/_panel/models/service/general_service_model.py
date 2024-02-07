from django.db import models
from .service_model import Service

class GeneralService(models.Model):
    description = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, related_name='services', null=True)  
    
    def __str__(self) -> str:
        return self.description
    
    class Meta:
        app_label = '_panel'
        db_table = 'general_service'
        
    # METHODS
    def get_Services(query): 
        general_services = GeneralService.objects.filter(description__icontains=query)
        services :list(Service)= []
        for general_service in general_services:
            services.extend(general_service.services.all())
        return services	