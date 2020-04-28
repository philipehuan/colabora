from django.urls import path
from .ViewSet import ColaboradorSimpleView
urlpatterns = [
    path('set_colaborador_get_info/', ColaboradorSimpleView.as_view()),
]