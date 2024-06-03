from django.contrib import admin
from .models import Products


# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'description', 'price')


admin.site.register(Products, ProductsAdmin)
