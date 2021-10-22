from django.test import Client, TestCase


class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_status_code_main_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
