from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Anuncio
from ..forms import AnuncioForm
from django.contrib import messages
from django.shortcuts import render, redirect
from ..forms import AnuncioForm

def agregar_anuncio(request):
    if request.method == 'POST':
        form = AnuncioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('nombre_de_tu_vista')  # Redirecciona a la vista apropiada
    else:
        form = AnuncioForm()

    return render(request, 'tu_template.html', {'form': form})

class AnuncioListView(ListView):
    model = Anuncio
    template_name = 'anuncios/index.html'
    context_object_name = 'anuncios'

class AnuncioCreateView(CreateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'anuncios/create.html'
    # fields = '__all__'
    success_url = reverse_lazy('lista_anuncios')

class AnuncioUpdateView(UpdateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'anuncios/edit.html'
    # fields = '__all__'
    success_url = reverse_lazy('lista_anuncios')

class AnuncioShowView(UpdateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'anuncios/show.html'
    # fields = '__all__'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for field in context['form'].fields.values():
            field.widget.attrs['disabled'] = True
        return context

    success_url = reverse_lazy('lista_anuncios')

class AnuncioDeleteView(DeleteView):
    model = Anuncio
    template_name = 'anuncios/delete.html'
    success_url = reverse_lazy('lista_anuncios')

def AnuncioDelete(request,id):
    anuncio = get_object_or_404(Anuncio, id=id)
    anuncio.delete()
    messages.success(request,"Anuncio eliminado correctamente")
    return redirect('lista_anuncios')