from django import forms
from django.contrib.auth.models import User
from app1.models import UserInfoPerfil

class FormaUser (forms.ModelForm):
    password = forms.CharField (widget = forms.PasswordInput())

    class Meta ():
        model = User
        fields = ("username","email", "password")

class FormaUserInfoPerfil (forms.ModelForm):
    class Meta ():
        model = UserInfoPerfil #EL MODELO
        fields = ("sitio_de_portafolio", "foto_perfil")
