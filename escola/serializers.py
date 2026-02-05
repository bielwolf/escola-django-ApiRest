from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import validate_cpf, validate_nome, validate_numero_telefone

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'numero_telefone']
    
    def validate(self, data):
        if validate_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf': 'CPF deve conter exatamente 11 dígitos numéricos.'})        
        if validate_nome(data['nome']):
            raise serializers.ValidationError({'nome': 'Nome deve conter apenas letras'})
        if validate_numero_telefone(data['numero_telefone']):
            raise serializers.ValidationError({'numero_telefone': 'Número de telefone deve conter no mínimo 13 caracteres.'})
        return data

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
        
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']