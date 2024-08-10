from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'warehouse', 'num_amount', 'cost_price', 'sell_price', 'expiration_date')
    search_fields = ('name', 'code', 'warehouse__name')
    list_filter = ('expiration_date', 'deliver_date')
