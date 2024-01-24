# views/resumen.py
from django.shortcuts import render
from anuncios.models import Pantalla
from ..models import Anuncio

def resumen(request):
    anuncios_activos_count = Anuncio.objects.filter(listo=True).count()
    pantallas_activas = Pantalla.objects.filter(estado=True)
    pante_true = Pantalla.objects.filter(estado=True)
    pante_all = Pantalla.objects.all()
    pantalla = pante_true.first()
    salidas_minimas = pantalla.salidas_minimas_por_hora
    tiempo_cada_espacio = pantalla.tiempo_cada_espacio_seg
    context = {
        'anuncios_activos_count': anuncios_activos_count,
        'pantallas_activas': pantallas_activas,
        'pante_true': pante_true,
        'pante_all': pante_all,
        'some_variable_from_view': 'Esta es una variable desde la vista de resumen.',
        'grafica_data': {
            'salidas_minimas': salidas_minimas,
            'tiempo_cada_espacio': tiempo_cada_espacio,
        },
    }
    return render(request, 'resumen/resumen.html', context)
