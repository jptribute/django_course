from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return HttpResponse ("<em>Pegueloo por 2da vez</em>")

def help (request):
    helpdict = {"help_dict":"Help pageeee pegueloooo"}
    return render (request, "APPtwo/help.html", helpdict) #APPtwo not case sensitive
