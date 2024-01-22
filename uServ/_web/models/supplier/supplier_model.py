
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


        
class Supplier(models.Model): 
    # FUNCTIONS     
    def get_ById(id):
        return Supplier.objects.filter(id=id).first()
    
    def is_uniqueByEmail(email):
        return Supplier.objects.filter(email=email).exists()
    
    def get_ByEmail(email):
        return Supplier.objects.filter(email=email).first()
    
    # FIELDS        
    owner_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True,)                              
    phone = models.CharField(max_length=15,) # +55 (00) 00000-0000 
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
      app_label = '_web'
      db_table = 'supplier'
    
    # VALIDATIONS
    def clean_fields(self, exclude=None):
        """
        Clean all fields and raise a ValidationError containing a dict
        of all validation errors if any occur.
        """
        print('clean_fields')
        if exclude is None:
            exclude = []

        errors = {}
        for f in self._meta.fields:
            if f.name in exclude:
                continue
            # Skip validation for empty fields with blank=True. The developer
            # is responsible for making sure they have a valid value.
            raw_value = getattr(self, f.attname)
            if f.blank and raw_value in f.empty_values:
                continue
            try:
                setattr(self, f.attname, f.clean(raw_value, self))
            except ValidationError as e:
                errors[f.name] = e.error_list

        if errors:
            raise ValidationError(errors)
    
    
    
    
      
      