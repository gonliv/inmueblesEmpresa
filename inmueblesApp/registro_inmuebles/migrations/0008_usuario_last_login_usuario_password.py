# Generated by Django 4.2.11 on 2024-05-20 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_inmuebles', '0007_contactform_alter_region_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=1, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
