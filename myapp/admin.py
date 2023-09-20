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

class UserAdmin(admin.ModelAdmin):
    """Список заказов."""
    list_display = ['name', 'registered_at']
    ordering = ['registered_at']
    list_filter = ['registered_at', 'name']
    """Отдельный заказ."""
    readonly_fields = ['registered_at']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Контактные данные',
            {
                'classes': ['collapse'],
                'description': 'Телефон и почта', 'fields': ['phone', 'address', 'email'],
            },
        ),
        (
            'Дата регистрации',
            {
                'fields': ['registered_at'],
            }
        ),
    ]


admin.site.register(Category)
admin.site.register(Order, OrderAdmin)
admin.site.register(User, UserAdmin)