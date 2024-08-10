from rest_framework import viewsets
from .models import History, HistoryProduct
from .serializers import HistorySerializer, HistoryProductSerializer

class HistoryProductViewSet(viewsets.ModelViewSet):
    queryset = HistoryProduct.objects.all()
    serializer_class = HistoryProductSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
