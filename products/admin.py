from django.contrib import admin
from .models import Product, Category
from reviews.models import Reviews


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
        'sku',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)