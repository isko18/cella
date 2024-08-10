from django.contrib import admin
from .models import User, Employee

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'employee', 'created_date')
    search_fields = ('full_name', 'phone', 'employee__name')
    list_filter = ('created_date',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')
    search_fields = ('name', 'phone')
