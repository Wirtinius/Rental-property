from django.urls import path
from .views import properties, property_detail, property_search, request_visit, approve_visit_requests, approve_request, add_property
urlpatterns = [
    path("properties", properties, name="properties"),
    path('properties/<uuid:id>', property_detail, name='property_detail'),
    path('search/', property_search, name='property_search'),
    path('properties/<uuid:id>/call', request_visit, name='request_visit'),
    path('approve_visit_requests/', approve_visit_requests, name='approve_visit_requests'),
    path('approve_request/<int:request_id>/', approve_request, name='approve_request'),
    path('add_property', add_property, name='add_property'),

]