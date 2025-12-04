from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, COURSE_CHOICES, PERIOD_CHOICES # Importar Profile e Choices

# ... Sua classe RegistroForm (não alterada neste snippet) ...

# Formulário para editar os campos do Profile (Curso e Período)
class ProfileEditForm(forms.ModelForm):
    # Adicionando o widget 'gray-box' do seu CSS
    course = forms.ChoiceField(
        choices=COURSE_CHOICES,
        label="Curso",
        widget=forms.Select(attrs={'class': 'gray-box'})
    )
    period = forms.ChoiceField(
        choices=PERIOD_CHOICES,
        label="Período / Semestre",
        widget=forms.Select(attrs={'class': 'gray-box'})
    )
    
    class Meta:
        model = Profile
        fields = ['course', 'period'] # Campos que queremos editar

# Formulário para editar os campos do User (Nome e Email)
class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Nome', 
        required=False,
        widget=forms.TextInput(attrs={'class': 'gray-box', 'placeholder': 'Seu primeiro nome'})
    )
    email = forms.EmailField(
        label='E-mail',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'gray-box'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'email'] # Campos que queremos editar