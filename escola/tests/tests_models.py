from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class EstudanteModelTestCase(TestCase):
    # def teste_falha(self):
    #     self.fail("Teste de falha intencional para verificar o framework de testes")

    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome="Teste do modelo",
            email="test@teste.com",
            cpf="01022214055",
            data_nascimento="2000-01-01",
            numero_telefone="98 99999-9999"
        )
    def test_verificar_criacao_estudante(self):
        """"Teste para verificar a criação de um estudante"""
        self.assertEqual(self.estudante.nome, "Teste do modelo")
        self.assertEqual(self.estudante.email, "test@teste.com")
        self.assertEqual(self.estudante.cpf, "01022214055")
        self.assertEqual(self.estudante.data_nascimento, "2000-01-01")
        self.assertEqual(self.estudante.numero_telefone, "98 99999-9999")

class CursoModelTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo="CURSO1",
            descricao="Descrição do curso 1",
            nivel="B"
        )
    def test_verificar_criacao_curso(self):
        """"Teste para verificar a criação de um curso"""
        self.assertEqual(self.curso.codigo, "CURSO1")
        self.assertEqual(self.curso.descricao, "Descrição do curso 1")
        self.assertEqual(self.curso.nivel, "B")

class MatriculaModelTestCase(TestCase):
    def setUp(self):
            self.estudante_matricula = Estudante.objects.create(
                nome="Teste do modelo",
                email="testemodelomatricula@test.com",
                cpf="91546870040",
                data_nascimento="2005-01-01",
                numero_telefone="87 99999-9999"
            )
            self.curso_matricula = Curso.objects.create(
                codigo="CURSO1",
                descricao="Descrição do curso 1",
                nivel="B"
            )
            self.matricula = Matricula.objects.create(
                estudante = self.estudante_matricula,
                curso = self.curso_matricula,
                periodo = "M"
            )

    def test_verificar_criacao_matricula(self):
        """"Teste para verificar a criação de uma matrícula"""
        self.assertEqual(self.matricula.estudante.nome, "Teste do modelo")
        self.assertEqual(self.matricula.curso.codigo, "CURSO1")
        self.assertEqual(self.matricula.periodo, "M")

