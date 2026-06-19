#from django.http import HttpResponse
from django.shortcuts import render
from .models import HidWork
from .forms import HidWorkForm

# Create your views here.

# def index(request):
#     return HttpResponse("Главная страница сайта")

def hid_work_list_view(request):
    hid_works = HidWork.objects.select_related('ResponsiblePersonProfile__user').filter(is_published=True)
    if request.user.is_authenticated and hasattr(request.user, "ResponsiblePersonProfile"):
        hid_works = HidWork.objects.select_related("ResponsiblePersonProfile__user")
    context = {
        "hid_works": hid_works
    }
    return render(request, "hid_work_list.html", context)

def hid_work_create_view(request):
    if request.method == "POST":
        form = HidWorkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #print(f"{form.cleaned_data['ResponsiblePersonProfile'].id}")
    else:
        form = HidWorkForm(initial={"is_published": True})
    return render(request, 'hid_work_form.html', {"form": form})