from django.db import models
from django.contrib.postgres.fields import JSONField

class Payment(models.Model):
    id = models.CharField(max_length=255, primary_key=True)  # Assuming ID is a string
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE)
    payer = models.ForeignKey('Payer', on_delete=models.CASCADE)
    additional_info = JSONField()

class PaymentMethod(models.Model):
    id = models.CharField(max_length=255, primary_key=True)  # Assuming ID is a string
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

class Payer(models.Model):
    id = models.CharField(max_length=255, primary_key=True)  # Assuming ID is a string
    email = models.EmailField()
    identification = JSONField()  # Store identification details
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)