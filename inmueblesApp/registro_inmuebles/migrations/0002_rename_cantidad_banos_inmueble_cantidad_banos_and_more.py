# Generated by Django 4.2.11 on 2024-05-17 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro_inmuebles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inmueble',
            old_name='Cantidad_banos',
            new_name='cantidad_banos',
        ),
        migrations.RenameField(
            model_name='inmueble',
            old_name='Cantidad_estacionamientos',
            new_name='cantidad_estacionamientos',
        ),
        migrations.RenameField(
            model_name='inmueble',
            old_name='Cantidad_habitaciones',
            new_name='cantidad_habitaciones',
        ),
        migrations.RenameField(
            model_name='inmueble',
            old_name='Comuna',
            new_name='comuna',
        ),
        migrations.RenameField(
            model_name='inmueble',
            old_name='Descripcion',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='inmueble',
            old_name='Direccion',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='inmueble',
            old_name='M2_construidos',
            new_name='m2_construidos',
        ),
        migrations.RenameField(
            model_name='inmueble',
            old_name='M2_totales',
            new_name='m2_totales',
        ),
        migrations.RenameField(
            model_name='inmueble',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='inmueble',
            old_name='Precio_mensual_arriendo',
            new_name='precio_mensual_arriendo',
        ),
        migrations.RenameField(
            model_name='inmueble',
            old_name='Tipo_inmueble',
            new_name='tipo_inmueble',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Apellidos',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Correo_electronico',
            new_name='correo_electronico',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Direccion',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Nombres',
            new_name='nombres',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='RUT',
            new_name='rut',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Telefono',
            new_name='telefono',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='Tipo_usuario',
        ),
        migrations.AddField(
            model_name='inmueble',
            name='propietario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='propiedades', to='registro_inmuebles.usuario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.CharField(choices=[('arrendatario', 'Arrendatario'), ('arrendador', 'Arrendador')], default='arrendatario', max_length=20),
        ),
    ]
