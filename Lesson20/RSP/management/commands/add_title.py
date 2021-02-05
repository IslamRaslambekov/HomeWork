from django.core.management.base import BaseCommand
from RSP.models import Title


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(f"Добавлено: {Title.objects.create(title='Врач эндокринолог')}")
