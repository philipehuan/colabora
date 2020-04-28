from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import *

class ColaboradorSerializer(ModelSerializer):
    nome_departamento = serializers.CharField(source='departamento.nomedepartamento', read_only=True)
    nome_funcao = serializers.CharField(source='funcao.nomefuncao', read_only=True)
    class Meta:
        model = Colaborador
        fields = ['id','nome', 'nascimento', 'rg', 'cpf', 'telefone', 'cnh', 'cnh_tipo','sexo', 'departamento','nome_departamento', 'funcao','nome_funcao']


class DepartamentoSerializer(ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


class FormacaoSerializer(ModelSerializer):
    class Meta:
        model = Formacao
        fields = '__all__'


class FuncaoSerializer(ModelSerializer):
    nomedepartamento = serializers.CharField(source='departamento.nomedepartamento', read_only=True)
    class Meta:
        model = Funcao
        fields = ['id', 'nomefuncao', 'departamento', 'nomedepartamento']


class SimpleFuncaoSerializer(ModelSerializer):
    nomedepartamento = serializers.CharField(source='departamento.nomedepartamento', read_only=True)
    id_departamento = serializers.IntegerField(source='departamento.id', read_only=True)

    class Meta:
        model = Funcao
        fields = ['nomefuncao', 'id_departamento','nomedepartamento']

