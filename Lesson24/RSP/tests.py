from django.test import TestCase
from faker import Faker

from models import *


class DoctorTestCase(TestCase):
    def setUp(self):
        faker = Faker(['ru_Ru'])
        t1 = Title.objects.create(title=faker.name())
        t2 = Title.objects.create(title=faker.name())
        self.dr1 = Doctor.objects.create(
            name=faker.name(),
            midlle_name=faker.name(),
            last_name=faker.name(),
        )
        self.dr1.title.add(t1)

        print(t1, t2)
        print(self.dr1.name, self.dr1.midlle_name, self.dr1.last_name)

    def test_how_many(self):
        self.assertEqual(self.dr1.title)


