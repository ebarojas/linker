# -*- encoding: utf-8 -*-

from django import forms
from headhunters.models import Headhunter


class Signup(forms.ModelForm):
    class Meta:
        model = Headhunter
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
        ]
        labels = {
            'first_name': 'Nombres:',
            'last_name': 'Apellidos:',
            'email': 'Correo electrónico:',
            'password': 'Contraseña: '
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Ej. Francisco'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Ej. Sánchez'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Ej. email@exaple.com'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Ej. ****************'
            }),
        }
