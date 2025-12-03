from rest_framework import serializers
from .models import Emmployer

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emmployer
        fields="__all__"