from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {"insert_me": "I'm coming from (templates/)first_app/index.html gonorrea!!", "insert_me2":"\ntest insert, esto esta en views.py"}
    return render(request, "first_app/index.html", context = my_dict)

def imagen(request):
    return render(request, "first_app/image.html")
