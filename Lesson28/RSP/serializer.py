from django.conf.urls import url, include
from rest_framework import routers, serializers

from .models import Title


class TitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'
