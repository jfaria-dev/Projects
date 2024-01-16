from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class Supplier(models.Model):
        
    owner_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=19,
                             validators=[
                                        RegexValidator(
                                            regex=r'^[(]\d{2}[)] \d{5}[-]\d{4}$',
                                            message="Informe um telefone válido.",
                                            code="invalid_registration",
                                        ),]) # +55 (00) 00000-0000
    
    company_name = models.CharField(max_length=250, null=True, blank=True)
    company_name_show = models.CharField(max_length=250, null=True, blank=True)
    company_document_number = models.CharField(max_length=18, null=True, blank=True) # 00.000.000/00000-00
    company_phone = models.CharField(max_length=19, null=True, blank=True)
    owner_document_number = models.CharField(max_length=14, null=True, blank=True) # 000.000.000-00
    professional_birthdate = models.DateField(null=True, blank=True)    
    
    def image_path(instance, filename):
        return '/'.join(['supplier', instance.id, filename])
    photo = models.ImageField(upload_to=image_path, null=True, blank=True)
        
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
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
    
    class Meta:
      app_label = '_web'
      db_table = 'supplier'
      
    
    def get_byId(id):
        return Supplier.objects.filter(id=id).first()
      
      