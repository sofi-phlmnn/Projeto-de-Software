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
        "link": ("https://www.google.com/maps/place/Pontif%C3%ADcia+Universidade+Cat%C3%B3lica+do+Rio+de+Janeiro"
                 "+(PUC-Rio)/@-22.9786329,-43.2340871,595m/data=!3m1!1e3!4m6!3m5!1s0x9bd5ca02b99d7b:0xf49ca71057d61fe8"
                 "!8m2!3d-22.9797463!4d-43.233402"),
        # use a imagem que preferir; se tiver uma local, troque por {% static 'img/mapa.png' %}
        "img": "https://lh3.googleusercontent.com/proxy/U810NOH9OcZkdWEJ0f48RumYHPXAcDZFnfIcTGyq367GDPi-55Wd66e1UEcx_QB9ZACBgvIj_2pGYv4F2ciUThx9v1hvfbhij51V6BzY8aWGDTMkOv655mdmzlzoKKOtewURHyCWUu9MzKIfgS-JqBJshDIrwf8FMGq2E0LkwFT28fNXQKTmpYvV1g",
        "alt": "Mapa do campus da PUC-Rio com pontos de interesse.",
    }

    # Blocos da coluna direita
    paines = [
        {
            "title": "Equipes de Competição",
            "color": "orange",
            "itens": ["Rio Robots", "Pegasus", "…", "Baja"],
        },
        {
            "title": "Projetos de Inovação",
            "color": "green",
            "itens": ["Apple Acadêmico", "Twist", "…", "Incubadora Gênesis"],
        },
        {
            "title": "Estágio interno",
            "color": "pink",
            "itens": ["ECOOA", "Empresa Júnior", "…", "AIChE"],
        },
        {
            "title": "Locais para alimentação",
            "color": "blue",
            "itens": ["LeMax", "Rei do Mate", "…", "Mega Mate"],
        },
        {
            "title": "Secretárias",
            "color": "green",
            "itens": ["Psicologia", "Economia", "…", "Ciência da Computação"],
        },
    ]

    ctx = {"hero": hero, "mapa": mapa, "paines": paines}
    return render(request, "mapa.html", ctx)
