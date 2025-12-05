from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify


class CategoriaOportunidade(models.TextChoices):
    EQUIPE = "EQUIPE", "Equipe de competição"
    ESTAGIO = "ESTAGIO", "Programa de estágio / inovação"
    DIRETORIO = "DIRETORIO", "Diretório / Centro Acadêmico"
    ENTIDADE = "ENTIDADE", "Entidade estudantil"
    INICIACAO = "INICIACAO", "Iniciação científica / pesquisa"


class Oportunidade(models.Model):
    """
    Modelo genérico que representa:
    - Equipes de competição
    - Estágios / Programas
    - Diretórios / Centros Acadêmicos
    - Entidades estudantis
    - Iniciação científica / pesquisa
    """

    categoria = models.CharField(
        max_length=20,
        choices=CategoriaOportunidade.choices,
    )

    # Campos principais (comuns a todos)
    nome = models.CharField(max_length=150)
    slug = models.SlugField(max_length=160, unique=True)

    # Imagens (equivalentes a img / img2)
    imagem = models.ImageField(
        upload_to="oportunidades/",
        blank=True,
        null=True,
        help_text="Imagem principal (ex: rio.jpg)",
    )
    imagem_mini = models.ImageField(
        upload_to="oportunidades/minis/",
        blank=True,
        null=True,
        help_text="Miniatura (ex: riobotz-mini.png)",
    )

    # Texto longo, equivalente a 'descricao'
    descricao = models.TextField()
    texto_lateral = models.TextField(
    blank=True,
    help_text="Texto opcional exibido ao lado da imagem no detalhe (substitui o Lorem Ipsum)."
)


    # Campos opcionais, usados só em algumas categorias
    tipo = models.CharField(
        max_length=100,
        blank=True,
        help_text="Opcional: usado para Diretório, Entidade, etc.",
    )
    topicos_lista = models.TextField(
        blank=True,
        help_text="HTML opcional com lista de tópicos (ul/li) para estágios, iniciação, etc.",
    )

    # Para destacar na home, se você quiser ligar isso aos 'destaques'
    destaque_home = models.BooleanField(
        default=False,
        help_text="Marque para aparecer na seção de destaques da home.",
    )

    # Campo de resumo para a página principal (nome + pequeno texto)
    resumo = models.CharField(
        max_length=255,
        blank=True,
        help_text="Texto curto para aparecer na lista geral (opcional).",
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        # Gera slug automaticamente se não houver
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    @property
    def categoria_label(self):
        """Equivalente ao 'categoria_label' que você passava no contexto."""
        return self.get_categoria_display()


class Tag(models.Model):
    """
    Equivalente ao dicionário:
    {"nome": "combate", "cor": "orange"}
    ligado a uma Oportunidade.
    """

    oportunidade = models.ForeignKey(
        Oportunidade,
        related_name="tags",
        on_delete=models.CASCADE,
    )
    nome = models.CharField(max_length=50)
    cor = models.CharField(
        max_length=30,
        help_text="Classe de cor (ex: 'orange', 'blue', 'green').",
    )

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return f"{self.nome} ({self.cor})"


class Contato(models.Model):
    """
    Equivalente ao dicionário:
    {"icone": "alternate_email", "texto": "@riorobotz"}
    ligado a uma Oportunidade.
    """

    oportunidade = models.ForeignKey(
        Oportunidade,
        related_name="contatos",
        on_delete=models.CASCADE,
    )
    icone = models.CharField(
        max_length=50,
        help_text="Nome do ícone (ex: 'alternate_email', 'mail', 'person').",
    )
    texto = models.CharField(
        max_length=150,
        help_text="Texto de contato (ex: @riorobotz, email, nome da pessoa).",
    )

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def __str__(self):
        return f"{self.icone}: {self.texto}"
