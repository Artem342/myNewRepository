from django import forms

from .models import HidWork
#from users.models import ResponsiblePersonProfile

class HidWorkForm(forms.ModelForm):
    class Meta:
        model = HidWork
        fields = (
            "title",
            "slug",
            "working_documentation",
            "start_date",
            "finish_date",
            "is_published",
            "ResponsiblePersonProfile", 
            "file"
        )
    
    # ResponsiblePersonProfile = forms.ModelChoiceField(
    #     queryset=ResponsiblePersonProfile.objects.all(),
    #     empty_label="Выберите ответственное лицо",  # <-- ТЕКСТ ПО УМОЛЧАНИЮ
    #     label="Ответственное лицо",
    #     required=True,  # <-- ОБЯЗАТЕЛЬНОЕ ПОЛЕ
    # )