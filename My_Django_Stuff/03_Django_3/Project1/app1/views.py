from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def index (request):
    dicci = {"link_html_views" : "Este es el value del diccionario que es el link entre views y el html"}
    return render (request, "app1/index.html", context = dicci)

def app1_view (request):
    return HttpResponse ("buena la app")

def form1_view (request):
    form = forms.Form1()

    if request.method == "POST":
        form = forms.Form1(request.POST)
        if form.is_valid():
            #El codigo para hacer algo
            print ("validacion de datos exitosa prros!")
            print ("NOMBRE: " + form.cleaned_data["name"] )
            print ("CORREO: " + form.cleaned_data["email"] )
            print ("TEXTO: " + form.cleaned_data["text"] )

    return render (request, "app1/form1_page.html", {"form_link":form})
