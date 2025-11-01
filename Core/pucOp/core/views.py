from django.shortcuts import render

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

    categorias = [
        {"class": "cat cat--orange", "label_html": "equipe", "href": "#"},
        {"class": "cat cat--blue",   "label_html": "iniciação<br/>científica", "href": "#"},
        {"class": "cat cat--yellow", "label_html": "entidades<br/>estudantis", "href": "#"},
        {"class": "cat cat--pink",   "label_html": "diretório<br/>acadêmico", "href": "#"},
        {"class": "cat cat--green",  "label_html": "estágio", "href": "#"},
    ]

    ctx = {"hero": hero, "destaques": destaques, "categorias": categorias}
    return render(request, "home.html", ctx)


def equipe_view(request):
    equipes = [
        {
            "nome": "RIOROBOTZ",
            "img": "rio.jpg",
            "descricao": (
                "A RioBotz é a equipe de competições robóticas da PUC-Rio, que visa projetar, "
                "otimizar e construir robôs de combate, humanoides, de sumô, e para diversas outras categorias. "
                "A RioBotz é uma referência mundial de inovação em Robótica, permitindo aos alunos desenvolverem "
                "capacidades não apenas em engenharia mas também em liderança, organização, comunicação, gestão e trabalho em equipe."
            ),
        },
        {
            "nome": "PEGASUS",
            "img": "pegasus.png",
            "descricao": (
                "A equipe PEGASUS é responsável por desenvolver carros de corrida no estilo Fórmula SAE, "
                "desde o projeto até a competição. Com um ambiente plural e inclusivo, reunimos estudantes de diferentes áreas, "
                "promovendo a troca de ideias e inovação. Divididos em dois núcleos — Projeto e Comercial — organizamos esforços em sete setores especializados. "
                "Nosso objetivo é aprimorar conhecimentos e alcançar a excelência na competição, aplicando na prática o que aprendemos em sala de aula."
            ),
        },
        {
            "nome": "AERORIO",
            "img": "aero.jpg",
            "descricao": (
                "A AeroRio é uma equipe de desenvolvimento e construção de aeronaves não tripuladas, como drones e aviões de asa fixa. "
                "O grupo busca constantemente novos conhecimentos e desafios, participando de competições nacionais e internacionais, "
                "bem como atuando no desenvolvimento de projetos de pesquisa. A equipe é composta por alunos de diversas Engenharias, "
                "integrando teoria e prática com foco em multidisciplinaridade, trabalho em equipe, proatividade e organização."
            ),
        },
        {
            "nome": "REPTILES BAJA",
            "img": "reptiles.png",
            "descricao": (
                "A equipe Reptiles Baja PUC-Rio constrói um veículo off-road, desde o projeto até a manufatura, "
                "para participar de competições organizadas pela SAE-Brasil. Além da aplicação prática dos conteúdos de sala, "
                "estimula habilidades como liderança, proatividade, organização, respeito e disciplina."
            ),
        },
    ]
    return render(request, "equipe.html", {"equipes": equipes})


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


def sobre_view(request):
    integrantes = [
        {
            "nome": "Maria Eduarda Dantas Avila",
            "foto": "duda.png",
            "bio": "Aluno(a) da ENG4021. Interesses: design, front-end e UX.",
            "links": {
                "insta": "https://instagram.com/SEU_USUARIO",
                "git": "https://github.com/SEU_USUARIO",
                "linkedin": "https://www.linkedin.com/in/SEU_USUARIO/"
            }
        },
        {
            "nome": "Gustavo",
            "foto": "gustavo.png",
            "bio": "Apaixonado por robótica e sistemas embarcados.",
            "links": {
                "insta": "",
                "git": "https://github.com/SEU_USUARIO",
                "linkedin": ""
            }
        },
        {
            "nome": "Eduardo",
            "foto": "eduardo.png",
            "bio": "Foco em back-end, APIs e dados.",
            "links": {
                "insta": "",
                "git": "",
                "linkedin": ""
            }
        },
        {
            "nome": "Felipe",
            "foto": "felipe.png",
            "bio": "Entusiasta de IA aplicada e ciência de dados.",
            "links": {
                "insta": "",
                "git": "",
                "linkedin": ""
            }
        },
        {
            "nome": "Sofia",
            "foto": "sofia.png",
            "bio": "Interesses em produto, pesquisa e UX writing.",
            "links": {
                "insta": "",
                "git": "",
                "linkedin": ""
            }
        },
    ]
    return render(request, "sobre.html", {"integrantes": integrantes})
