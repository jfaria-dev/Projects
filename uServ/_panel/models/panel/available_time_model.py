from django.db import models

HOUR_CHOICES = [
    ("{:02d}".format(i) + ':00', "{:02d}".format(i) + ':00') for i in range(0, 24)
    ]



class AvailableTime(models.Model):
    supplier = models.ForeignKey('_web.Supplier', on_delete=models.CASCADE, related_name='available_times')
    day_of_week = models.CharField(max_length=20, choices=[('Domingo', 'Domingo'), ('Segunda', 'Segunda'), ('Terça', 'Terça'), ('Quarta', 'Quarta'), ('Quinta', 'Quinta'), ('Sexta', 'Sexta'), ('Sábado', 'Sábado')], default='Domingo') 
    open_time = models.CharField(max_length=5, choices=HOUR_CHOICES, default='08:00')
    close_time = models.CharField(max_length=5, choices=HOUR_CHOICES, default='18:00')
    
    class Meta:
        app_label = '_web'
        db_table = 'supplier_availability_time'
    
    
    
    def get_ById(id):
        at = AvailableTime.objects.filter(id=id).first()
       
        return at
    
    