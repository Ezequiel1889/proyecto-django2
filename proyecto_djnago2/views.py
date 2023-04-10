from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def mi_vista(request):
    return HttpResponse("<h1> Mi primera vista </h1>")


def mostrar_fecha(request):
    return HttpResponse(f"<p> {datetime.now()} </p>")

def saludar(request, nombre, apellido):
    return HttpResponse(f"<h1> Hola {nombre} {apellido}</h1>")


def mi_primer_template(request):
    
    archivo = open(r"C:\Users\ezequ\OneDrive\Escritorio\Programacion\proyectos\proyecto-django2\templates\mi_primer_template.html", "r")
    
    template = Template(archivo.read())
    
    archivo.close()
    
    contexto = Context()
    
    temple_renderizado = template.render(contexto)
    
    return HttpResponse(temple_renderizado)
