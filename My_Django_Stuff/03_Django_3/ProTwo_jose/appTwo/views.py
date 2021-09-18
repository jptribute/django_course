from django.shortcuts import render
from django.http import HttpResponse
#from appTwo.models import User
from appTwo.forms import NuevoUsuarioForm
# Create your views here.

def index(request):
    return render(request,'apptwo/index.html')

def users(request):
    form = NuevoUsuarioForm()

    if request.method == "POST":
        form = NuevoUsuarioForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print ("Error en la forma")

    return render (request, "apptwo/users.html", {"form_link":form})

"""
def users(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {"users":user_list}
    return render(request,'apptwo/users.html',context=user_dict)
"""
