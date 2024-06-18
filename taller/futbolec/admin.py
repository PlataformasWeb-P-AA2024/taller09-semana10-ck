from django.contrib import admin

# Importar las clases del modelo
from futbolec.models import Jugador, Equipo, Campeonato, CampeonatoEquipos
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Se crea la clase heredada de ModelResource
# con el objetivo hacer exclude  para la importación


# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Estudiante
class EquipoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # se vincula con la clase EstudianteResource
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ('nombre', 'siglas', 'twitter', 'edad')
    search_fields = ('nombre', 'siglas')
    # exclude = ("modulos",) # se excluye de la interfaz del admin

# admin.site.register se lo altera
# el primer argumento es el modelo (Estudiante)
# el segundo argumento la clase EstudianteAdmin
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador)
admin.site.register(CampeonatoEquipos)
admin.site.register(Campeonato)


