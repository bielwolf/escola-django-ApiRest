from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('estudantes-list')

    def test_autenticacao_user_credenciais_validas(self):
        """Teste para autenticar um usuário com credenciais válidas."""
        user = authenticate(username='admin', password='admin')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_autenticacao_user_username_incorreto(self):
        """Teste para autenticar um username inválidos."""
        user = authenticate(username='admin123', password='admin')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_autenticacao_user_password_incorreto(self):
        """Teste para autenticar um password inválidos."""
        user = authenticate(username='admin', password='admin123')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_get_autorizada(self):
        """Teste para acessar uma rota protegida com autenticação válida."""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)