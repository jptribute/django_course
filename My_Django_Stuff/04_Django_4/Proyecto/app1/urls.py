from django.conf.urls import url
from . import views

#Eso es para TEMPLATE TAGGING

app_name = "app1_html_link"

urlpatterns = [
    url (r"^relative/$", views.relative, name = "nombre_relative"),
    url (r"^other/$", views.other, name = "nombre_other")

]

"""
Los "name" que le doy a cada url son para que el html los detecte
"""
