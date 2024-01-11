from django.utils.translation import gettext_lazy as _
from django import forms
from ..models import Supplier

# update a supplier
class SupplierUpdateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['doc_number', 'fantasy_name']
        exclude = ['email', 'name', 'phone', 'password']  
        labels = {
            'doc_number': _('CPF/CNPJ:'),
            'fantasy_name': _('Nome Fantasia:')
        }       