# -*- encoding: utf-8 -*-

from django import forms
from headhunters.models import Headhunter, Vacant


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


class AddVacant(forms.ModelForm):
    class Meta:
        model = Vacant
        fields = [
            'location',
            'name',
            'salary',
            'headline',
            'details',
            'picture',
        ]

        labels = {
            'location': '¿En qué ciudad es el empleo?:',
            'name': 'Nombre de la empresa:',
            'salary': 'Salario:',
            'headline' : '¿Qué estás buscado? (Vacante)',
            'details': 'Detalles de la Vacante:',
            'picture': 'Imagen:',
        }

        widgets = {
            'location': forms.TextInput(attrs={
            }),
            'name': forms.TextInput(attrs={
            }),
            'salary': forms.TextInput(attrs={
            }),
            'headline': forms.TextInput(attrs={
            }),
            'details': forms.TextInput(attrs={
            }),
        }

