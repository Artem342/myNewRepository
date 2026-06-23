from django import forms

from .models import HidWork

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
            "responsible_person_profile", 
            "file"
        )