from django.core.management.base import BaseCommand
from RSP.models import Title


class Command(BaseCommand):

    def handle(self, *args, **options):
        title = Title.objects.filter(id=1)
        title.delete()