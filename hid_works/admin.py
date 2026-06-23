from django.contrib import admin
from .models import HidWork, HidWorkMaterial, WorkingDocumentation

# Register your models here.

class HidWorkMaterialInline(admin.TabularInline):
    model = HidWorkMaterial
    extra = 1

@admin.register(WorkingDocumentation)
class WorkingDocumentationAdmin(admin.ModelAdmin):
    list_display = ("id", "designation", "title")
    list_filter = ("designation",)
    search_fields = ("designation",)

@admin.register(HidWork)
class HidWorkAdmin(admin.ModelAdmin):
    list_display = ("id", "title") #, "slug", "working_documentation", "start_date", "finish_date", "photo", "is_published")
    list_filter = ("working_documentation", "is_published")
    search_fields =  ("title",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = (HidWorkMaterialInline, )

    # @admin.display(description="ФИО")
    # def user_full_name(self, obj):
    #     return obj.user.get_full_name()

@admin.register(HidWorkMaterial)
class HidWorkMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')