from django.db import models

class UnitForService(models.Model):
    general_service = models.ForeignKey('GeneralService', on_delete=models.CASCADE, related_name='units_for_service')
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    class Meta:
        app_label = '_panel'
        db_table = 'unit_for_service'
        
    def __str__(self) -> str:
        return self.name
    
     