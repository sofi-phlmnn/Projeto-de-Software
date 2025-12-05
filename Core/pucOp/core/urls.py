from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("equipes/", views.equipes, name="equipes"),
    path("diretorios/", views.diretorios, name="diretorios"),
    path("iniciacao/", views.iniciacao, name="iniciacao"),
    path("entidades/", views.entidades, name="entidades"),
    path("estagios/", views.estagios, name="estagios"),
    path("equipes/<int:id>/", views.oportunidade_detalhe, name="equipe_detalhe"),
    path("estagios/<int:id>/", views.oportunidade_detalhe, name="estagio_detalhe"),
    path("diretorios/<int:id>/", views.oportunidade_detalhe, name="diretorio_detalhe"),
    path("entidades/<int:id>/", views.oportunidade_detalhe, name="entidade_detalhe"),
    path("iniciacao/<int:id>/", views.oportunidade_detalhe, name="iniciacao_detalhe"),
    path("mapa/", views.mapa, name="mapa"),
    path("sobre/", views.sobre, name="sobre"),
]
