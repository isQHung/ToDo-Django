from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput
from django import forms

class RegisterForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        # widgets = {
        #     'username': TextInput(attrs={
        #         'class': "form-control",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #     }),
            
        #     'password': PasswordInput(attrs={
        #         'class': "form-control"
        #     }),
        # }

            