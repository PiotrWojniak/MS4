"""Imports"""
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """Create diplay list for products in admin panel"""
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    # sorting product by SKU
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """Create display list for category in admin panel"""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
