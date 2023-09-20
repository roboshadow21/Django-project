from django.contrib import admin
from .models import Category, Product, Order, User

@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['added_at', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]
    """Отдельный продукт."""
    readonly_fields = ['added_at', 'rating']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание', 'fields': ['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating', 'added_at'],
            }
        ),
    ]

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
admin.site.register(Product, ProductAdmin)