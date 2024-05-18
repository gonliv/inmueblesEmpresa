import os
import django

# Configura las variables de entorno necesarias para Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inmueblesApp.settings')
django.setup()

from registro_inmuebles.models import Inmueble, Comuna

def export_inmuebles_por_comuna():
    # Abre el archivo para escribir los resultados
    with open('inmuebles_por_comuna.txt', 'w') as file:
        # Obtén todas las comunas
        comunas = Comuna.objects.all()
        for comuna in comunas:
            # Obtén los inmuebles en arriendo para la comuna actual
            inmuebles = Inmueble.objects.filter(comuna=comuna, precio_mensual_arriendo__gt=0)
            if inmuebles.exists():
                file.write(f'Comuna: {comuna.nombre}\n')
                for inmueble in inmuebles:
                    file.write(f'  Nombre: {inmueble.nombre}\n')
                    file.write(f'  Descripción: {inmueble.descripcion}\n')
                file.write('\n')  # Espacio entre comunas

if __name__ == '__main__':
    export_inmuebles_por_comuna()