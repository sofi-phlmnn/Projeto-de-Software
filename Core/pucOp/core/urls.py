from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),

    # NOVO: página de perfil
    path("perfil/", views.perfil_aluno, name="perfil"),

    # Equipes
    path("equipes/", views.equipes, name="equipes"),
    path("equipes/<int:id>/", views.equipe_detalhe, name="equipe_detalhe"),

    # Mapa
    path("mapa/", views.mapa, name="mapa"),

    # Sobre
    path("sobre/", views.sobre, name="sobre"),

    # Diretórios
    path("diretorios/", views.diretorios, name="diretorios"),
    path("diretorios/<int:id>/", views.diretorio_detalhe, name="diretorio_detalhe"),

    # Iniciação científica
    path("iniciacao/", views.iniciacao, name="iniciacao"),
    path("iniciacao/<int:id>/", views.iniciacao_detalhe, name="iniciacao_detalhe"),

    # Entidades
    path("entidades/", views.entidades, name="entidades"),
    path("entidades/<int:id>/", views.entidade_detalhe, name="entidade_detalhe"),

    # Estágios
    path("estagios/", views.estagios, name="estagios"),
    path("estagios/<int:id>/", views.estagio_detalhe, name="estagio_detalhe"),

#novos

    path("favoritos/", views.favoritos, name="favoritos"),
    path("favoritos/toggle/<str:tipo>/<int:item_id>/", views.toggle_favorito, name="toggle_favorito"),
]