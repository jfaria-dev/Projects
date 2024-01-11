from django.utils.translation import gettext_lazy as _
from ..api.Cielo.models.TransactionSale import Customer, CreditCard
from django import forms

# register a new supplier
class CieloCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Name', 'Birthdate']
        exclude = ['Email', 'Address', 'DeliveryAddress', 'Billing']
        labels = {
            'Name': _('Nome do Titular:'),
            'Birthdate': _('Data de Nascimento:')
        } 
    
    Name = forms.CharField(
        widget = forms.TextInput(attrs={
                                    "class": "form-control",
                                    "placeholder":"Nome do Titular"
                                    }))
    Birthdate = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'class': 'form-control'
        }))  

class CieloCreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['CardNumber', 'ExpirationDate', 'SecurityCode']
        exclude = ['Holder', 'SaveCard', 'Brand', 'CardOnFile']
        labels = {
            'CardNumber': _('Numero do Cartao:'),
            'ExpirationDate': _('Vencimento:'),
            'SecurityCode': _('CVV:')
        }
    
    SecurityCode = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"CVV"}))
    ExpirationDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder':'Vencimento', 'type': 'date'}))
    CardNumber = forms.CharField(
        max_length=19, 
        widget = forms.TextInput(attrs={
                                    "class": "form-control",
                                    "placeholder":"Numero do Cartão",
                                    "hx-get": "/check_card",
                                    "hx-trigger": "keyup",
                                    "hx-target": "#card-error",
                                    })
    )
    
