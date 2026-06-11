from django.contrib import admin
from .models import User, ResponsiblePersonProfile, EngineerProfile

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(ResponsiblePersonProfile)
class ResponsiblePersonProfileAdmin(admin.ModelAdmin):
    list_display = ("user_full_name", "position", "order")

    @admin.display(description="ФИО")
    def user_full_name(self, obj):
        return obj.user.get_full_name()

@admin.register(EngineerProfile)
class EngineerProfileAdmin(admin.ModelAdmin):
    list_display = ("user_full_name", "kategoriya")
    ordering = ("-created_at",)

    @admin.display(description="ФИО")
    def user_full_name(self, obj):
        return obj.user.get_full_name()