from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("equipes/", views.equipes, name="equipes"),
    path("equipes/<int:id>/", views.equipe_detalhe, name="equipe_detalhe"),
    path("mapa/", views.mapa, name="mapa"),
    path("sobre/", views.sobre, name="sobre"),
    path("diretorios/", views.diretorios, name="diretorios"),
    path("diretorios/<int:id>/", views.diretorio_detalhe, name="diretorio_detalhe"),
    path("iniciacao/", views.iniciacao, name="iniciacao"),
    path("iniciacao/<int:id>/", views.iniciacao_detalhe, name="iniciacao_detalhe"),
    path("entidades/", views.entidades, name="entidades"),
    path("entidades/<int:id>/", views.entidade_detalhe, name="entidade_detalhe"),
    path("estagios/", views.estagios, name="estagios"),
    path("estagios/<int:id>/", views.estagio_detalhe, name="estagio_detalhe"),
]
