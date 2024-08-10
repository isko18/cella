from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns_swagger
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/history/', include('apps.history.urls')),
    path('api/v1/notification/', include('apps.notification.urls')),
    path('api/v1/product/', include('apps.product.urls')),
    path('api/v1/user/', include('apps.user.urls')),
    path('api/v1/warehouse/', include('apps.warehouse.urls')),
]

# Добавляем swagger URL'ы
urlpatterns += urlpatterns_swagger

# Статические и медиа файлы
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
