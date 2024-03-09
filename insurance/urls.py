from django.urls import path
from .views import InsuranceListView, InsuranceAddView, InsuranceEditView, InsuranceDeleteView, InsuranceDetailView

urlpatterns = [
    path('insurance_add/', InsuranceAddView.as_view(), name="insurance_add"),
    path('insurance_list/', InsuranceListView.as_view(), name="insurance_list"),
    path('insurance_edit/<int:pk>/', InsuranceEditView.as_view(), name="insurance_edit"),
    path('insurance_delete/<int:pk>/', InsuranceDeleteView.as_view(), name="insurance_delete"),
    path('insurance_detail/<int:pk>/', InsuranceDetailView.as_view(), name="insurance_detail"),

]
