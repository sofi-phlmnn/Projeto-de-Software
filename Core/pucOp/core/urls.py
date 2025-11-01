from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("equipes/", views.equipe_view, name="equipes"),
    path("mapa/", views.mapa_view, name="mapa"),
    path("sobre/", views.sobre_view, name="sobre"),
]
