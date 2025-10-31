from django.db import models

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    matricula_do_aluno = models.CharField(max_length=20)

    def __str__(self):
        return f"Curso {self.id}"


class Aluno(models.Model):
    matricula = models.CharField(max_length=20, primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    periodo = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="alunos")

    def __str__(self):
        return self.nome


class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=150)
    nome_fantasia = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome_fantasia


class Vaga(models.Model):
    id = models.AutoField(primary_key=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="vagas")
    titulo = models.CharField(max_length=150)
    remuneracao = models.DecimalField(max_digits=10, decimal_places=2)
    carga_horaria = models.CharField(max_length=50)
    modalidade = models.CharField(max_length=50)
    localizacao = models.CharField(max_length=100)
    prazo = models.DateField()

    def __str__(self):
        return self.titulo


class Candidatura(models.Model):
    id = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="candidaturas")
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE, related_name="candidaturas")
    data = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.aluno.nome} - {self.vaga.titulo}"