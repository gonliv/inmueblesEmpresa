from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from .models import Usuario, Inmueble, SolicitudArriendo

def registrar_usuario(datos_usuario):
    try:
        nuevo_usuario = Usuario.objects.create(**datos_usuario)
        return nuevo_usuario
    except Exception as e:
        # Manejo de errores y logging si es necesario
        raise e

def actualizar_usuario(usuario_id, datos_actualizados):
    try:
        usuario = Usuario.objects.get(id=usuario_id)
        for clave, valor in datos_actualizados.items():
            setattr(usuario, clave, valor)
        usuario.save()
        return usuario
    except Usuario.DoesNotExist:
        # Manejo de error si el usuario no existe
        raise ObjectDoesNotExist(f"Usuario con id {usuario_id} no encontrado")

def listar_propiedades_por_comuna(comuna):
    propiedades = Inmueble.objects.filter(comuna=comuna)
    return propiedades

def publicar_propiedad(usuario_id, datos_propiedad):
    try:
        usuario = Usuario.objects.get(id=usuario_id)
        nueva_propiedad = Inmueble.objects.create(propietario=usuario, **datos_propiedad)
        return nueva_propiedad
    except Usuario.DoesNotExist:
        raise ObjectDoesNotExist(f"Usuario con id {usuario_id} no encontrado")

def listar_propiedades_arrendador(usuario_id):
    try:
        usuario = Usuario.objects.get(id=usuario_id)
        propiedades = usuario.propiedades.all()
        return propiedades
    except Usuario.DoesNotExist:
        raise ObjectDoesNotExist(f"Usuario con id {usuario_id} no encontrado")

def eliminar_propiedad(propiedad_id):
    try:
        propiedad = Inmueble.objects.get(id=propiedad_id)
        propiedad.delete()
    except Inmueble.DoesNotExist:
        raise ObjectDoesNotExist(f"Inmueble con id {propiedad_id} no encontrado")

def editar_propiedad(propiedad_id, datos_actualizados):
    try:
        propiedad = Inmueble.objects.get(id=propiedad_id)
        for clave, valor in datos_actualizados.items():
            setattr(propiedad, clave, valor)
        propiedad.save()
        return propiedad
    except Inmueble.DoesNotExist:
        raise ObjectDoesNotExist(f"Inmueble con id {propiedad_id} no encontrado")

def generar_solicitud_arriendo(usuario_id, propiedad_id):
    try:
        usuario = Usuario.objects.get(id=usuario_id)
        propiedad = Inmueble.objects.get(id=propiedad_id)
        solicitud = SolicitudArriendo.objects.create(arrendatario=usuario, inmueble=propiedad)
        return solicitud
    except (Usuario.DoesNotExist, Inmueble.DoesNotExist) as e:
        raise ObjectDoesNotExist(str(e))

def aceptar_arrendatario(propiedad_id, solicitud_id):
    try:
        solicitud = SolicitudArriendo.objects.get(id=solicitud_id, inmueble_id=propiedad_id)
        solicitud.estado = 'aceptado'
        solicitud.save()
        return solicitud
    except SolicitudArriendo.DoesNotExist:
        raise ObjectDoesNotExist(f"Solicitud con id {solicitud_id} para inmueble con id {propiedad_id} no encontrada")