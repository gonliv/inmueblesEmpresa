from django.contrib import admin
from .models import Comuna, Region, Usuario, Inmueble, SolicitudArriendo

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Inmueble)
admin.site.register(SolicitudArriendo)
admin.site.register(Region)
admin.site.register(Comuna)
