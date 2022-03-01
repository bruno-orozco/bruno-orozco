from django.contrib import admin

from mensajes.models import *



class Mensajes(admin.ModelAdmin):

    list_display = (
        'nombre_contacto',
        'numero_telefonoo',
        'email',
        'mensaje',
    )

