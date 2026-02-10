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
        self.assertEqual(data['nome'], self.estudante.nome)
        self.assertEqual(data['email'], self.estudante.email)
        self.assertEqual(data['cpf'], self.estudante.cpf)
        self.assertEqual(data['data_nascimento'], self.estudante.data_nascimento)
        self.assertEqual(data['numero_telefone'], self.estudante.numero_telefone)

class CursoSerializerTestCase(TestCase):
    def setUp(self):
        self.curso = Curso(
            codigo="CURSO1",
            descricao="Descrição do curso 1",
            nivel="B"
        )
        self.serializer_curso = CursoSerializer(instance=self.curso)

    def test_verificar_campos_curso_serializer(self):
        """"Teste para verificar os campos do serializer do curso"""
        data = self.serializer_curso.data
        self.assertEqual(set(data.keys()), set(['id', 'codigo', 'descricao', 'nivel']))

    def test_verificar_conteudo_curso_serializer(self):
        """"Teste para verificar o conteúdo do serializer do curso"""
        data = self.serializer_curso.data
        self.assertEqual(data['codigo'], self.curso.codigo)
        self.assertEqual(data['descricao'], self.curso.descricao)
        self.assertEqual(data['nivel'], self.curso.nivel)

class MatriculaSerializerTestCase(TestCase):
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome="Teste do modelo",
            email="test@teste.com",
            cpf="01022214055",
            data_nascimento="2000-01-01",
            numero_telefone="98 99999-9999"
        )
        self.curso_matricula = Curso.objects.create(
            codigo="CURSO1",
            descricao="Descrição do curso 1",
            nivel="B"
        )
        self.matricula = Matricula(
            estudante = self.estudante_matricula,
            curso = self.curso_matricula,
            periodo = "M"
        )
        self.serializer_matricula = MatriculaSerializer(instance=self.matricula)

    def test_verificar_campos_matricula_serializer(self):
        """"Teste para verificar os campos do serializer da matrícula"""
        data = self.serializer_matricula.data
        self.assertEqual(set(data.keys()), set(['id', 'estudante', 'curso', 'periodo']))

    def test_verificar_conteudo_matricula_serializer(self):
        """"Teste para verificar o conteúdo do serializer da matrícula"""
        data = self.serializer_matricula.data
        self.assertEqual(data['estudante'], self.matricula.estudante.id)
        self.assertEqual(data['curso'], self.matricula.curso.id)
        self.assertEqual(data['periodo'], self.matricula.periodo)
