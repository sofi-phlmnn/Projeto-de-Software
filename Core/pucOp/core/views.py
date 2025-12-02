from django.shortcuts import render
from django.urls import reverse

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




 # <-- FECHOU A LISTA AQUI
    



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
        "categorias": categorias
    }
    return render(request, "home.html", ctx)





def equipes(request):
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


def diretorios(request):
    diretorios = [
        {
            "nome": "DAAF",
            "img": "daff2.png",
            "descricao": (
                "O DAAF acolhe os alunos tanto"
                "academicamente quanto"
                " socialmente,transformando a "
                "Engenharia da PUC na melhor"
                " possível!"
            ),
        },
        {
            "nome": "DAQEQ",
            "img": "daqeq.png",
            "descricao": (
                "O Diretório Acadêmico de"
                " Química e das Engenharias" 
                "Química e de Materiais atua na"
                " luta pelos direitos dos estudantes," 
                "promove eventos acadêmicos,"
                "culturais e sociais."
            ),
        },
        {
            "nome": "CAINF",
            "img": "cainf2.png",
            "descricao": (
                "O Centro Acadêmico de"
                " Informática representa os alunos"
                " do Departamento de Informática,"
                " defendendo seus interesses e "
                "promovendo eventos"
                " de tecnologia."
            ),
        },
    ]
    return render(request, "diretorios.html", {"diretorios": diretorios})


def estagios(request):
    estagios = [
        {
            "nome": "APPLE DEVELOPER ACADEMY – PUC-RIO",
            "descricao": (
                "Programa de inovação tecnológica promovido pela PUC com apoio da Apple, focado no "
                "desenvolvimento de apps e produtos digitais."
            ),
            "topicos_lista": """
            <ul>
                <li> Programa de inovação / extensão</li>
                <li> Inscrições periódicas pelo ECOA / PUC-Rio</li>
                <li> Atuação prática com projetos, mentoria e tecnologia</li>
                <li> Inscrições periódicas pelo ECOA / PUC-Rio</li>
            </ul>
            """
        },
        {
            "nome": "PROGRAMA DE ESTÁGIO PETROBRAS",
            "descricao": "Programa de estágio nacional da Petrobras para estudantes de nível técnico ou superior.",
            "topicos_lista": """
            <ul>
                <li> Estágios para cursos técnicos ou superiores</li>
                <li> Bolsa-auxílio recente: R$ 1.825,00</li>
                <li> Carga horária típica: 20 horas semanais</li>
            </ul>
            """
        },
        {
            "nome": "IGNIÇÃO PETROBRAS / ECOA PUC-RIO",
            "descricao": (
                "Programa de inovação no mercado de óleo e gás em parceria com a Petrobras, "
                "organizado pelo ECOA na PUC-Rio."
            ),
            "topicos_lista": """
            <ul>
                <li> Voltado a estudantes universitários com criatividade tecnológica</li>
                <li> Desenvolvimento de soluções para problemas reais</li>
                <li> Participação remunerada ou com bolsa conforme normas do ECOA / PUC</li>
            </ul>
            """
        },
        {
            "nome": "I9CULTURA / TECNOTOPIAS",
            "descricao": (
                "Programa de inovação cultural do Instituto ECOA PUC-Rio que valoriza o uso de tecnologia "
                "para promover transformações na área cultural."
            ),
            "topicos_lista": """
            <ul>
                <li> Desenvolve exposições e instalações com tecnologia, cultura e arte</li>
                <li> Programa gratuito e aberto ao público para participação e experimentação</li>
                <li> Instalações imersivas explorando cultura, meio ambiente e inovação</li>
            </ul>
            """
        },
    ]
    return render(request, "estagios.html", {"estagios": estagios})


def entidades(request):
    entidades = [
        {
            "nome": "PUC EMPRESA JÚNIOR",
            "img": "ej.png",
            "descricao": "Consultoria e projetos com clientes reais para desenvolvimento dos alunos nas áreas de gestão e tecnologia.",
            "tipo": "Empresa Júnior",
            "contatos": [
                {"icone": "person", "texto": "Maria Luiza Castro (Presidência 2025.2)"},
                {"icone": "alternate_email", "texto": "@pucempresa"},
                {"icone": "mail", "texto": "contato@pucempresa.br"},
            ]
        },
        {
            "nome": "DIRETÓRIO ACADÊMICO DE ENGENHARIA (DAENG)",
            "img": "deep.png",
            "descricao": "Representação estudantil dos cursos de engenharia: apoio acadêmico, eventos e integração dos alunos.",
            "tipo": "Diretório Acadêmico",
            "contatos": [
                {"icone": "alternate_email", "texto": "@daeng_puc"},
                {"icone": "mail", "texto": "daeng@puc-rio.br"},
            ]
        },
        {
            "nome": "CENTRO ACADÊMICO DE COMPUTAÇÃO (CACOMP)",
            "img": "com.png",
            "descricao": "Iniciativas para alunos de Ciência da Computação: hackathons, grupos de estudo e integração com o mercado.",
            "tipo": "Centro Acadêmico",
            "contatos": [
                {"icone": "alternate_email", "texto": "@cacomp_puc"},
                {"icone": "mail", "texto": "cacomp@puc-rio.br"},
            ]
        },
        {
            "nome": "COLETIVO ECOPUC",
            "img": "ecoa.png",
            "descricao": "Projetos ambientais no campus: reciclagem, comunicação e voluntariado voltados à sustentabilidade.",
            "tipo": "Coletivo",
            "contatos": [
                {"icone": "alternate_email", "texto": "@ecopuc"},
                {"icone": "mail", "texto": "ecopuc@puc-rio.br"},
            ]
        },
    ]
    return render(request, "entidades.html", {"entidades": entidades})


def mapa(request):
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


def sobre(request):
    return render(request, "sobre.html")




def iniciacao(request):
    iniciacoes = [
        {
            "nome": "PIBIC – Iniciação Científica com Bolsa",
            "descricao": (
                "O PIBIC é o principal programa de iniciação científica da PUC-Rio, oferecendo bolsas "
                "para estudantes que desejam desenvolver projetos de pesquisa com orientação docente."
            ),
            "topicos_lista": """
            <ul>
                <li><strong>Duração:</strong> 12 meses de pesquisa</li>
                <li><strong>Bolsa:</strong> Auxílio CNPq ou PUC</li>
                <li><strong>Resultado:</strong> Seminários e publicações</li>
            </ul>
            """
        },
        {
            "nome": "Laboratórios e Grupos de Pesquisa",
            "descricao": (
                "Os laboratórios da PUC-Rio oferecem ambientes de investigação em diversas áreas como "
                "tecnologia, humanidades, saúde e comunicação."
            ),
            "topicos_lista": """
            <ul>
                <li><strong>Participação:</strong> Com bolsa ou voluntária</li>
                <li><strong>Inscrição:</strong> Via professor orientador</li>
                <li><strong>Benefício:</strong> Experiência para mestrado e publicações</li>
            </ul>
            """
        },
        {
            "nome": "ECOA – Inovação e Pesquisa Criativa",
            "descricao": (
                "O Instituto ECOA desenvolve projetos interdisciplinares envolvendo tecnologia, cultura, "
                "sustentabilidade e arte, oferecendo experiências únicas aos alunos."
            ),
            "topicos_lista": """
            <ul>
                <li><strong>Diferencial:</strong> Pesquisa + Inovação</li>
                <li><strong>Ambiente:</strong> Colaborativo e criativo</li>
                <li><strong>Projetos:</strong> Exposições, mostras e prototipagem</li>
            </ul>
            """
        },
    ]

    return render(request, "iniciacao.html", {"iniciacoes": iniciacoes})
























