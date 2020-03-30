# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .Serializers import *
from .models import *


class ColaboradorViewSet(ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer


class DepartamentoViewSet(ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class FormacaoViewSet(ModelViewSet):
    queryset = Formacao.objects.all()
    serializer_class = FormacaoSerializer


class FuncaoViewSet(ModelViewSet):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer
