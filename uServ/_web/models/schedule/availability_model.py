from django.db import models
from _web.models import Supplier

class Availability(models.Model):
    provider = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    weekday = models.IntegerField(choices=[(0, 'Segunda-feira'), (1, 'Terça-feira'), (2, 'Quarta-feira'), (3, 'Quinta-feira'), (4, 'Sexta-feira'), (5, 'Sábado'), (6, 'Domingo')])
    start_time = models.TimeField()
    end_time = models.TimeField()