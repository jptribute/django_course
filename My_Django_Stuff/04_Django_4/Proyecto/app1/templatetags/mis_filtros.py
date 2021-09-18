from django import template

register = template.Library()

def corta (value,arg):
    return value.replace (arg,"")
def pone_uno (value,arg):
    return value.replace (arg,"1")

register.filter("corta_filtro", corta)
register.filter("pone_uno_filtro", pone_uno)

#o con decorator mas bonito
"""
register = template.Library()

@register.filter(name="corta_filtro")
def corta (value,arg):
    return value.replace (arg,"")
"""
