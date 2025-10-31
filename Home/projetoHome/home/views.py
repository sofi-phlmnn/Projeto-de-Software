from django.shortcuts import render

def home(request):
<<<<<<< Updated upstream
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

    # Oportunidades em destaque (mesmo conteúdo do seu HTML)
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
            "href": "#",
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
            "href": "#",
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
            "href": "#",
        },
    ]

    # Categorias (mantendo o <br/> onde existia)
    categorias = [
        {"class": "cat cat--orange", "label_html": "equipe", "href": "#"},
        {"class": "cat cat--blue",   "label_html": "iniciação<br/>científica", "href": "#"},
        {"class": "cat cat--yellow", "label_html": "entidades<br/>estudantis", "href": "#"},
        {"class": "cat cat--pink",   "label_html": "diretório<br/>acadêmico", "href": "#"},
        {"class": "cat cat--green",  "label_html": "estágio", "href": "#"},
    ]

    ctx = {"hero": hero, "destaques": destaques, "categorias": categorias}
    return render(request, "home.html", ctx)
=======
    return render(request, "index.html")
>>>>>>> Stashed changes
