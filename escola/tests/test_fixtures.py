from django.test import TestCase
from escola.models import Estudante, Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_carregar_fixtures(self):
        """Teste para verificar se as fixtures foram carregadas corretamente."""
        estudante = Estudante.objects.get(nome="João Felipe Peixoto")
        curso = Curso.objects.get(pk=1)

        self.assertEqual(estudante.numero_telefone, "64 97560-4872")
        self.assertEqual(curso.codigo, "POO")

    
