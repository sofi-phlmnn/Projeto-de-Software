from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("equipes/", views.equipes, name="equipes"),
    path("mapa/", views.mapa, name="mapa"),
    path("sobre/", views.sobre, name="sobre"),
    path("diretorios/", views.diretorios, name="diretorios"),
    path("iniciacao/", views.iniciacao, name="iniciacao"),
    path("entidades/", views.entidades, name="entidades"),
    path("estagios/", views.estagios, name="estagios"),
    path("perfil/", views.perfil, name="perfil"),
]