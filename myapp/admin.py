from django.contrib import admin
from .models import Category, Product, Order, User


class OrderAdmin(admin.ModelAdmin):
    """Список заказов."""
    list_display = ['customer', 'total_price', 'ordered_at']
    ordering = ['ordered_at', '-total_price']
    list_filter = ['ordered_at', 'total_price']
    """Отдельный заказ."""
    readonly_fields = ['ordered_at', 'customer']
    fieldsets = [
            (
                None,
                {
                    'classes': ['wide'],
                    'fields': ['customer'],
                },
            ),
            (
                'Заказ',
                {
                    'classes': ['collapse'],
                    'description': 'Состав заказа', 'fields': ['products'],
                },
            ),
            (
                'Стоимость и дата',
                {
                    'fields': ['total_price', 'ordered_at'],
                }
            ),
        ]

admin.site.register(Category)
admin.site.register(Order, OrderAdmin)