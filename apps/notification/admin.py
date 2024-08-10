from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user_id', 'type', 'date')
    search_fields = ('title', 'user_id')
    list_filter = ('type', 'date')
