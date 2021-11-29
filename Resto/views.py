from django.shortcuts import render
from .serializers import DistrictSerializer, SectorSerializer, RestaurantSerializer
from .models import District, Sector, Restaurant
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from rest_framework import generics

@api_view(['GET'])
def endPointDocumentation(request):
    routes = [
        {
            'Endpoint': '/districts/',
            'method': 'GET',
            'body': None,
            'description': 'returns array of all Districts'
        },
        {
            'Endpoint': '/district/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single District object with all methods of PUT,PATCH,DELETE'
        },
        {
            'Endpoint': '/sectors/',
            'method': 'GET',
            'body': None,
            'description': 'returns array of all Sectors'
        },
        {
            'Endpoint': '/sector/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single Sector object with all methods of PUT,PATCH,DELETE'
        },
        {
            'Endpoint': '/restaurants/',
            'method': 'GET',
            'body': None,
            'description': 'returns array of all Restaurants'
        },
        {
            'Endpoint': '/restaurant/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single Restaurant object with all methods of PUT,PATCH,DELETE'
        },
    ]
    return Response(routes)

    
class DistrictList(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class DistrictDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    
class SectorList(generics.ListCreateAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class SectorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer

class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
