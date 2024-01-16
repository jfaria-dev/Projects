from django import forms
from ...models import SupplierAddress

class AddressForm(forms.ModelForm):
    class Meta:
        model = SupplierAddress
        fields = ['street', 'number', 'complement', 'neighborhood', 'city', 'state', 'postal_code']


        