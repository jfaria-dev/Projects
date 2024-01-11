from django.db import models

class ResponseCardBind(models.Model):
    status = models.CharField(max_length=2)
    provider = models.CharField(max_length=4)
    card_type = models.CharField(max_length=9)
    foreign_card = models.BooleanField()
    corporate_card = models.BooleanField()
    issuer = models.CharField(max_length=20)
    issuer_code = models.CharField(max_length=3)