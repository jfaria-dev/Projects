from django.db import models
from django.forms import ValidationError

import re
from itertools import cycle

from enum import Enum

class DocumentTypes(Enum):
    CNPJ = 'CNPJ'
    CPF = 'CPF'
  
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class SupplierDetails(models.Model):
    """
    Supplier Details Model
    """
    
    # FUNCTIONS
    def get_ById(id):
        return SupplierDetails.objects.filter(supplier_id=id).first()
    
    def is_uniqueByDocument(value :str):
        if SupplierDetails.objects.filter(company_document_number=value).exists():
            raise ValidationError("Documento já cadastrado.")
    
    def company_document_is_valid(value :str):  
        """Verify if numbers of document is valid. CPF or CNPJ

        Args:
            document (document): value of company_document_number

        Raises:
            ValidationError: if not inform all numbers
            ValidationError: if not inform only numbers
            ValidationError: if number is invalid
        """
        value = re.sub(r'\D', '', value)
        if len(value) not in [11, 14]:
            raise ValidationError("Documento inválido, informe todos os números.")        
        if value in (c * len(value) for c in "1234567890"):
            raise ValidationError("Documento inválido, informe apenas números") 
        value_reverse = value[::-1]        
        for i in range(2, 0, -1):            
            if len(value) == 14:
                document_enum = zip(cycle(range(2, 10)), value_reverse[i:])
            else:
                document_enum = enumerate(value_reverse[i:], start=2)            
            dv = sum(map(lambda x: int(x[1]) * x[0], document_enum)) * 10 % 11
            if value_reverse[i - 1:i] != str(dv % 10):
                raise ValidationError("Documento inválido.") 
    
    def image_path(instance, filename):
        """Set path to save image.

        Args:
            instance (Supplier): Supplier to be created
            filename (str): Name of file

        Returns:
            str: Path to save image
        """
        return '/'.join(['supplier', instance.id, filename])
    
        
    
    # FIELDS 
    supplier = models.OneToOneField('Supplier', on_delete=models.CASCADE, related_name='details')   
    document_type = models.CharField(max_length=4) # 1 - CPF, 2 - CNPJ
    company_document_number = models.CharField(max_length=19, validators=[company_document_is_valid, is_uniqueByDocument]) # 00.000.000/00000-00 or 000.000.000-00
    birthdate = models.DateField()    
    company_name = models.CharField(max_length=250)
    company_phone = models.CharField(max_length=15,) # +55 (00) 00000-0000
    company_name_show = models.CharField(max_length=250,)
    owner_document_number = models.CharField(max_length=14, validators=[company_document_is_valid]) # 000.000.000-00
    photo = models.ImageField(upload_to=image_path, null=True, blank=True)
    
    
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
      db_table = 'supplier_details'