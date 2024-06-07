from django.contrib import admin
from products.models import Product, Types


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'types')
    search_fields = ('name', 'description')


class TypesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Types, TypesAdmin)
