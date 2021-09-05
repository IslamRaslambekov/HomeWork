from django.core.management.base import BaseCommand
from RSP.models import Doctor, Title


class Command(BaseCommand):

    def handle(self, *args, **options):

        titles = list(Title.objects.all())

        doctor = Doctor.objects.create(name='Beniamino',
                                       middle_name='Grigorievich',
                                       last_name='Vailiev')
        doctor.title.add(titles[4])
        print(f'Добавлено: {doctor}')
