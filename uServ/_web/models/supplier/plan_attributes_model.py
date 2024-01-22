from django.db import models

class PlanOffer(models.Model):
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE, related_name='attributes')
    attributes = models.ForeignKey('PlanAttributes', on_delete=models.CASCADE, related_name='plans')
    
    class Meta:
        app_label = '_web'
        db_table = 'plan_offer'

class PlanAttributes(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)    
    
    class Meta:
        app_label = '_web'
        db_table = 'plan_attributes'