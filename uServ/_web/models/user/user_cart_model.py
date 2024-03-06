from typing import Any
from django.db import models    

from datetime import datetime, timedelta

HOUR_CHOICES = [
    ("{:02d}".format(i) + ':00', "{:02d}".format(i) + ':00') for i in range(0, 24)
    ]




class UserCart(models.Model):
    # ------------------METHODS------------------
    def get_ById(cart_id):
        return UserCart.objects.filter(id=cart_id).first()

    # ------------------FIELDS------------------
    user = models.ForeignKey('_web.User', on_delete=models.CASCADE, related_name='orders')
    service = models.ForeignKey('_panel.Service', on_delete=models.CASCADE, related_name='orders')
    worker = models.ForeignKey('_panel.Worker', on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    date = models.DateField()
    time = models.CharField(max_length=5, choices=HOUR_CHOICES, default='08:00')
    value = models.CharField(max_length=10, default='0,00')
    quantity = models.PositiveIntegerField()
    expired_at = models.DateTimeField(default= datetime.now() + timedelta(days=1))
    
    class Meta:
        app_label = '_web'
        db_table = 'user_cart'
    
 