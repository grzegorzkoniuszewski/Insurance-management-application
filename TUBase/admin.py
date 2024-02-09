from django.contrib import admin
from .models import CustomTUBase


class TUBaseAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'full_name', 'location', 'phone', 'email','id_name']
    search_fields = ['short_name', 'full_name', 'location', 'phone', 'email']


CustomTUBase._meta.verbose_name_plural = "Insurance companies"

admin.site.register(CustomTUBase, TUBaseAdmin)
