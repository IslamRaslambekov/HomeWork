from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Title, Doctor
from .serializer import TitleSerializer, DoctorSerializer
from .permissions import ReadOnly


class TitleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = Doctor.objects.prefetch_related('title')
    serializer_class = DoctorSerializer
