from django.contrib import admin
from inmobiliaria.models import Region, Comuna,Direccion,Inmueble, Perfil


class BaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre','is_active')
    list_filter = ('is_active',)
    search_fields = ('nombre',)
    ordering = ('id',)
    class Meta:
        abstract = True

@admin.register(Perfil)
class PerfilAdmin(BaseAdmin):
    list_display_links = ('nombre',)  # Especifica qué campo será el enlace
    def nombre(self,model):
        return f'{model.usuario.first_name} {model.usuario.last_name}'



@admin.register(Comuna)
class ComunaAdmin(BaseAdmin):
    pass

@admin.register(Region)
class RegionAdmin(BaseAdmin):
    pass


@admin.register(Direccion)
class DireccionAdmin(BaseAdmin):
    list_display_links = ('nombre',)  # Especifica qué campo será el enlace

    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        return (list_display[0],'nombre','comuna',list_display[2])
    
    def nombre(self,model):
        return f'{model.calle} {model.numero}'

    nombre.short_description="Direccion"


@admin.register(Inmueble)
class Inmueble(BaseAdmin):
    list_display_links = ('nombre',)  # Especifica qué campo será el enlace
    list_filter = ('direccion','is_active')
    search_fields = ('precio', 'direccion','propietario')
    ordering = ('-id','-precio')
    list_editable = ('is_active',)
    

