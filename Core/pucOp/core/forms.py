from django import forms
from .models import StudentProfile


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = [
            "nome",
            "curso",
            "periodo",
            "disponibilidade",
            "modalidade",
            "cr",
            "creditos_cursados",
            "creditos_totais",
            "ac_cumpridas",
            "ac_total",
        ]