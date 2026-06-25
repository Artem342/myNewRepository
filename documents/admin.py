from django.contrib import admin
from .models import AdministrativeDocument

# Register your models here.

@admin.register(AdministrativeDocument)
class AdministrativeDocumentAdmin(admin.ModelAdmin):
    pass