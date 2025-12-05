from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import Http404

from .models import Oportunidade, CategoriaOportunidade


# --------------------------------------------------------------------
# HOME
# --------------------------------------------------------------------
def home(request):
    hero = {
        "titulo": "Bem-vindo ao Portal de Oportunidades da PUC-Rio!",
        "descricao": (
            "Estamos aqui para ser sua central de informações, reunindo de forma rápida e fácil tudo sobre estágios, "
            "equipes de competição, iniciação científica, projetos de inovação e muito mais. Nosso objetivo é auxiliar você, "
            "aluno da PUC, a encontrar as melhores oportunidades para o seu desenvolvimento acadêmico e profissional. "
            "Explore e aproveite!"
        ),
        "logo_url": "https://quempuc.biobd.inf.puc-rio.br/static/images/puc-rio-logo.png",
    }

    destaques = [
        {
            "badge_class": "badge--purple",
            "icon": "school",
            "titulo": "Iniciação Científica em IA",
            "descricao": "Participe de um projeto de pesquisa inovador em Inteligência Artificial.",
            "meta": [
                {"icon": "person", "texto": "Prof. Dr. Carlos Silva"},
                {"icon": "event", "texto": "Inscrições até 30/11/2024"},
            ],
            "href": reverse("core:iniciacao"),
        },
        {
            "badge_class": "badge--green",
            "icon": "code",
            "titulo": "Estágio em Desenvolvimento Web",
            "descricao": "Vaga de estágio para desenvolvimento de aplicações web em empresa parceira.",
            "meta": [
                {"icon": "business", "texto": "Tech Solutions"},
                {"icon": "schedule", "texto": "20h semanais"},
            ],
            "href": reverse("core:estagios"),
        },
        {
            "badge_class": "badge--blue",
            "icon": "engineering",
            "titulo": "Equipe de Robótica",
            "descricao": "Faça parte da equipe de robótica da PUC-Rio e participe de competições nacionais.",
            "meta": [
                {"icon": "groups", "texto": "RioBotz"},
                {"icon": "event_available", "texto": "Reuniões semanais"},
            ],
            "href": reverse("core:equipes"),
        },
    ]

    categorias = [
        {"class": "cat cat--orange", "label_html": "equipes",                  "href": reverse("core:equipes")},
        {"class": "cat cat--blue",   "label_html": "iniciação<br/>científica", "href": reverse("core:iniciacao")},
        {"class": "cat cat--yellow", "label_html": "entidades<br/>estudantis", "href": reverse("core:entidades")},
        {"class": "cat cat--pink",   "label_html": "diretório<br/>acadêmico",  "href": reverse("core:diretorios")},
        {"class": "cat cat--green",  "label_html": "estágio",                  "href": reverse("core:estagios")},
    ]

    ctx = {
        "hero": hero,
        "destaques": destaques,
        "categorias": categorias,
    }
    return render(request, "home.html", ctx)


# --------------------------------------------------------------------
# LISTAS POR TIPO (usando models, mas mantendo os templates atuais)
# --------------------------------------------------------------------

def equipes(request):
    """Lista de equipes de competição (usa equipe.html)."""
    equipes_qs = (
        Oportunidade.objects
        .filter(categoria=CategoriaOportunidade.EQUIPE)
        .order_by("nome")
    )
    return render(request, "equipe.html", {"equipes": equipes_qs})


def diretorios(request):
    """Lista de diretórios / centros acadêmicos (diretorios.html)."""
    diretorios_qs = (
        Oportunidade.objects
        .filter(categoria=CategoriaOportunidade.DIRETORIO)
        .order_by("nome")
    )
    return render(request, "diretorios.html", {"diretorios": diretorios_qs})


def estagios(request):
    """Lista de estágios / programas (estagios.html)."""
    estagios_qs = (
        Oportunidade.objects
        .filter(categoria=CategoriaOportunidade.ESTAGIO)
        .order_by("nome")
    )
    return render(request, "estagios.html", {"estagios": estagios_qs})


def entidades(request):
    """Lista de entidades estudantis (entidades.html)."""
    entidades_qs = (
        Oportunidade.objects
        .filter(categoria=CategoriaOportunidade.ENTIDADE)
        .order_by("nome")
    )
    return render(request, "entidades.html", {"entidades": entidades_qs})


def iniciacao(request):
    """Lista de iniciação científica / pesquisa (iniciacao.html)."""
    iniciacoes_qs = (
        Oportunidade.objects
        .filter(categoria=CategoriaOportunidade.INICIACAO)
        .order_by("nome")
    )
    return render(request, "iniciacao.html", {"iniciacoes": iniciacoes_qs})


# --------------------------------------------------------------------
# DETALHE GENÉRICO (usa detalhe_oportunidade.html)
# --------------------------------------------------------------------

def oportunidade_detalhe(request, id):
    """
    Página de detalhe genérica para QUALQUER Oportunidade,
    usando o mesmo template detalhe_oportunidade.html.
    """
    oportunidade = get_object_or_404(Oportunidade, id=id)

    # Mapa de categoria -> nome da URL da lista (para o botão Voltar)
    voltar_url_name_por_categoria = {
        CategoriaOportunidade.EQUIPE: "core:equipes",
        CategoriaOportunidade.ESTAGIO: "core:estagios",
        CategoriaOportunidade.DIRETORIO: "core:diretorios",
        CategoriaOportunidade.ENTIDADE: "core:entidades",
        CategoriaOportunidade.INICIACAO: "core:iniciacao",
    }

    voltar_url_name = voltar_url_name_por_categoria.get(oportunidade.categoria)
    if not voltar_url_name:
        raise Http404("Categoria não configurada para voltar.")

    ctx = {
        "categoria_label": oportunidade.categoria_label,  # ex: "Equipe de competição"
        "objeto": oportunidade,
        "voltar_url": reverse(voltar_url_name),
    }
    return render(request, "detalhe_oportunidade.html", ctx)


# --------------------------------------------------------------------
# MAPA (mantém igual)
# --------------------------------------------------------------------

def mapa(request):
    hero = {
        "titulo": "Mapa do Campus PUC-Rio",
        "descricao": (
            "Encontre rapidamente equipes de competição, projetos de inovação, secretarias e pontos de alimentação. "
            "Clique nos itens da lista para centralizar no mapa ou clique em um ponto do mapa para abrir no Google Maps."
        ),
        "logo_url": "https://quempuc.biobd.inf.puc-rio.br/static/images/puc-rio-logo.png",
    }

    mapa_info = {
        "link": (
            "https://www.google.com/maps/place/Pontif%C3%ADcia+Universidade+Cat%C3%B3lica+do+Rio+de+Janeiro"
            "+(PUC-Rio)/@-22.9786329,-43.2340871,595m/data=!3m1!1e3!4m6!3m5!1s0x9bd5ca02b99d7b:0xf49ca71057d61fe8"
            "!8m2!3d-22.9797463!4d-43.233402"
        ),
        "alt": "Mapa do campus da PUC-Rio com pontos de interesse.",
    }

    paines = [
        {
            "title": "Equipes de Competição",
            "color": "orange",
            "itens": ["RioBotz", "Pegasus", "Reptiles Baja", "AeroRio"],
        },
        {
            "title": "Projetos de Inovação",
            "color": "green",
            "itens": ["Apple Developer Academy", "Ignição Petrobras", "I9Cultura / Tecnotopias", "ECOA PUC-Rio"],
        },
        {
            "title": "Estágio interno",
            "color": "pink",
            "itens": ["PUC Empresa Júnior", "Estágio Interno CCS", "AIChE", "PET Engenharia"],
        },
        {
            "title": "Locais para alimentação",
            "color": "blue",
            "itens": ["LeMax", "Rei do Mate", "Mega Mate", "Cantina do Frade"],
        },
        {
            "title": "Secretarias",
            "color": "green",
            "itens": ["Secretaria Psicologia", "Secretaria Economia", "Secretaria Computação", "Secretaria CCS"],
        },
    ]

    pontos = [
        {"name": "PUC-Rio (Campus)", "lat": -22.979580, "lng": -43.233480, "desc": "Entrada principal da PUC-Rio.", "tipo": "campus"},

        # Equipes de competição
        {"name": "RioBotz", "lat": -22.9800367048818, "lng": -43.23288754210833, "desc": "Laboratório RioBotz – robôs de combate.", "tipo": "equipes"},
        {"name": "Pegasus",        "lat": -22.9790798161517, "lng": -43.23316845692918, "desc": "Equipe Pegasus – Fórmula SAE.", "tipo": "equipes"},
        {"name": "Reptiles Baja",  "lat": -22.979870489298467, "lng": -43.23312574270568, "desc": "Equipe Reptiles Baja SAE.", "tipo": "equipes"},
        {"name": "AeroRio",        "lat": -22.97955124079113,  "lng": -43.23283962884005, "desc": "Equipe AeroRio – aviões e drones.", "tipo": "equipes"},

        # Projetos de inovação
        {"name": "Apple Developer Academy",      "lat": -22.97909785428375,  "lng": -43.234103295781174, "desc": "Laboratório Apple Developer Academy.", "tipo": "inovacao"},
        {"name": "Ignição Petrobras",          "lat": -22.97895148267144,  "lng": -43.23372099956563,  "desc": "Ignição Petrobras – RDC.", "tipo": "inovacao"},
        {"name": "I9Cultura / Tecnotopias",      "lat": -22.97941112975673,  "lng": -43.232963581712146, "desc": "Projetos culturais e tecnologia – ECOA.", "tipo": "inovacao"},
        {"name": "ECOA PUC-Rio",                 "lat": -22.979742197483868, "lng": -43.23285522461012,  "desc": "Instituto ECOA de inovação.", "tipo": "inovacao"},

        # Entidades / Estágio interno
        {"name": "PUC Empresa Júnior", "lat": -22.97998406374321, "lng": -43.2325942729298,  "desc": "Empresa Júnior da PUC-Rio.", "tipo": "estagio"},
        {"name": "Estágio Interno CCS","lat": -22.979952128356045,"lng": -43.23359260217461,  "desc": "Estágio interno no CCS.", "tipo": "estagio"},
        {"name": "AIChE",              "lat": -22.97950513808575, "lng": -43.23430202795027,  "desc": "Capítulo AIChE – Engenharia Química.", "tipo": "estagio"},
        {"name": "PET Engenharia",     "lat": -22.978906590831073,"lng": -43.23331988629732,  "desc": "PET Engenharia – RDC.", "tipo": "estagio"},

        # Alimentação
        {"name": "LeMax",           "lat": -22.979677465987344, "lng": -43.232373371322744, "desc": "Restaurante LeMax (CCS).", "tipo": "alimentacao"},
        {"name": "Rei do Mate",     "lat": -22.98002951410263, "lng": -43.23297164651833,  "desc": "Quiosque Rei do Mate.", "tipo": "alimentacao"},
        {"name": "Mega Mate",       "lat": -22.979894703663575, "lng": -43.232687988768255,  "desc": "Loja Mega Mate.", "tipo": "alimentacao"},
        {"name": "Cantina do Frade","lat": -22.97963015670803,  "lng": -43.23314509295869,  "desc": "Cantina do Frade – Amizade.", "tipo": "alimentacao"},

        # Secretarias
        {"name": "Secretaria Psicologia", "lat": -22.980086253214224, "lng": -43.23381240603214, "desc": "Secretaria de Psicologia.", "tipo": "secretaria"},
        {"name": "Secretaria Economia",   "lat": -22.97995410273898,  "lng": -43.23395752380477, "desc": "Secretaria de Economia.", "tipo": "secretaria"},
        {"name": "Secretaria Computação", "lat": -22.979791097741757, "lng": -43.2333960765081,  "desc": "INF – Secretaria de Computação.", "tipo": "secretaria"},
        {"name": "Secretaria CCS",        "lat": -22.979908439593603, "lng": -43.23410977859713, "desc": "Secretaria geral do CCS.", "tipo": "secretaria"},
    ]

    ctx = {
        "hero": hero,
        "mapa": mapa_info,
        "paines": paines,
        "pontos": pontos,
    }
    return render(request, "mapa.html", ctx)


# --------------------------------------------------------------------
# SOBRE
# --------------------------------------------------------------------

def sobre(request):
    return render(request, "sobre.html")
