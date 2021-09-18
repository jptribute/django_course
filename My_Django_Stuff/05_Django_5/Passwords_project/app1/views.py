from django.shortcuts import render
from app1.formas import FormaUser, FormaUserInfoPerfil
#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def home (request):
    return render(request, "app1/home.html")

@login_required
def special(request):
    return HttpResponse("You're logged in, severooooo!")

@login_required
def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect(reverse("home")) #ojo con home

def register (request):
    registered = False

    if request.method == "POST":
        user_form = FormaUser (data = request.POST) #LAS FORMAS
        profile_form = FormaUserInfoPerfil (data = request.POST) #LAS FORMAS

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save (commit = False)
            profile.user = user

            if "foto_perfil" in request.FILES:
                profile.foto_perfil = request.FILES["foto_perfil"]

            profile.save()

            registered = True
        else:
            print (user_form.errors, profile_form.errors)
    else:
        user_form = FormaUser()
        profile_form = FormaUserInfoPerfil()

    return render (request, "app1/registro.html", {"user_form_link":user_form,
                                                   "profile_form_link":profile_form,
                                                   "registered_link":registered})

def login_usuario (request):
    if request.method == "POST":
        username = request.POST.get("username_h")
        password = request.POST.get("password_h")

        user = authenticate (username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))

            else:
                return HttpResponse("CUENTA INACTIVA")
        else:
            print("Alguien intento loguearse y fallo!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Detalles de login proporcionados son invalidos!")

    else:
        return render (request, "app1/login.html", {})
