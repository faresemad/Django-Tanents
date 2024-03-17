from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from app.models import Client, Domain


@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ["name", "created_on"]


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ["domain", "tenant"]
