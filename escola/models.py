from django.db import models
from django.core.validators import MinLengthValidator

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
    codigo = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(3)], null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    nivel = models.CharField(max_length=1, choices=NIVEL, null=False, default='B', blank=False)

    def __str__(self):
        return self.codigo
    

PERIODO = [
    ('M', 'Matutino'),
    ('V', 'Vespertino'),
    ('N', 'Noturno'),
]
class Matricula(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, null=False, default='M') 