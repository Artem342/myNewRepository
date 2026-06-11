from django.contrib import admin
from .models import HidWork

# Register your models here.

@admin.register(HidWork)
class HidWorkAdmin(admin.ModelAdmin):
    list_display = ("working_documentation", "hidden_work_name", "start_date", "finish_date")

    # @admin.display(description="ФИО")
    # def user_full_name(self, obj):
    #     return obj.user.get_full_name()