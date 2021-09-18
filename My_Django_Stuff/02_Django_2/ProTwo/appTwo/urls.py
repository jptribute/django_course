from django.conf.urls import url
from appTwo import views

urlpatterns = [
    url(r'^$',views.help,name='help'),
#    url(r'^$',views.userpage,name='name userpage')  #EVIDENTEMENTE NO INTERESA ESTE ARCHIVO PARA LAS URLS
]
