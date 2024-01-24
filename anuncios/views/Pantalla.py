from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Pantalla
from ..forms import PantallaForm
from django.contrib import messages
import json
from ..models import Anuncio
# views.py
from django.shortcuts import render, redirect
from ..forms import CMSEventForm


def crear_cms_evento(request):
    if request.method == 'POST':
        cms_event_form = CMSEventForm(request.POST, request.FILES)
        if cms_event_form.is_valid():
            cms_event_form.save()
            return redirect('lista_pantallas')
    else:
        cms_event_form = CMSEventForm()

    return render(request, 'pantallas/cmsanuncio.html', {'cms_event_form': cms_event_form})

class PantallaShowView(UpdateView):
    model = Pantalla
    form_class = PantallaForm
    template_name = 'pantallas/show.html'
    success_url = reverse_lazy('lista_pantallas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for field in context['form'].fields.values():
            field.widget.attrs['disabled'] = True
        
        # Obtén los datos necesarios
        salidas_minimas = self.object.salidas_minimas_por_hora
        tiempo_cada_espacio = self.object.tiempo_cada_espacio_seg

        # Añade los datos al contexto en formato JSON
        context['data'] = json.dumps({
            'salidas_minimas': salidas_minimas,
            'tiempo_cada_espacio': tiempo_cada_espacio,
        })

        # Inicializa el formulario CMSEventForm y añádelo al contexto
        cms_event_form = CMSEventForm()
        context['cms_event_form'] = cms_event_form

        return context

class PantallaListView(ListView):
    model = Pantalla
    template_name = 'pantallas/index.html'
    context_object_name = 'pantallas'

class PantallaCreateView(CreateView):
    model = Pantalla
    form_class = PantallaForm
    template_name = 'pantallas/create.html'
    # fields = '__all__'
    success_url = reverse_lazy('lista_pantallas')

class PantallaUpdateView(UpdateView):
    model = Pantalla
    form_class = PantallaForm
    template_name = 'pantallas/edit.html'
    # fields = '__all__'
    success_url = reverse_lazy('lista_pantallas')

class PantallaShowView(UpdateView):
    model = Pantalla
    form_class = PantallaForm
    template_name = 'pantallas/show.html'
    # fields = '__all__'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for field in context['form'].fields.values():
            field.widget.attrs['disabled'] = True
        return context

    success_url = reverse_lazy('lista_pantallas')

class PantallaDeleteView(DeleteView):
    model = Pantalla
    template_name = 'pantallas/delete.html'
    success_url = reverse_lazy('lista_pantallas')

def PantallaDelete(request,id):
    pantalla = get_object_or_404(Pantalla, id=id)
    pantalla.delete()
    messages.success(request,"Pantalla eliminado correctamente")
    return redirect('lista_pantallas')
class PantallaShowView(UpdateView):
    model = Pantalla
    form_class = PantallaForm
    template_name = 'pantallas/show.html'
    success_url = reverse_lazy('lista_pantallas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for field in context['form'].fields.values():
            field.widget.attrs['disabled'] = True
        
        # Obtén los datos necesarios
        salidas_minimas = self.object.salidas_minimas_por_hora
        tiempo_cada_espacio = self.object.tiempo_cada_espacio_seg

        # Añade los datos al contexto en formato JSON
        context['data'] = json.dumps({
            'salidas_minimas': salidas_minimas,
            'tiempo_cada_espacio': tiempo_cada_espacio,
        })
        
        return context

class PantallaListView(ListView):
    model = Pantalla
    template_name = 'pantallas/index.html'
    context_object_name = 'pantallas'

class PantallaCreateView(CreateView):
    model = Pantalla
    form_class = PantallaForm
    template_name = 'pantallas/create.html'
    # fields = '__all__'
    success_url = reverse_lazy('lista_pantallas')

class PantallaUpdateView(UpdateView):
    model = Pantalla
    form_class = PantallaForm
    template_name = 'pantallas/edit.html'
    # fields = '__all__'
    success_url = reverse_lazy('lista_pantallas')

class PantallaShowView(UpdateView):
    model = Pantalla
    form_class = PantallaForm
    template_name = 'pantallas/show.html'
    success_url = reverse_lazy('lista_pantallas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Deshabilitar los campos de PantallaForm
        for field in context['form'].fields.values():
            field.widget.attrs['disabled'] = True

        # Agregar el formulario CMSEventForm al contexto
        context['formulario_evento'] = CMSEventForm()

        return context
class PantallaDeleteView(DeleteView):
    model = Pantalla
    template_name = 'pantallas/delete.html'
    success_url = reverse_lazy('lista_pantallas')

def PantallaDelete(request,id):
    pantalla = get_object_or_404(Pantalla, id=id)
    pantalla.delete()
    messages.success(request,"Pantalla eliminado correctamente")
    return redirect('lista_pantallas')