from django import forms
#from django.forms import inlineformset_factory
from .models import HidWork
from hidden_work.forms_utils import apply_bootstrap_classes



class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        apply_bootstrap_classes(self)


class HidWorkForm(BootstrapModelForm):
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

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     apply_bootstrap_classes(self)

        # for field in self.fields.values():
        #     if isinstance(field.widget, forms.CheckboxInput):
        #         field.widget.attrs["class"] = "form-check-input"
        #     elif isinstance(field.widget, forms.Select):
        #         field.widget.attrs["class"] = "form-select"
        #     else:
        #         field.widget.attrs["class"] = "form-control"