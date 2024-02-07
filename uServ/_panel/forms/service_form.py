from django import forms
from django.utils.translation import gettext_lazy as _
from ..models import Service

class ServiceForm(forms.ModelForm):  
    class Meta:
        model = Service
        fields = [
            'general_service', 
            'price', 
            'unit',
            'execution_time',
            'service_image', 
            'requirements',
            'active'
            ]
        exclude = ['warranty', 'delivery_time']
        labels = {
            'general_service': _('Serviço:'),
            'price': _('Valor:'),			
            'service_image': _('Imagem:'),	
            'requirements': _('Exigências para Execução:'),	
            'active': _('Ativo:')
        }