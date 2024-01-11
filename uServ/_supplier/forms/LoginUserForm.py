from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm

from django import forms
from django.contrib.auth import authenticate
from django.forms.widgets import PasswordInput, TextInput

# login an user
class LoginUserForm(AuthenticationForm):
    username = forms.EmailField(error_messages={'invalid':"E-mail Inválido"},
                                label='Email',
                                widget=TextInput(attrs={                                    
                                    'class': 'input100',
                                    'aria-label': "email",
                                    'name': "username",
                                    'aria-describedby': "basic-addon1"
    }))
    password = forms.CharField(widget=PasswordInput(attrs={
        'class': 'input100',
        'aria-label': "password",
        'name': "password",
        'aria-describedby': "basic-addon1"
    }))    
    
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is None:
            raise forms.ValidationError('Email ou Senha inválidos')
        return self.cleaned_data
    