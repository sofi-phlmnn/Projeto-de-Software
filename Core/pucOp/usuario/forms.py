from django import forms
from django.contrib.auth.models import User

class CadastroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirmar senha", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username", "email", "first_name"]

    def clean_password2(self):
        p1 = self.cleaned_data.get("password")
        p2 = self.cleaned_data.get("password2")

        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("As senhas não coincidem!")

        return p2