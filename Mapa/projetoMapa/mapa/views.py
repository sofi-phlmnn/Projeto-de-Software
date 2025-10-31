from django.shortcuts import render

def mapa_view(request):
    hero = {
        "titulo": "Mapa do Campus PUC-Rio",
        "descricao": (
            "Encontre rapidamente equipes de competição, projetos de inovação, secretarias e pontos de alimentação. "
            "Clique no mapa para abrir no Google Maps."
        ),
        "logo_url": "https://quempuc.biobd.inf.puc-rio.br/static/images/puc-rio-logo.png",
    }

    mapa = {
        "link": (
            "https://www.google.com/maps/place/Pontif%C3%ADcia+Universidade+Cat%C3%B3lica+do+Rio+de+Janeiro"
            "+(PUC-Rio)/@-22.9786329,-43.2340871,595m/data=!3m1!1e3!4m6!3m5!1s0x9bd5ca02b99d7b:0xf49ca71057d61fe8"
            "!8m2!3d-22.9797463!4d-43.233402"
        ),
        "alt": "Mapa do campus da PUC-Rio com pontos de interesse.",
    }

    paines = [
        {"title": "Equipes de Competição",      "color": "orange", "itens": ["Rio Robots", "Pegasus", "…", "Baja"]},
        {"title": "Projetos de Inovação",       "color": "green",  "itens": ["Apple Acadêmico", "Twist", "…", "Incubadora Gênesis"]},
        {"title": "Estágio interno",            "color": "pink",   "itens": ["ECOOA", "Empresa Júnior", "…", "AIChE"]},
        {"title": "Locais para alimentação",    "color": "blue",   "itens": ["LeMax", "Rei do Mate", "…", "Mega Mate"]},
        {"title": "Secretárias",                "color": "green",  "itens": ["Psicologia", "Economia", "…", "Ciência da Computação"]},
    ]

    pontos = [
        {"name": "PUC-Rio (Gávea)", "lat": -22.97960, "lng": -43.23350, "desc": "Campus"},
        {"name": "LeMax",           "lat": -22.97905, "lng": -43.23300, "desc": "Alimentação"},
        {"name": "Secretaria CCS",  "lat": -22.97990, "lng": -43.23410, "desc": "Secretaria"},
    ]

    ctx = {"hero": hero, "mapa": mapa, "paines": paines, "pontos": pontos}
    return render(request, "mapa.html", ctx)
