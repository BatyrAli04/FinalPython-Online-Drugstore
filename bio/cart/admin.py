from django.contrib import admin

from .models import Order, ProductsInOrder


class ProductsInOrderInline(admin.TabularInline):
    model = ProductsInOrder

    verbose_name = 'Ordered goods'
    verbose_name_plural = 'Ordered goods'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ordering = ('created',)
    list_display = ('customer', 'quantity', 'created', )

    inlines = (ProductsInOrderInline,)

    def quantity(self, obj):
        return ProductsInOrder.objects.filter(order=obj).count()

    quantity.short_description = 'Number of positions'