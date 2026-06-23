from django.urls import path

from .views import hid_work_create_view, HidWorkListView #, hid_work_list_view


urlpatterns = [
    #path('', hid_work_list_view, name="home"),
    path('', HidWorkListView.as_view(), name="home"),
    path('hid_works/create', hid_work_create_view, name="hid_work-create")

]