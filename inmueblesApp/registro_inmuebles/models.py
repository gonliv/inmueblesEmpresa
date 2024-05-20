from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class Usuario(AbstractUser):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField(unique=True)
    ARRENDATARIO = 'arrendatario'
    ARRENDADOR = 'arrendador'
    
    TIPO_USUARIO_CHOICES = [
        (ARRENDATARIO, 'Arrendatario'),
        (ARRENDADOR, 'Arrendador'),
    ]
    
    tipo_usuario = models.CharField(
        max_length=20, 
        choices=TIPO_USUARIO_CHOICES,
        default=ARRENDATARIO
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios',
        blank=True,
        help_text='Los grupos a los que pertenece el usuario.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios',
        blank=True,
        help_text='Permisos específicos para este usuario.'
    )

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Region(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Reg"
        verbose_name_plural = "Regiones"

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Inmueble(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    cantidad_estacionamientos = models.IntegerField()
    cantidad_habitaciones = models.IntegerField()
    cantidad_banos = models.IntegerField()
    direccion = models.CharField(max_length=255)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    
    CASA = 'casa'
    DEPARTAMENTO = 'departamento'
    PARCELA = 'parcela'
    
    TIPO_INMUEBLE_CHOICES = [
        (CASA, 'Casa'),
        (DEPARTAMENTO, 'Departamento'),
        (PARCELA, 'Parcela'),
    ]
    
    tipo_inmueble = models.CharField(
        max_length=20, 
        choices=TIPO_INMUEBLE_CHOICES
    )
    
    precio_mensual_arriendo = models.DecimalField(max_digits=10, decimal_places=2)
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='propiedades', default=1)

    def __str__(self):
        return self.nombre

class SolicitudArriendo(models.Model):
    arrendatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitudes')
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='solicitudes')
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('aceptado', 'Aceptado'), ('rechazado', 'Rechazado')], default='pendiente')

    def __str__(self):
        return f"Solicitud de {self.arrendatario} para {self.inmueble}"
    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    
    def __str__(self):
        return f"{self.customer_name} - {self.customer_email}"  
    
