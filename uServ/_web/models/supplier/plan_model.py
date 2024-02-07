from django.db import models

class Plan(models.Model):
    # FUNCTIONS
    def getPlans():
        return Plan.objects.filter(is_active=True)
    
    def get_ById(id):
        return Plan.objects.filter(id=id).first()
       
    
    # FIELDS
    attributes = models.ManyToManyField('Attribute', related_name='plan_attributes', blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        app_label = '_web'
        db_table = 'plan'

class Attribute(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return f'{self.name} - {self.description} - {self.quantity}'
    
    class Meta:
        app_label = '_web'
        db_table = 'attributes' 