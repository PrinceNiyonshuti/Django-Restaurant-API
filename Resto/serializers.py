from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import District, Sector, Restaurant

class DistrictSerializer(serializers.ModelSerializer):
    Sectors = serializers.StringRelatedField(many=True)
    class Meta:
        model = District
        fields = ['name','Sectors']
        
class SectorSerializer(serializers.ModelSerializer):
    Restaurants = serializers.StringRelatedField(many=True)
    class Meta:
        model = Sector
        fields = ['name','Restaurants']

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
