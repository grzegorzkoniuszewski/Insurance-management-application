from django.urls import path
from . import views

urlpatterns = [
    path('insurance_add/', views.insurance_add, name="insurance_add"),
    path('insurance_list/', views.insurance_list, name="insurance_list"),
    path('insurance_detail/<int:policy_id>/', views.insurance_detail, name="insurance_detail"),
    path('insurance_edit/<int:policy_id>/', views.insurance_edit, name="insurance_edit"), # Dodana ścieżka do widoku edycji
    # path('insurance_delete/<int:policy_id>/', views.insurance_delete, name="insurance_delete"),
]
