from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante, Curso, Matricula
from escola.serializers import MatriculaSerializer

class MatriculasTestCase(APITestCase):
    def setUp(self):

        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('matriculas-list')
        self.client.force_authenticate(user=self.user)
        self.estudante_01 = Estudante.objects.create(
            nome="Teste do modelo 01",
            email="test01@teste.com",
            cpf="01022214055",
            data_nascimento="2002-01-01",
            numero_telefone="98 99999-9999"
        )
        self.curso_01 = Curso.objects.create(
            codigo="CURSO1",
            descricao="Descrição do curso 1",
            nivel="B"
        )
        self.matricula_01 = Matricula.objects.create(
            estudante=self.estudante_01,
            curso=self.curso_01,
            periodo="M"
        )
        self.estudante_02 = Estudante.objects.create(
            nome="Teste do modelo 02",
            email="test02@teste.com",
            cpf="01022214056",
            data_nascimento="2004-01-01",
            numero_telefone="77 99999-9999"
        )
        self.curso_02 = Curso.objects.create(
            codigo="CURSO2",
            descricao="Descrição do curso 2",
            nivel="I"
        )
        self.matricula_02 = Matricula.objects.create(
            estudante=self.estudante_02,
            curso=self.curso_02,
            periodo="M"
        )

    def test_requisicao_get_matriculas(self):
        """Testa a requisição GET para listar as matrículas."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_uma_matricula(self):
        """Testa a requisição get para listar uma matrícula específica."""
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados = Matricula.objects.get(pk=1)
        dados_serializados = MatriculaSerializer(instance=dados).data
        self.assertEqual(response.data, dados_serializados)

    def test_requisicao_post_para_criar_matricula(self):
        """Testa a requisição POST para criar uma matrícula."""
        data = {
            "estudante": self.estudante_02.id,
            "curso": self.curso_02.id,
            "periodo": "M"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put_para_atualizar_matricula(self):
        """Testa a requisição PUT para atualizar uma matrícula."""
        dados = {
            "estudante": self.estudante_01.pk,
            "curso": self.curso_02.pk,
            "periodo": "V"
        }
        response = self.client.put(self.url+'1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
       

    def test_requisicao_delete_para_nao_deletar_matricula(self):
        """Testa a requisição DELETE para não deletar uma matrícula."""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)