from django.urls import path
from . import views

urlpatterns = [
    path('insurance_add', views.insurance_add, name="insurance_add"),
    path('insurance_list', views.insurance_list, name="insurance_list"),
    ]
