from django import forms
from unemployeds.models import Unemployed


class Signup(forms.ModelForm):
    class Meta:
        model = Unemployed
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Write your first name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'email@exaple.com'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '10 digits please'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': '****************'
            }),
        }
