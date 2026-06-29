from django.urls import path

from .views import HidWorkListView, HidWorkDetailView, HidWorkCreateView, HidWorkListJSONView, HidWorkListFetchView #id_work_create_view


urlpatterns = [
    #path('', hid_work_list_view, name="home"),
    #path('hid_works/create', hid_work_create_view, name="hid_work-create")
    path('', HidWorkListView.as_view(), name="home"),
    path('hid_works/create/', HidWorkCreateView.as_view(), name="hid_work-create"),
    path('hid_works/hid_work-json/', HidWorkListJSONView.as_view(), name="hid_work-json"),
    path('hid_works/hid_works-fetch/', HidWorkListFetchView.as_view(), name="hid_work-fetch"),
    path('hid_works/<slug:slug>/', HidWorkDetailView.as_view(), name="hid_work-detail")
]