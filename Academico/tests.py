# python
from django.test import TestCase
from django.apps import apps

class AcademicoTests(TestCase):
    def test_app_installed(self):
        # Cambia 'Academico' por 'academico' si ese es el app label real
        app_config = apps.get_app_config('Academico')
        self.assertIsNotNone(app_config)

    def test_root_no_server_error(self):
        response = self.client.get('/')
        self.assertLess(response.status_code, 500)
