from django.test import TestCase
from django.urls import reverse_lazy


class TestHealthCheckView(TestCase):
    url = reverse_lazy('healthcheck')

    def test_healthcheck(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), {'status': 'ok'})
