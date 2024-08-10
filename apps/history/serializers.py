from rest_framework import serializers
from .models import History, HistoryProduct

class HistoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryProduct
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    products = HistoryProductSerializer(many=True, read_only=True)

    class Meta:
        model = History
        fields = '__all__'
