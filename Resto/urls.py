from django.urls import path
from Resto import views


urlpatterns = [
    path('', views.endPointDocumentation),
    path('districts/', views.DistrictList.as_view(), name='listDistrict'),
    path('district/<int:pk>', views.DistrictDetail.as_view(), name='listDistrict'),
    path('sectors/', views.SectorList.as_view(), name='listSector'),
    path('sector/<int:pk>', views.SectorDetail.as_view(), name='sectorDetails'),
    path('restaurants/', views.RestaurantList.as_view(), name='listRestorant'),
    path('restaurant/<int:pk>', views.RestaurantDetail.as_view(), name='listRestorant'),
]
