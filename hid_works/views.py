#from django.http import HttpResponse
from django.shortcuts import render
from .models import HidWork, WorkingDocumentation, HidWorkMaterial
from .forms import HidWorkForm
from django.views.generic import ListView, DeleteView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .serializers import HidWorkSerialazer, HidWorkMaterialSerialazer
from rest_framework.response import Response
from rest_framework.decorators import action

class HidWorkFilter(filters.FilterSet):
    search = filters.CharFilter(method="get_search2")
    
    def get_search2(self, queryset, name, value):
        if value:
            queryset = queryset.filter(
                Q(title__icontains=value) | Q(start_date__icontains=value)
            )
        return queryset

    class Meta:
        model = HidWork
        exclude = ['file',]


class HidWorkViewSet(ModelViewSet):
    queryset = HidWork.objects.all()
    serializer_class = HidWorkSerialazer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HidWorkFilter

    @action(detail=False, methods=["get"])
    def work_doc(self, request):
        working_docs = WorkingDocumentation.objects.all()
        return Response(
            [{"id": WD.id, "title": WD.title} for WD  in working_docs]
        )


class HidWorkMaterialFilter(filters.FilterSet):
    class Meta:
        model = HidWorkMaterial
        exclude = ['file',]


class HidWorkMaterialViewSet(ModelViewSet):
    queryset = HidWorkMaterial.objects.all()
    serializer_class = HidWorkMaterialSerialazer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HidWorkMaterialFilter


class HidWorkListFetchView(TemplateView):
    template_name = "hid_work_list_fetch.html"


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