from django.urls import path
from .views import InsuranceListView, InsuranceAddView, InsuranceEditView, InsuranceDeleteView

urlpatterns = [
    path('insurance_add/', InsuranceAddView.as_view(), name="insurance_add"),
    path('insurance_list/', InsuranceListView.as_view(), name="insurance_list"),
    path('insurance_edit/', InsuranceEditView.as_view(), name="insurance_edit"),
    path('insurance_delete/', InsuranceDeleteView.as_view(), name="insurance_delete"),
]
