from django.db import models

# Create your models here.


class Pantalla(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='ruta_de_guardado/', max_length=100)
    nombre = models.CharField(max_length=200)
    estado = models.BooleanField()
    ancho_en_pixeles = models.IntegerField()
    alto_en_pixeles = models.IntegerField()

    tiempo_cada_espacio_seg = models.IntegerField()
    nro_espacios_publicitarios = models.IntegerField()
    salidas_minimas_por_hora = models.IntegerField()
    lunes = models.BooleanField()
    martes = models.BooleanField()
    miercoles = models.BooleanField()
    jueves = models.BooleanField()
    viernes = models.BooleanField()
    sabado = models.BooleanField()
    domingo = models.BooleanField()
    # porcentaje_ocupacion = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.imagen


    # def obtener_icono_ocupacion(self):
    #     # Lógica para determinar qué imagen mostrar en función del porcentaje de ocupación
    #     # Puedes personalizar esta lógica según tus necesidades
    #     if self.ocupacion >= 80:
    #         return 'url_a_imagen_80_percent.png'
    #     elif self.ocupacion >= 60:
    #         return 'url_a_imagen_60_percent.png'
    #     elif self.ocupacion >= 40:
    #         return 'url_a_imagen_40_percent.png'
    #     else:
    #         return 'url_a_imagen_menos_40_percent.png'

class Anuncio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    OPCIONES_ENUM = (
                ('Archivo','Archivo'),
                    ('Widgets','Widgets'),
                    ('Lista Inteligente','Lista Inteligente'),
                    
                )
    tipo = models.CharField(max_length=17, choices=OPCIONES_ENUM)
    # carpeta_id = models.ForeignKey(Carpeta,on_delete=models.PROTECT)
    file = models.FileField(upload_to="videos_imagenes", null=True)
    audio_en_video = models.BooleanField()
    listo = models.BooleanField()
    alta = models.DateTimeField(auto_now_add=True)  # This field will automatically be set to the current timestamp when the object is created

    def __str__(self):
        return self.nombre
    




class CMSEvent(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    file = models.FileField(upload_to='uploads', null=True)
    fecha_inicial = models.DateField(null=True, blank=True)
    fecha_final = models.DateField(null=True, blank=True)
    lunes = models.BooleanField()
    martes = models.BooleanField()
    miercoles = models.BooleanField()
    jueves = models.BooleanField()
    viernes = models.BooleanField()
    sabado = models.BooleanField()
    domingo = models.BooleanField()
    hora_inicial = models.TimeField(null=True, blank=True)
    hora_final = models.TimeField(null=True, blank=True)
    tiempo_video = models.DurationField(null=True, blank=True)
    multiplicador = models.IntegerField(null=True, blank=True)
    autoeliminacion = models.BooleanField(default=False)
    play_exclusivo = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
