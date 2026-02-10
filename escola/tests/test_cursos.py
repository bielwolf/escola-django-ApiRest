from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso
from escola.serializers import CursoSerializer

class CursosTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('cursos-list')
        self.client.force_authenticate(user=self.user)
        self.curso_01 = Curso.objects.create(
            codigo="CURSO1",
            descricao="Descrição do curso 1",
            nivel="B"
        )
        self.curso_02 = Curso.objects.create(
            codigo="CURSO2",
            descricao="Descrição do curso 2",
            nivel="I"
        )

    def test_requisicao_get_cursos(self):
        """Testa a requisição GET para listar os cursos."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_um_curso(self):
        """Testa a requisição get para listar um curso específico."""
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados = Curso.objects.get(pk=1)
        dados_serializados = CursoSerializer(instance=dados).data
        self.assertEqual(response.data, dados_serializados)

    def test_requisicao_post_para_criar_curso(self):
        """Testa a requisição POST para criar um curso."""
        data = {
            "codigo": "CURSO3",
            "descricao": "Descrição do curso 3",
            "nivel": "B"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put_para_atualizar_curso(self):
        """Testa a requisição PUT para atualizar um curso."""
        dados =  {
            "codigo": "CURSO1",
            "descricao": "Descrição do curso 1 atualizada",
            "nivel": "I"
        }
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_delete_para_deletar_curso(self):
        """Testa a requisição DELETE para deletar um curso."""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

