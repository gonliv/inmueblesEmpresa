from django.contrib import admin
from .models import Comuna, Region, Usuario, Inmueble, SolicitudArriendo
from .models import ContactForm

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Inmueble)
admin.site.register(SolicitudArriendo)
admin.site.register(Region)
admin.site.register(Comuna)

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'message')
    search_fields = ('customer_name', 'customer_email')
    readonly_fields = ('contact_form_uuid',)
