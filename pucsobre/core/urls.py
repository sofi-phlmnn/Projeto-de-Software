from django.urls import path
from . import views

urlpatterns = [
    path('', views.sobre_equipe, name='sobre'),
]