
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from AuthApp.views import GetUserView
from CoreApp.ViewSet import ColaboradorViewSet
from CoreApp.ViewSet import DepartamentoViewSet
from CoreApp.ViewSet import FormacaoViewSet
from CoreApp.ViewSet import FuncaoViewSet


router = DefaultRouter(trailing_slash=False)
router.register('colabora/coreapp/colaborador', ColaboradorViewSet)
router.register('colabora/coreapp/departamento',DepartamentoViewSet)
router.register('colabora/coreapp/formacao', FormacaoViewSet)
router.register('colabora/coreapp/funcao', FuncaoViewSet)
router.register('colabora/authapp/getuser', GetUserView, basename='user')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('colabora/authapp/api-token-auth', obtain_auth_token)
]
