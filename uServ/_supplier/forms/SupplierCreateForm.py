from django.utils.translation import gettext_lazy as _
from ..models import Supplier
from django import forms

# register a new supplier
class SupplierCreateForm(forms.ModelForm):   
    
    class Meta:
        model = Supplier
        fields = ['name', 'email', 'phone', 'password']
        exclude = ['doc_number', 'fantasy_name']
        labels = {
            'name': _('Nome Fantasia ou do Fornecedor'),
            'email': _('E-mail'),	
            'phone': _('Telefone para Contato:'),	
            'password': _('Senha'),	
        }   
    
   

    def clean_email(self):
        email = self.cleaned_data['email']
        if Supplier.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está em uso.')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone']
        if len(phone_number) != 15:
            raise forms.ValidationError('O telefone deve ter 15 dígitos.')
        return phone_number   