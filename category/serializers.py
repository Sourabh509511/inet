from .models import category 
from rest_framework import serializers


class categorySerializer(serializers.ModelSerializer):

    class Meta:
        model=category
        fields="__all__"
