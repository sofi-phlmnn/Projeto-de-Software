from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("equipes/", views.equipes, name="equipes"),
    path("diretorios/", views.diretorios, name="diretorios"),
    path("iniciacao/", views.iniciacao, name="iniciacao"),
    path("entidades/", views.entidades, name="entidades"),
    path("estagios/", views.estagios, name="estagios"),

    path("perfil/", views.perfil, name="perfil"), 
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("cadastro/", views.cadastro_view, name="cadastro"),
    
    # ROTAS DE REDEFINIÇÃO DE SENHA (OK)
    path(
        'password_reset/', 
        auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), 
        name='password_reset_dev'
    ),
    path(
        'password_reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), 
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), 
        name='password_reset_confirm'
    ),
    path(
        'reset/done/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), 
        name='password_reset_complete'
    ),
    
    # Rota de Logout (OK)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    path("equipes/<int:id>/", views.oportunidade_detalhe, name="equipe_detalhe"),
    path("estagios/<int:id>/", views.oportunidade_detalhe, name="estagio_detalhe"),
    path("diretorios/<int:id>/", views.oportunidade_detalhe, name="diretorio_detalhe"),
    path("entidades/<int:id>/", views.oportunidade_detalhe, name="entidade_detalhe"),
    path("iniciacao/<int:id>/", views.oportunidade_detalhe, name="iniciacao_detalhe"),
    path("mapa/", views.mapa, name="mapa"),
    path("sobre/", views.sobre, name="sobre"),

]
