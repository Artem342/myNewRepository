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
            #"file"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")