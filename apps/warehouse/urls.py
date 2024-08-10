from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WarehouseViewSet, PermissionViewSet

router = DefaultRouter()
router.register(r'warehouses', WarehouseViewSet)
router.register(r'permissions', PermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
