from django.contrib import admin

from .models import Productos, Proveedores, Tipo_productos, Clientes, Renovaciones

# MODELO DE VISTA
class ProveedoresAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Proveedor',          {'fields': ['nombre_proveedor', 'descripcion']}),
        ('Contacto',          {'fields': ['email', 'web']}),
    ]

class ProductoAdmin(admin.ModelAdmin):
    #list_display = ('nombre_producto', 'proveedor', 'tipo', 'precio_compra', 'precio_venta',  'margen', "Mas25")
    list_display = ('nombre_producto', 'proveedor', 'tipo', 'precio_compra', 'precio_venta',  'margen')
    list_filter = ['proveedor', 'tipo']
    search_fields = ['nombre_producto']
    def margen(self, obj):
        return obj.precio_venta - obj.precio_compra

    #def Mas25(self, obj):
    #    return (obj.precio_venta - obj.precio_compra) >= (obj.precio_compra * 0.25)
    #Mas25.boolean = True

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'email', 'web')
    search_fields = ['nombre_cliente']

class RenovacionesAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'producto', 'fecha_inicio', 'fecha_renovacion', 'caducado')
    ordering = ("-fecha_renovacion",)
    def caducado(self, obj):
        return obj.fecha_renovacion < obj.fecha_inicio
    caducado.boolean = True

admin.site.register(Productos, ProductoAdmin)
admin.site.register(Proveedores, ProveedoresAdmin)
admin.site.register(Tipo_productos)
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Renovaciones, RenovacionesAdmin)


# Register your models here.
