# equipe/urls.py
from django.urls import path
from .views import equipe_view
urlpatterns = [ path("", equipe_view, name="equipe"), ]
