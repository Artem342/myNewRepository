#from django.http import HttpResponse
from django.shortcuts import render
from .models import HidWork, WorkingDocumentation
from .forms import HidWorkForm
from django.views.generic import ListView

# Create your views here.

# def index(request):
#     return HttpResponse("Главная страница сайта")

# def hid_work_list_view(request):
#     hid_works = HidWork.objects.select_related('responsible_person_profile__user').filter(is_published=True)
#     if request.user.is_authenticated and hasattr(request.user, "responsible_person_profile"):
#         hid_works = HidWork.objects.select_related("responsible_person_profile__user")
#     context = {
#         "hid_works": hid_works
#     }
#     return render(request, "hid_work_list.html", context)


class HidWorkListView(ListView):
    model = HidWork
    template_name = "hid_work_list.html"
    context_object_name = "hid_works"

    def get_queryset(self):
        hid_works = HidWork.objects.filter(is_published=True)
        working_documentation = self.request.GET.get("working_documentation")
        
        if working_documentation:
            hid_works = hid_works.filter(working_documentation=working_documentation)
        
        return hid_works
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selected_working_documentation"] = self.request.GET.get("working_documentation","")
        context["working_documentations"] = WorkingDocumentation.objects.all()
        return context


def hid_work_create_view(request):
    if request.method == "POST":
        form = HidWorkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = HidWorkForm(initial={"is_published": True})
    return render(request, 'hid_work_form.html', {"form": form})

