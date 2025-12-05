from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Cria um formulário baseado no UserCreationForm padrão do Django
class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email') # Adicionando 'email' que não vem por padrão
