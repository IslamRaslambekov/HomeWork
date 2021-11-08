from django.test import TestCase
from faker import Faker

from .models import *


class DoctorTestCase(TestCase):
    def setUp(self):
        faker = Faker(['ru_Ru'])
        t1 = Title.objects.create(title=faker.name())
        t2 = Title.objects.create(title=faker.name())
        self.dr1 = Doctor.objects.create(
            name=faker.name(),
            last_name=faker.name(),
        )
        self.dr1.title.add(t1)
        self.dr1.title.add(t2)

    def test_how_many_titles(self):
        self.assertEqual(self.dr1.get_titles_count(), 2)

    def test_title_more_than_null(self):
        self.assertTrue(self.dr1.get_more_than_null())

    def test_title_less_than_null(self):
        self.assertFalse(self.dr1.get_less_than_null())

    def test_name_is_null(self):
        self.assertFalse(self.dr1.name_is_null())

    def test_middle_name_is_null(self):
        self.assertTrue(self.dr1.middle_name_is_null())
