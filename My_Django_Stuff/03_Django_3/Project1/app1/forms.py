from django import forms
from django.core import validators

def verifica_z (value):
    if value[0].lower() != "z":
        raise forms.ValidationError("El nombre tiene que empezar por Z perrito")

class Form1 (forms.Form):
    name = forms.CharField (validators=[verifica_z])
    email = forms.EmailField ()
    verify_email = forms.EmailField (label = "OTra vez el correo, sisas?")
    text = forms.CharField (widget = forms.Textarea)
    botcatcher = forms.CharField (required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean (self):
        todo_limpio = super().clean()
        email = todo_limpio["email"]
        vmail = todo_limpio["verify_email"]

        if email != vmail:
            raise forms.ValidationError("Los correos deben ser iguales!".upper())

"""
    def clean_botcatcher (self):
        botcatcher = self.cleaned_data["botcatcher"]
        if len(botcatcher) > 0:
            raise forms.ValidationError ("GOTCHA BOT PRRO!")
        return botcatcher
"""
