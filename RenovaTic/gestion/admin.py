from django.contrib import admin

from .models import Productos, Proveedores, Tipo_productos, Clientes

# MODELO DE VISTA
class ProveedoresAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Proveedor',          {'fields': ['nombre_proveedor', 'descripcion']}),
        ('Contacto',          {'fields': ['email', 'web']}),
    ]

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'proveedor', 'tipo', 'precio_compra', 'precio_venta', 'magen')
    list_filter = ['proveedor', 'tipo']
    search_fields = ['nombre_producto']

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'email', 'web')
    search_fields = ['nombre_cliente']

admin.site.register(Productos, ProductoAdmin)
admin.site.register(Proveedores, ProveedoresAdmin)
admin.site.register(Tipo_productos)
admin.site.register(Clientes, ClientesAdmin)


# Register your models here.
