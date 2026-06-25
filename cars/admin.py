from django.contrib import admin

from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'brand',
        'model',
        'year',
        'price',
        'owner',
        'is_active',
        'created_at',
    )

    search_fields = (
        'brand',
        'model',
    )

    list_filter = (
        'brand',
        'year',
        'is_active',
    )

    ordering = (
        '-created_at',
    )