from django.contrib import admin
from django.contrib import admin
from core.models import Evento

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'date_evento', 'data_criacao', 'data_confirm', 'usuario')
    list_filter = ('titulo', 'usuario', 'date_evento',)


admin.site.register(Evento, EventoAdmin)

