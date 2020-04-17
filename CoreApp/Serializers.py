from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import *


class ColaboradorSerializer(ModelSerializer):
    class Meta:
        model = Colaborador
        fields = '__all__'


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
