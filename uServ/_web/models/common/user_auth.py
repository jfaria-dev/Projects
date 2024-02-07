from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserAuthManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O campo de email deve ser preenchido.")    
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)

class UserAuth(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_client = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserAuthManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    
    class Meta:
        app_label = '_web'
        db_table = 'user_auth'
    
    def get_ByEmail(email):
        return UserAuth.objects.filter(email=email).first()
    
    def create_user(email, password, is_supplier):
        if is_supplier:
            return UserAuth.objects.create_user(email=email, password=password, is_supplier=is_supplier)
        return UserAuth.objects.create_user(email=email, password=password, is_client=True)
        