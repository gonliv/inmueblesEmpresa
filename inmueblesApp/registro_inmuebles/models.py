from django.db import models

# Create your models here.

from django.db import models

class Usuario(models.Model):
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    RUT = models.CharField(max_length=12, unique=True)
    Direccion = models.CharField(max_length=255)
    Telefono = models.CharField(max_length=15)
    Correo_electronico = models.EmailField(unique=True)
    TIPO_USUARIO_CHOICES = (
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador'),
    )
    Tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)

    def __str__(self):
        return f"{self.Nombres} {self.Apellidos}"

class Inmueble(models.Model):
    Nombre = models.CharField(max_length=255)
    Descripcion = models.TextField()
    M2_construidos = models.FloatField()
    M2_totales = models.FloatField()
    Cantidad_estacionamientos = models.IntegerField()
    Cantidad_habitaciones = models.IntegerField()
    Cantidad_banos = models.IntegerField()
    Direccion = models.CharField(max_length=255)
    Comuna = models.CharField(max_length=100)
    TIPO_INMUEBLE_CHOICES = (
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('parcela', 'Parcela'),
    )
    Tipo_inmueble = models.CharField(max_length=20, choices=TIPO_INMUEBLE_CHOICES)
    Precio_mensual_arriendo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.Nombre