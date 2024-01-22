from django.utils.translation import gettext_lazy as _
from ...models import SupplierDetails, DocumentTypes
from django import forms
import re

GEEKS_CHOICES =( 
    ("CNPJ", "CNPJ"), 
    ("CPF", "CPF") 
) 

# register a new supplier
class SupplierDetailsForm(forms.ModelForm): 
    document_type = forms.ChoiceField(choices=GEEKS_CHOICES, widget=forms.Select, label="Tipo de Documento")
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Data da Constituição")
    
    class Meta:
        model = SupplierDetails
        fields = [
            'document_type', 
            'company_document_number', 
            'birthdate',
            'company_name', 
            'company_phone', 
            'company_name_show', 
            'owner_document_number',
            ]        
        labels = {  
            'document_type': _('Tipo de Documento'),                             
            'company_document_number': _('CNPJ'),
            'company_name': _('Nome da Empresa'),
            'company_phone': _('Telefone da Empresa'),	
            'company_name_show': _('Nome no Aplicativo'),
            'owner_name': _('Nome Completo'),
            'owner_document_number': _('Documento do Representante (CPF)'),
            'birthdate': _('Data da Constituição'),
        } 
        widgets = {
            'company_document_number': forms.TextInput(attrs={'placeholder': '00.000.000/0000-00'}),
            'company_name': forms.TextInput(attrs={
                'placeholder': 'Informe o número do documento', 
                'disabled': 'disabled', 
                }),
            'owner_document_number': forms.TextInput(attrs={'placeholder': '000.000.000-00'}),            
            'company_name_show': forms.TextInput(attrs={'placeholder': 'Nome que aparecerá no App'}),            
            'company_phone': forms.TextInput(attrs={'placeholder': 'Telefone para contato'}),         
        }
       
    # def clean(self):
    #     document_number = self.cleaned_data.get('company_document_number')
    #     if document_number:
    #         if SupplierDetails.is_uniqueByDocument(document_number):
    #             raise forms.ValidationError(_('CNPJ existente.'))