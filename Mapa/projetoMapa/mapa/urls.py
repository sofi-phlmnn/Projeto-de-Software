from django.urls import path
from .views import mapa_view

urlpatterns = [
    path("", mapa_view, name="mapa"),
]
