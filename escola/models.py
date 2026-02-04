from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    cpf = models.CharField(max_length=11, unique=True, null=False)
    data_nascimento = models.DateField(null=False)
    numero_telefone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.nome


NIVEL = [
    ('B', 'Básico'),
    ('I', 'Intermediário'),
    ('A', 'Avançado'),
]
class Curso(models.Model):
    codigo = models.CharField(max_length=10, unique=True, null=False)
    descricao = models.TextField(null=False, blank=False)
    nivel = models.CharField(max_length=1, choices=NIVEL, null=False, default='B')

    def __str__(self):
        return self.codigo