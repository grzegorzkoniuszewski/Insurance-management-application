from django.urls import path
from . import views

urlpatterns = [
    path('policy_add', views.policy_add, name="policy_add"),
    ]
