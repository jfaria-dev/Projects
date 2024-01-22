from django.utils.translation import gettext_lazy as _
from ...models import Supplier
from django import forms

# register a new supplier
class SupplierForm(forms.ModelForm):   
    
    class Meta:
        model = Supplier
        fields = ['owner_name', 'email', 'phone']        
        labels = {
            'owner_name': _('Nome Completo'),
            'email': _('E-mail'),	
            'phone': _('Telefone para Contato')
        }
    
    def clean_phone(self):
        phone = str(self.cleaned_data.get('phone'))
        print('phone: ', phone)
        if len(phone) < 14:
            raise forms.ValidationError(_('Telefone Inválido.'))
        return phone
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            if Supplier.is_uniqueByEmail(email=email):
                raise forms.ValidationError(_('E-mail já Existe.'))
        return email
        