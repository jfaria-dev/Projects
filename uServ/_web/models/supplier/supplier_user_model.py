# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from .supplier_model import Supplier
# from django.db import models

# class SupplierUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("O campo de email deve ser preenchido.")
        
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
        
#         return self.create_user(email, password, **extra_fields)

# class SupplierUser(AbstractBaseUser, PermissionsMixin):
#     def get_ByEmail(email):
#         return SupplierUser.objects.filter(email=email).first()
    
    
#     email = models.EmailField(unique=True)
#     supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = SupplierUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['password']

#     def __str__(self):
#         return self.email
    
#     def create_user(email, password, supplier):
#         user = SupplierUser.objects.create_user(email=email, password=password, supplier=supplier)
        
    
#     class Meta:
#         app_label = '_web'
        
    