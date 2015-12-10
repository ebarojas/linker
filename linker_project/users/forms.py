# -*- encoding: utf-8 -*-

from django import forms
from headhunters.models import Headhunter
from unemployeds.models import Unemployed

class HeadhunterProfile(forms.ModelForm):
    class Meta:
        model = Headhunter

        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'location',
            'headline',
            'picture_url'
        ]

        labels = {
            'first_name': 'Nombres:',
            'last_name': 'Apellidos:',
            'email': 'Correo electrónico:',
            'phone': 'Teléfono de contacto: ',
            'location': '¿Donde vives?: ',
            'headline': '¿A que te dedicas?',
            'picture_url': 'Foto de perfil(URL): '
        }


class UnemployedProfile(forms.ModelForm):
    class Meta:
        model = Unemployed

        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'location',
            'headline',
            'picture_url',
            'resume'
        ]

        labels = {
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'email': 'Correo electrónico',
            'phone': 'Teléfono de contacto',
            'location': '¿Donde vives?',
            'headline': '¿A que te dedicas?',
            'picture_url': 'Foto de perfil(URL)',
            'resume': 'Estracto profesional'
        }
