from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class User(models.Model):
    user_auth = models.OneToOneField('_auth.UserAuth', on_delete=models.CASCADE, null=True, related_name='user_client')
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=16, null=True)    
    document = models.CharField(max_length=18, null=True)
    photo = models.ImageField(upload_to='user/photo', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # formas de pagamento adicionar depois)
    
    
    class Meta:
        app_label = '_web'
        db_table = 'user'
        