from django.db import models
from django.core.validators import RegexValidator
from django.http import JsonResponse
import requests


class SupplierAddress(models.Model):
    # FUNCTIONS
    def api_get_addres_information(postal_code):   
        """Get the address from the postal code through the BrasilAPI: 
            "https://brasilapi.com.br/api/cep/v2/{postal_code}"  
        Args:
            request (string): postal code of the address

        Returns:
            Json: 
                {
                    "cep": "01001000",
                    "state": "SP",
                    "city": "São Paulo",
                    "neighborhood": "Sé",
                    "street": "Praça da Sé - lado ímpar",
                    "service": "correios-alt",
                    "location": {
                        "type": "Point",
                        "coordinates": {        
                        }
                }
        """     
        postal_code = postal_code.replace('-', '').replace('.', '')        
        url = f"https://brasilapi.com.br/api/cep/v2/{postal_code}"  
        response = requests.get(url)    
        data = response.json()
        print('d: ', data)    
        return  data
    
    def get_BySupplierId(supplier_id):
        return SupplierAddress.objects.filter(supplier_id=supplier_id).first()
    
    # FIELDS
    supplier = models.OneToOneField('Supplier', on_delete=models.CASCADE, related_name='address')
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=200, null=True, blank=True)
    neighborhood = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=10,
                                   validators= [
                                        RegexValidator(
                                            regex=r'^\d{2}[.]\d{3}[-]\d{3}$',
                                            message="Informe um Cep válido.",
                                            code="invalid_registration",
                                        ),]) # +55 (00) 00000-0000)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    
    
    class Meta:
        app_label = '_web'
        db_table = 'address'
        
    