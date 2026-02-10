from django.test import TestCase
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer

class EstudanteSerializerTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome="Teste do modelo",
            email="test@teste.com",
            cpf="01022214055",
            data_nascimento="2000-01-01",
            numero_telefone="98 99999-9999"
        )
        self.serializer_estudante = EstudanteSerializer(instance=self.estudante)

    def test_verificar_campos_estudante_serializer(self):
        """"Teste para verificar os campos do serializer do estudante"""
        data = self.serializer_estudante.data
        self.assertEqual(set(data.keys()), set(['id', 'nome', 'email', 'cpf', 'data_nascimento', 'numero_telefone']))

    def test_verificar_conteudo_estudante_serializer(self):
        """"Teste para verificar o conteúdo do serializer do estudante"""
        data = self.serializer_estudante.data
        self.assertEqual(data['nome'], "Teste do modelo")
        self.assertEqual(data['email'], "test@teste.com")
        self.assertEqual(data['cpf'], "01022214055")
        self.assertEqual(data['data_nascimento'], "2000-01-01")
        self.assertEqual(data['numero_telefone'], "98 99999-9999")