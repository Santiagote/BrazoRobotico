from django.http import HttpResponse
from django.shortcuts import render

from Controles.camera import grabar_objetos
from Controles.pinza import recoger_datos_objeto


def home(request):
    return render(request, 'index.html')


def controles(request):
    return render(request, 'controles.html')

def vista_grabar_objetos(request):
    grabar_objetos()
    return HttpResponse('Grabacion de Objetos iniciada')

def vista_recoger_objetos(request):
    datos= recoger_datos_objeto()
    return HttpResponse(f'Datos del objeto recogidos: {datos}')

def descripcion(request):
    return render(request, 'descripcion.html')

def registro (request):
    return render(request, 'registro.html')

def Login(request):
        return render(request,'Login.html')