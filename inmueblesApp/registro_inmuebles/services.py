from .models import Usuario, Inmueble

def registrar_usuario(datos_usuario):
    nuevo_usuario = Usuario.objects.create(**datos_usuario)
    return nuevo_usuario

def actualizar_usuario(usuario_id, datos_actualizados):
    usuario = Usuario.objects.get(id=usuario_id)
    for clave, valor in datos_actualizados.items():
        setattr(usuario, clave, valor)
    usuario.save()
    return usuario

def listar_propiedades_por_comuna(comuna):
    propiedades = Inmueble.objects.filter(Comuna=comuna)
    return propiedades

def publicar_propiedad(usuario_id, datos_propiedad):
    usuario = Usuario.objects.get(id=usuario_id)
    nueva_propiedad = Inmueble.objects.create(arrendador=usuario, **datos_propiedad)
    return nueva_propiedad

def listar_propiedades_arrendador(usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    propiedades = usuario.propiedades.all()
    return propiedades

def eliminar_propiedad(propiedad_id):
    propiedad = Inmueble.objects.get(id=propiedad_id)
    propiedad.delete()

def editar_propiedad(propiedad_id, datos_actualizados):
    propiedad = Inmueble.objects.get(id=propiedad_id)
    for clave, valor in datos_actualizados.items():
        setattr(propiedad, clave, valor)
    propiedad.save()
    return propiedad

def generar_solicitud_arriendo(usuario_id, propiedad_id):
    # Generar una solicitud de arriendo a una propiedad
    usuario = Usuario.objects.get(id=usuario_id)
    propiedad = Inmueble.objects.get(id=propiedad_id)
    pass

def aceptar_arrendatario(propiedad_id, solicitud_id):
    pass