from django.contrib import admin
from .models import AdministrativeDocument, ProjectDocument #, ProjectDocumentAttachment

# Register your models here.

@admin.register(AdministrativeDocument)
class AdministrativeDocumentAdmin(admin.ModelAdmin):
    pass

@admin.register(ProjectDocument)
class ProjectDocumentAdmin(admin.ModelAdmin):
    pass

# @admin.register(ProjectDocumentAttachment)
# class ProjectDocumentAttachmentAdmin(admin.ModelAdmin):
#     pass