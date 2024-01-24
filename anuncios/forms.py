from django import forms
from .models import Pantalla
from .models import Anuncio 

from django.forms import ValidationError

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        
        for field_name in self.fields:
            field = self.fields[field_name]
            widget = field.widget
            attrs = widget.attrs
            
            if 'class' in attrs:
                attrs['class'] += ' form-control'
            else:
                attrs['class'] = 'form-control'

class PantallaForm(forms.ModelForm):
    class Meta:
        model = Pantalla
        fields = '__all__'

    # Asegúrate de incluir el atributo enctype en tu formulario
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({'accept': 'image/*'})  # Esto limita la selección a archivos de imagen



class AnuncioForm(BaseForm):
    # nombre = forms.CharField(min_length=3, max_length=50)
    # imagen = forms.ImageField(required=False, validators=[MaxSizefileValidation(max_file_size=2)])
    # precio = forms.IntegerField(min_value=1, max_value=1000)

    # def clean_nombre(self):
    #     nombre = self.cleaned_data["nombre"]
    #     existe = Producto.objects.filter(nombre__iexact=nombre).exists() 
    #     if existe:
    #         raise ValidationError("Este nombre ya existe")

    #     return nombre
    class Meta:
        model = Anuncio
        #fields = ["nombre","correo","tipo_consulta","mensaje","avisos"]
        fields = '__all__'

        # widgets = {
        #     "fecha_fabricacion": forms.SelectDateWidget(),
        #     "categoria_id" : forms.Select(attrs={'class':'form-control'}),
        #     "nombre":forms.TextInput(attrs={'class':'form-control'})  
        # }

# forms.py
from django import forms
from .models import CMSEvent

class CMSEventForm(forms.ModelForm):
    class Meta:
        model = CMSEvent
        fields = '__all__'
