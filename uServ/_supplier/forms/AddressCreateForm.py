from django import forms
from ..models.Address import Address

# set supplier address
class AddressCreateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['supplier', 'street', 'number', 'complement', 'district', 'city', 'state', 'zip_code']
        
    def __init__(self, *args, **kwargs):
        # Remover supplier do formulário ao exibir
        super(AddressCreateForm, self).__init__(*args, **kwargs)
        self.fields['supplier'].widget = forms.HiddenInput()
        self.fields['supplier'].required = False