from django.core.management.base import BaseCommand
from RSP.models import Doctor


class Command(BaseCommand):

    def handle(self, *args, **options):
        doctor = Doctor.objects.filter(id=2)
        doctor.delete()