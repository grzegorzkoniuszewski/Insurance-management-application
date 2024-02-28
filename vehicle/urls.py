from django.urls import path
from . import views

urlpatterns = [
    path('vehicle_add', views.vehicle_add, name="vehicle_add"),
    path('vehicle_list', views.vehicle_list, name="vehicle_list"),
    path('vehicle_detail', views.vehicle_detail, name="vehicle_detail"),
    path('vehicle_details_edit', views.vehicle_details_edit, name="vehicle_details_edit"),
    path('vehicle_status_add', views.vehicle_status_add, name="vehicle_status_add"),
    ]