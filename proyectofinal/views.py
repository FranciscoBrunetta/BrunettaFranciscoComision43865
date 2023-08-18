from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from aplicacion.models import Vino

def saludo(request):
    return HttpResponse("Hola Mundo!!!")

def bienvenido(request):
    return HttpResponse("<html><h1>Bienvenidos a nuestro sitio web!</h1></html>")

def diaDeHoy(request):
    dia = datetime.datetime.now()
    respuestaDia =f"Hoy es <br> {dia}"
    return HttpResponse(respuestaDia)

def saludoPersonal(request, nombre):
    saludo =f"Bienvenido {nombre}!"
    return HttpResponse(saludo)

def pruebaTemplate(request):
    
    plantilla = loader.get_template("index.html")

    datos = {
        "nombre": "Jose Francisco",
        "apellido": "Brunetta",
        "dni": 11903000,
        "fecha_hoy": datetime.datetime.now(),
        "notas": [7,8,10,5,4,3],
    }
    documento = plantilla.render(datos)
    return HttpResponse(documento)

def ingresar_vino(request, pcategoria, puva):
    vino = Vino(categoria=pcategoria, uva=puva)
    vino.save()

    respuesta = f"El vino ingresado fue de la categoria {vino.categoria} de la uva {vino.uva}"
    return HttpResponse(respuesta)