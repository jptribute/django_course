from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.

class VistaInicio(TemplateView):
    template_name = "inicio.html"

    def get_context_data(self,**kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["injectme"] = "INYECCION BASICA"
        return contexto
