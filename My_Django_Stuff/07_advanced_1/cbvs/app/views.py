from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.

"""
def inicio(request):
    return render(request,"inicio.html")
"""

class CBVview(View):
    def get(self,request):
        return HttpResponse("Class Based Views... a ver si entiendo")
