from django.contrib import admin
from .models import District,Sector,Restaurant,DishCategory,Dish,DishImage

# Register your models here.
admin.site.register(District)
admin.site.register(Sector)
admin.site.register(Restaurant)
admin.site.register(DishCategory)
admin.site.register(Dish)
admin.site.register(DishImage)
