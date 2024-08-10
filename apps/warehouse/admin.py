from django.contrib import admin
from .models import Warehouse, Permission

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'num_amount', 'created_date')
    search_fields = ('name', 'id')
    list_filter = ('created_date',)

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'add', 'sell', 'edit', 'see_cost_price', 'see_sell_price', 'see_amount')
    search_fields = ('employee_id',)
    list_filter = ('add', 'sell', 'edit', 'see_cost_price', 'see_sell_price', 'see_amount')
