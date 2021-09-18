from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User
# Create your views here.

def index(request):
    return HttpResponse("<em>My Second Project</em>")

def help(request):
    helpdict = {'help_insert':'HELP PAGE asdasd'}
    return render(request,'apptwo/help.html',context=helpdict)

def userpage (request):
    user_list = User.objects.order_by ("last_name") #se especifica el atributo del model User, aqui "last_name"
    list_dict = {"conexion_html": user_list}
    return render(request,'appTwo/users2.html', context=list_dict)  #fijarse en las conexiones de estas 3 lineas
