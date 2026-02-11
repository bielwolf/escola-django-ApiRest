from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer
class EstudantesTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']

    def setUp(self):
        # self.user = User.objects.create_superuser(username='admin', password='admin')
        self.user = User.objects.get(username="bielwolf")
        self.url = reverse('estudantes-list')
        self.client.force_authenticate(user=self.user)
        # self.estudante_01 = Estudante.objects.create(
        #     nome="Teste do modelo 01",
        #     email="test01@teste.com",
        #     cpf="01022214055",
        #     data_nascimento="2002-01-01",
        #     numero_telefone="98 99999-9999"
        # )
        # self.estudante_02 = Estudante.objects.create(
        #     nome="Teste do modelo 02",
        #     email="test02@teste.com",
        #     cpf="01022214056",
        #     data_nascimento="2004-01-01",
        #     numero_telefone="77 99999-9999"
        # )
        self.estudante_01 = Estudante.objects.get(pk=1)
        self.estudante_02 = Estudante.objects.get(pk=2)
        

    def test_requisicao_get_estudantes(self):
        """Testa a requisição GET para listar os estudantes."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_um_estudante(self):
        """Testa a requisição get para listar um estudante específico."""
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados = Estudante.objects.get(pk=1)
        dados_serializados = EstudanteSerializer(instance=dados).data
        self.assertEqual(response.data, dados_serializados)

    def test_requisicao_post_para_criar_estudante(self):
        """Testa a requisição POST para criar um estudante."""
        data = {
            "nome": "Teste",
            "email": "test03@teste.com",
            "cpf": "57416249015",
            "data_nascimento": "2003-01-01",
            "numero_telefone": "88 99999-9999"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_requisicao_put_para_atualizar_estudante(self):
        """Testa a requisição PUT para atualizar um estudante."""
        dados = {
            "nome": "Novo",
            "email": "novo@teste.com",
            "cpf": "01022214055",
            "data_nascimento": "2002-01-02",
            "numero_telefone": "98 99999-9991"
        }
        response = self.client.put(self.url+'1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_delete_para_deletar_estudante(self):
        """Testa a requisição DELETE para deletar um estudante."""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    