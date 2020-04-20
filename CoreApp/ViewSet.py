# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet

from .Serializers import *
from .models import *
# from .pagination import StandardPagination

class Colaborador_get_info(ViewSet):
    def list(self, request):
        queryset = Funcao.objects.all()
        serializer = SimpleFuncaoSerializer(queryset, many= True)
        return Response(serializer.data)

class ColaboradorViewSet(ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer


class DepartamentoViewSet(ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    # pagination_class = StandardPagination

class FormacaoViewSet(ModelViewSet):
    queryset = Formacao.objects.all()
    serializer_class = FormacaoSerializer


class FuncaoViewSet(ModelViewSet):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer
