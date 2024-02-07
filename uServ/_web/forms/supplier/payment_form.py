from django.utils.translation import gettext_lazy as _
import re
from django import forms
from ...models import PaymentCard

class PaymentForm(forms.ModelForm):
    # FIELDS
    expiration_date = forms.CharField(label="Data de Vencimento", max_length=5)
    class Meta:
        model = PaymentCard
        fields = [
            'card_number', 
            'card_holder_name', 
            'expiration_date', 
            'security_code']
        labes = {
            'card_number': _('Número do cartão'),
            'card_holder_name': _('Nome do titular'),
            'expiration_date': _('Data de expiração'),
            'security_code': _('Código de segurança')
            }
        widget = {
            'card_number': forms.TextInput(attrs={'placeholder': 'Número do cartão'}),
            'card_holder_name': forms.TextInput(attrs={'placeholder': 'Nome do titular'}),
            'expiration_date': forms.TextInput(attrs={'placeholder': 'Data de expiração'}),
            'security_code': forms.TextInput(attrs={'placeholder': 'Código de segurança'})
            }
    # FUNCTIONS
    
    
    # CLEAN
    def clean_expiration_date(self):
        expiration_date = self.cleaned_data['expiration_date']
        if not re.match(r'^\d{2}/\d{2}$', expiration_date):
            raise forms.ValidationError("Invalid date format. Please use MM/YY.")
        return expiration_date
    
    