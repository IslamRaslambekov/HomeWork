from django.conf.urls import url, include
from rest_framework import routers, serializers

from .models import Title, Doctor


class TitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.StringRelatedField(many=True)

    class Meta:
        model = Doctor
        exclude = ['image']
