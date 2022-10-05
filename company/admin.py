from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'owner', 'created', 'updated']
    search_fields = ['name', 'owner']
    list_filter = ['created', 'updated']
