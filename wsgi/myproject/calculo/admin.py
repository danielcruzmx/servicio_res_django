from django.contrib import admin
from models import Ispt, Regla, Constante

class IsptAdmin(admin.ModelAdmin):
    list_display = ('id','tipo','linferior','superior','bruto','cuota','excedente')

class ReglasAdmin(admin.ModelAdmin):
    list_display = ('id','tipo','concepto','variable','formula','descripcion','tipo_calculo')

class ConstantesAdmin(admin.ModelAdmin):
    list_display = ('id','constante','valor')


admin.site.register(Ispt, IsptAdmin)
admin.site.register(Regla, ReglasAdmin)
admin.site.register(Constante, ConstantesAdmin)