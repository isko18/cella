from rest_framework import serializers
from .models import Warehouse, Permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):
    access = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Warehouse
        fields = '__all__'
