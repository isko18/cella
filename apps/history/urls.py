from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HistoryViewSet, HistoryProductViewSet

router = DefaultRouter()
router.register(r'histories', HistoryViewSet)
router.register(r'history-products', HistoryProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
