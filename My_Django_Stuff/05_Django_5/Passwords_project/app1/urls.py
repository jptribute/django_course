from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name = "app1"

urlpatterns = [
    url (r"^registro/$", views.register, name= "registro"),
    url (r"^login/$", views.login_usuario, name= "nombre_login"),

]
