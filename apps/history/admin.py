from django.contrib import admin
from .models import History, HistoryProduct

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'buyer_name', 'debt', 'debt_return_date', 'created_date')
    search_fields = ('user_id', 'buyer_name')
    list_filter = ('debt_return_date', 'created_date')

@admin.register(HistoryProduct)
class HistoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'warehouse', 'amount', 'sold_price', 'sold_currency')
    search_fields = ('name', 'code', 'warehouse__name')
