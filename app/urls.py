from django.urls import path
from .views import properties, property_detail, property_search
urlpatterns = [
    path("properties", properties, name="properties"),
    path('properties/<int:id>', property_detail, name='property_detail'),
    path('search/', property_search, name='property_search'),
]