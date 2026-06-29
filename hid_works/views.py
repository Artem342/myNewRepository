#from django.http import HttpResponse
from django.shortcuts import render
from .models import HidWork, WorkingDocumentation
from .forms import HidWorkForm
from django.views.generic import ListView, DeleteView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.http import JsonResponse

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


class HidWorkListFetchView(TemplateView):
    template_name = "hid_work_list_fetch.html"

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


class HidWorkListJSONView(ListView):
    model = HidWork

    def get_queryset(self):
        hid_works = HidWork.objects.filter(is_published=True)
        working_documentation = self.request.GET.get("working_documentation")
        
        if working_documentation:
            hid_works = hid_works.filter(working_documentation=working_documentation)
        return hid_works

    def render_to_response(self, context, **response_kwargs):
        hid_works= context["object_list"]
        data = []

        for hid_work in hid_works:
            data.append(
                {
                    "id": hid_work.id,
                    "title": hid_work.title,
                    "slug": hid_work.slug,
                    "working_documentation": hid_work.working_documentation.designation,
                    "responsible_person_profile": hid_work.responsible_person_profile.user.last_name,
                    "start_date": hid_work.start_date,
                    "finish_date": hid_work.finish_date,
                }
            )
        return JsonResponse(data, safe=False)


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

class HidWorkDetailView(DeleteView):
    model = HidWork
    template_name = "hid_work_detail.html"
    context_object_name = "hid_work" 
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return HidWork.objects.filter(is_published=True)
    
# def hid_work_create_view(request):
#     if request.method == "POST":
#         form = HidWorkForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#     else:
#         form = HidWorkForm(initial={"is_published": True})
#     return render(request, 'hid_work_form.html', {"form": form})

class HidWorkCreateView(CreateView):
    model = HidWork
    form_class = HidWorkForm
    template_name = "hid_work_form.html"
    success_url = reverse_lazy("home")