from django.utils.translation import gettext_lazy as _

from django import forms
from ...models import SupplierAddress

class SupplierAddressForm(forms.ModelForm):
    class Meta:
        model = SupplierAddress
        fields = [
            'postal_code',
            'street', 
            'number', 
            'complement', 
            'neighborhood', 
            'city', 
            'state', 
        ]
        labels = {
            'postal_code': _('CEP'),
            'street': _('Logradouro'), 
            'number': _('Número'),
            'complement': _('Complemento'),
            'neighborhood': _('Bairro'),
            'city': _('Cidade'),
            'state': _('Estado'),
        }
        widgets = {
            'postal_code': forms.TextInput(attrs={'placeholder':'00.000-000'}),
            'street': forms.TextInput(attrs={'placeholder': 'Rua, Avenida, etc.'}),
            'number': forms.TextInput(attrs={'placeholder': 'Número'}),
            'complement': forms.TextInput(attrs={'placeholder': 'Complemento'}),
            'neighborhood': forms.TextInput(attrs={'placeholder': 'Bairro'}),
            'city': forms.TextInput(attrs={'placeholder': 'Cidade'}),
            'state': forms.TextInput(attrs={'placeholder': 'Estado'}),
        }
        error_messages = {
            "postal_code": {
                "invalid": _("Informe um CEP válido."),
            }
        }       
    

        def clean(self):
            cleaned_data = super().clean()
            
            postal_code = cleaned_data.get('postal_code')
            if len(postal_code) != 10:
                self.add_error('postal_code', "Informe um CEP válido")


