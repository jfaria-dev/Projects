from django.utils.translation import gettext_lazy as _
from ..models import SupplierService, Service, Category, Unity
from django import forms

class ServiceForm(forms.ModelForm):  
    class Meta:
        model = SupplierService
        fields = [
            'service', 
            'price', 
            'unit',
            'service_image', 
            'requirements',
            'active'
            ]
        exclude = ['warranty', 'delivery_time']
        labels = {
            'service': _('Serviço:'),
            'price': _('Valor:'),			
            'service_image': _('Imagem:'),	
            'requirements': _('Exigências para Execução:'),	
            'active': _('Ativo:')
        }
    
    unit = forms.ModelChoiceField(queryset=Unity.objects.all(), label='Unidade de Valor:')
