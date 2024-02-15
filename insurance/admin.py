from django.contrib import admin
from .models import PolicyStatus, PolicyType, InsurancePolicy

admin.site.site_header = 'Insurance Management Application site administration'
admin.site.index_title = 'Insurance Management Application administration panel'
admin.site.site_title = 'Insurance Management Application - Administration panel'


# Admin class for PolicyStatus model.
@admin.register(PolicyStatus)
class PolicyStatusAdmin(admin.ModelAdmin):
    # Display the 'policy_status_name' field in the admin list view.
    list_display = ('policy_status_name',)


# Admin class for PolicyType model.
@admin.register(PolicyType)
class PolicyTypeAdmin(admin.ModelAdmin):
    # Display the 'policy_type_name' field in the admin list view.
    list_display = ('policy_type_name',)


# Admin class for InsurancePolicy model.
@admin.register(InsurancePolicy)
class InsurancePolicyAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view.
    list_display = ('policy_number', 'validity_start_date', 'validity_end_date', 'status', 'policy_type')
    # Add filters for 'status' and 'policy_type' fields.
    list_filter = ('status', 'policy_type')