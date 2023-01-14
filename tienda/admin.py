from django.contrib import admin
from .models import Categoria,Libro,Presentacion,Contacto



class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre']

class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo','categoria','paginas','precio','estado']

admin.site.register(Libro,LibroAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Presentacion)
admin.site.register(Contacto)

