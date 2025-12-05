from django.db import models
from django.utils.text import slugify


class CategoriaOportunidade(models.TextChoices):
    EQUIPE = "EQUIPE", "Equipe de competição"
    ESTAGIO = "ESTAGIO", "Programa de estágio / inovação"
    DIRETORIO = "DIRETORIO", "Diretório / Centro Acadêmico"
    ENTIDADE = "ENTIDADE", "Entidade estudantil"
    INICIACAO = "INICIACAO", "Iniciação científica / pesquisa"


class Oportunidade(models.Model):
    categoria = models.CharField(
        max_length=20,
        choices=CategoriaOportunidade.choices,
    )

    nome = models.CharField(max_length=150)
    slug = models.SlugField(max_length=160, unique=True)

    # 👇 ESTES SÃO OS CAMPOS QUE O SEED E OS TEMPLATES USAM
    img = models.CharField(
        max_length=200,
        blank=True,
        help_text="Nome do arquivo da imagem principal (ex: rio.jpg).",
    )
    img2 = models.CharField(
        max_length=200,
        blank=True,
        help_text="Nome do arquivo da imagem secundária (ex: riobotz-mini.png).",
    )

    descricao = models.TextField()

    resumo = models.CharField(
        max_length=255,
        blank=True,
        help_text="Texto curto para listas.",
    )

    texto_lateral = models.TextField(
        blank=True,
        help_text="Texto exibido ao lado da imagem principal no detalhe.",
    )

    tipo = models.CharField(
        max_length=100,
        blank=True,
        help_text="Opcional: tipo da oportunidade (Diretório, Empresa Júnior, etc.).",
    )

    topicos_lista = models.TextField(
        blank=True,
        help_text="HTML com lista de tópicos (ul/li) para estagios, iniciacao, etc.",
    )

    destaque_home = models.BooleanField(
        default=False,
        help_text="Marque para aparecer na seção de destaques da home.",
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    @property
    def categoria_label(self):
        return self.get_categoria_display()


class Tag(models.Model):
    oportunidade = models.ForeignKey(
        Oportunidade,
        related_name="tags",
        on_delete=models.CASCADE,
    )
    nome = models.CharField(max_length=50)
    cor = models.CharField(
        max_length=30,
        help_text="Classe de cor (ex: orange, blue, green).",
    )

    def __str__(self):
        return f"{self.nome} ({self.cor})"


class Contato(models.Model):
    oportunidade = models.ForeignKey(
        Oportunidade,
        related_name="contatos",
        on_delete=models.CASCADE,
    )
    icone = models.CharField(
        max_length=50,
        blank=True,
        help_text="Nome do ícone (ex: alternate_email, mail, person).",
    )
    texto = models.CharField(
        max_length=150,
        help_text="Texto de contato (ex: @riobotz, email, nome da pessoa).",
    )

    def __str__(self):
        return f"{self.icone}: {self.texto}"
