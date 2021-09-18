from django.shortcuts import render

# Create your views here.

def home (request):
    dicti = {"key1_frase":"Esta es la primera key", "key2_numero":666}
    return render (request, "app1/home.html", context = dicti)

def other (request):
    return render (request, "app1/other.html")

def relative (request):
    return render (request, "app1/relative_url_templates.html")
