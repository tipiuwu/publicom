# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Este es index en Anuncios ...")


# views.py
from django.shortcuts import render
# views.py
from django.shortcuts import render
from .models import Pantalla
# views.py

def lista_pantallas(request):
    cantidad_pantallas = Pantalla.objects.count()

    context = {
        'cantidad_pantallas': cantidad_pantallas,
    }

    return render(request, 'anuncios\templates\resumen\resumen.html', context)

def index(request):
    context = {
        'some_variable_from_view': 'Esta es una variable desde la vista de anuncios.',
    }
    return render(request, 'anuncios/anuncios_index.html', context)
