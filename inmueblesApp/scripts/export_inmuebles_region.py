import os
import django

# Configura las variables de entorno necesarias para Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inmueblesApp.settings')
django.setup()

from registro_inmuebles.models import Inmueble, Comuna, Region


def export_inmuebles_por_region():
    with open('inmuebles_por_region.txt', 'w') as file:
        regiones = Region.objects.all()
        for region in regiones:
            comunas_region = Comuna.objects.filter(region=region)
            inmuebles_region = Inmueble.objects.filter(comuna__in=comunas_region, precio_mensual_arriendo__gt=0)
            if inmuebles_region.exists():
                file.write(f'Región: {region.nombre}\n')
                for inmueble in inmuebles_region:
                    file.write(f'  Nombre: {inmueble.nombre}\n')
                    file.write(f'  Descripción: {inmueble.descripcion}\n')
                file.write('\n')

if __name__ == '__main__':
    export_inmuebles_por_region()