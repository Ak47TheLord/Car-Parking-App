from .models import *
from rest_framework import serializers


class SlotSerializers(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = "__all__"


class UserRegisterFormSerializer(serializers.ModelSerializer):
    # email = forms.EmailField()
    class Meta:
        model = Profile
        fields = "__all__"
