from django.db import models

class User(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=16)
    document = models.CharField(max_length=18)
    password = models.CharField(max_length=128)
    
    class Meta:
        app_label = '_user'
        db_table = 'user'
        