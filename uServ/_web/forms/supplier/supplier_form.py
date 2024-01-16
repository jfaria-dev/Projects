from django.utils.translation import gettext_lazy as _
from ...models import Supplier
from django import forms

# register a new supplier
class SupplierForm(forms.ModelForm):   
    
    class Meta:
        model = Supplier
        fields = ['owner_name', 'email', 'phone', 'company_name', 'company_name_show', 'company_phone', 'company_document_number', 'owner_document_number']        
        labels = {
            'owner_name': _('Nome Completo'),
            'email': _('E-mail'),	
            'phone': _('Telefone para Contato'),	
            'company_name': _('Nome da Empresa'),
            'company_document_number': _('Cnpj'),
            'owner_document_number': _('Documento do Representante')
        } 
    
        
