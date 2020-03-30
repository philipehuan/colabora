from rest_framework.serializers import ModelSerializer

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
    class Meta:
        model = Funcao
        fields = '__all__'
