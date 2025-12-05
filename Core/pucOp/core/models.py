# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nome = models.CharField(max_length=150)
    curso = models.CharField(max_length=100)
    periodo = models.PositiveIntegerField(default=1)

    disponibilidade = models.CharField(max_length=50, blank=True)   # ex: "20-30h/sem"
    modalidade = models.CharField(max_length=50, blank=True)        # ex: "Remoto/Híbrido"

    cr = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)  # 7.9
    creditos_cursados = models.PositiveIntegerField(default=0)
    creditos_totais = models.PositiveIntegerField(default=180)

    ac_cumpridas = models.PositiveIntegerField(default=0)  # horas complementares feitas
    ac_total = models.PositiveIntegerField(default=100)    # horas necessárias

    def __str__(self):
        return f"Perfil de {self.nome} ({self.user.username})"

    @property
    def ac_percentual(self):
        if self.ac_total == 0:
            return 0
        return int(self.ac_cumpridas / self.ac_total * 100)
    
class Favorite(models.Model):
    TIPO_CHOICES = [
        ("equipe", "Equipe de competição"),
        ("estagio", "Estágio / Programa"),
        ("diretorio", "Diretório / CA"),
        ("entidade", "Entidade estudantil"),
        ("iniciacao", "Iniciação científica"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    objeto_id = models.PositiveIntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'tipo', 'objeto_id')

    def __str__(self):
        return f"{self.user.username} - {self.tipo} #{self.objeto_id}"