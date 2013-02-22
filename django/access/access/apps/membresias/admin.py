from django.contrib import admin
from access.apps.membresias.models import membresia,info_adicional,miembros_adicionales,tipo_poliza,tipo_cobertura,rel_mem,MenoresEdad

admin.site.register(membresia)
admin.site.register(info_adicional)
admin.site.register(miembros_adicionales)
admin.site.register(tipo_poliza)
admin.site.register(tipo_cobertura)
admin.site.register(rel_mem)
admin.site.register(MenoresEdad)
