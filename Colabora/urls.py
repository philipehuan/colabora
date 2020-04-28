
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from CoreApp.ViewSet import ColaboradorViewSet, Colaborador_get_info
from CoreApp.ViewSet import DepartamentoViewSet
from CoreApp.ViewSet import FormacaoViewSet
from CoreApp.ViewSet import FuncaoViewSet


router = DefaultRouter()
router.register('colabora/coreapp/colaborador', ColaboradorViewSet)
router.register('colabora/coreapp/departamento',DepartamentoViewSet)
router.register('colabora/coreapp/formacao', FormacaoViewSet)
router.register('colabora/coreapp/funcao', FuncaoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
