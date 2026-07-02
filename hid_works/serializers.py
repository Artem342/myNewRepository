from rest_framework.serializers import ModelSerializer
from .models import HidWork, WorkingDocumentation, HidWorkMaterial


class HidWorkSerialazer(ModelSerializer):
    class Meta:
        #fields = "__all__"
        exclude = ["slug"]
        model = HidWork


class HidWorkMaterialSerialazer(ModelSerializer):
    class Meta:
        fields = "__all__"
        #exclude = ["slug"]
        model = HidWorkMaterial