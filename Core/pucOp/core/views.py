from django.shortcuts import render
from django.urls import reverse
from django.http import Http404


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
# EQUIPES  
# --------------------------------------------------------------------
EQUIPES_DATA = [
    {
        "id": 1,
        "nome": "RioBotz",
        "img": "rio.jpg",
        "img2": "riobotz-mini.png",
        "descricao": (
            "A RioBotz é a equipe de competições robóticas da PUC-Rio, que visa projetar, "
            "otimizar e construir robôs de combate, humanoides, de sumô, e para diversas outras categorias. "
            "A RioBotz é uma referência mundial de inovação em Robótica, permitindo aos alunos desenvolverem "
            "capacidades não apenas em engenharia mas também em liderança, organização, comunicação, gestão e trabalho em equipe."
        ),
        "contatos": [
            {"icone": "alternate_email", "texto": "@riorobotz"},
        ],
        "tags": [
            {"nome": "combate",    "cor": "orange"},
            {"nome": "humanoides", "cor": "blue"},
            {"nome": "automação",  "cor": "green"},
        ],
    },
    {
        "id": 2,
        "nome": "Pegasus",
        "img": "pegasus.png",
        "img2": "pegasus-mini.png",
        "descricao": (
            "A equipe PEGASUS é responsável por desenvolver carros de corrida no estilo Fórmula SAE, "
            "desde o projeto até a competição. Com um ambiente plural e inclusivo, reunimos estudantes de diferentes áreas, "
            "promovendo a troca de ideias e inovação. Divididos em dois núcleos — Projeto e Comercial — organizamos esforços em sete setores especializados. "
            "Nosso objetivo é aprimorar conhecimentos e alcançar a excelência na competição, aplicando na prática o que aprendemos em sala de aula."
        ),
        "contatos": [
            {"icone": "alternate_email", "texto": "@pegasus_puc"},
        ],
        "tags": [
            {"nome": "fórmula SAE", "cor": "orange"},
            {"nome": "carros",      "cor": "blue"},
            {"nome": "projeto",     "cor": "green"},
        ],
    },
    {
        "id": 3,
        "nome": "AeroRio",
        "img": "aero.jpg",
        "img2": "aerorio-mini.png",
        "descricao": (
            "A AeroRio é uma equipe de desenvolvimento e construção de aeronaves não tripuladas, como drones e aviões de asa fixa. "
            "O grupo busca constantemente novos conhecimentos e desafios, participando de competições nacionais e internacionais, "
            "bem como atuando no desenvolvimento de projetos de pesquisa. A equipe é composta por alunos de diversas Engenharias, "
            "integrando teoria e prática com foco em multidisciplinaridade, trabalho em equipe, proatividade e organização."
        ),
        "contatos": [
            {"icone": "alternate_email", "texto": "@aerorio"},
        ],
        "tags": [
            {"nome": "aeronaves", "cor": "orange"},
            {"nome": "drones",    "cor": "blue"},
            {"nome": "pesquisa",  "cor": "green"},
        ],
    },
    {
        "id": 4,
        "nome": "Reptiles Baja",
        "img": "reptiles.png",
        "img2": "reptiles-mini.png",
        "descricao": (
            "A equipe Reptiles Baja PUC-Rio constrói um veículo off-road, desde o projeto até a manufatura, "
            "para participar de competições organizadas pela SAE-Brasil. Além da aplicação prática dos conteúdos de sala, "
            "estimula habilidades como liderança, proatividade, organização, respeito e disciplina."
        ),
        "contatos": [
            {"icone": "alternate_email", "texto": "@reptilesbaja"},
        ],
        "tags": [
            {"nome": "off-road",    "cor": "orange"},
            {"nome": "baja",        "cor": "blue"},
            {"nome": "prototipagem","cor": "green"},
        ],
    },
]



def equipes(request):
    return render(request, "equipe.html", {"equipes": EQUIPES_DATA})


def equipe_detalhe(request, id):
    """Página de detalhe de equipe usando ID e template genérico."""
    equipe = next((e for e in EQUIPES_DATA if e["id"] == id), None)
    if not equipe:
        raise Http404("Equipe não encontrada.")

    ctx = {
        "categoria_label": "Equipe de competição",
        "objeto": equipe,                     # usado no detalhe_oportunidade.html
        "voltar_url": reverse("core:equipes"),
    }
    return render(request, "detalhe_oportunidade.html", ctx)


# --------------------------------------------------------------------
# DIRETÓRIOS  
# --------------------------------------------------------------------
DIRETORIOS_DATA = [
    {
        "id": 1,
        "nome": "DAAF",
        "img": "daff2.png",
        "img2": "daaf-mini.png",
        "descricao": (
            "O Diretório Acadêmico de Administração e Finanças (DAAF) acolhe os alunos "
            "tanto academicamente quanto socialmente, promovendo integração, eventos e "
            "apoio ao longo da graduação."
        ),
        "tipo": "Diretório Acadêmico",
        "contatos": [
            {"icone": "alternate_email", "texto": "@daaf_puc"},
            {"icone": "mail",            "texto": "daaf@puc-rio.br"},
        ],
        "tags": [
            {"nome": "administração", "cor": "orange"},
            {"nome": "eventos",       "cor": "blue"},
            {"nome": "apoio",         "cor": "green"},
        ],
    },
    {
        "id": 2,
        "nome": "DAQEQ",
        "img": "daqeq.png",
        "img2": "daqeq-mini.png",
        "descricao": (
            "O Diretório Acadêmico de Química e das Engenharias Química e de Materiais "
            "atua na luta pelos direitos dos alunos, promove eventos acadêmicos e culturais."
        ),
        "tipo": "Diretório Acadêmico",
        "contatos": [
            {"icone": "alternate_email", "texto": "@daqeq_puc"},
            {"icone": "mail",            "texto": "daqeq@puc-rio.br"},
        ],
        "tags": [
            {"nome": "química",   "cor": "orange"},
            {"nome": "engenharias","cor": "blue"},
            {"nome": "representação","cor": "green"},
        ],
    },
    {
        "id": 3,
        "nome": "CAINF",
        "img": "cainf2.png",
        "img2": "cainf-mini.png",
        "descricao": (
            "O Centro Acadêmico de Informática (CAINF) representa os alunos da Computação, "
            "promovendo palestras, grupos de estudo e eventos de tecnologia."
        ),
        "tipo": "Centro Acadêmico",
        "contatos": [
            {"icone": "alternate_email", "texto": "@cainf_puc"},
            {"icone": "mail",            "texto": "cainf@puc-rio.br"},
        ],
        "tags": [
            {"nome": "computação", "cor": "orange"},
            {"nome": "palestras",  "cor": "blue"},
            {"nome": "eventos",    "cor": "green"},
        ],
    },
]



def diretorios(request):
    return render(request, "diretorios.html", {"diretorios": DIRETORIOS_DATA})


def diretorio_detalhe(request, id):
    diretorio = next((d for d in DIRETORIOS_DATA if d["id"] == id), None)
    if not diretorio:
        raise Http404("Diretório não encontrado.")

    ctx = {
        "categoria_label": "Diretório / Centro Acadêmico",
        "objeto": diretorio,
        "voltar_url": reverse("core:diretorios"),
    }
    return render(request, "detalhe_oportunidade.html", ctx)


# --------------------------------------------------------------------
# ESTÁGIOS / PROGRAMAS (apenas lista por enquanto)
# --------------------------------------------------------------------
ESTAGIOS_DATA = [
    {
        "id": 1,
        "nome": "APPLE DEVELOPER ACADEMY – PUC-RIO",
        "img": "apple-academy.png",
        "img2": "apple-academy-mini.png",
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
        """,
        "tags": [
            {"nome": "apps",        "cor": "orange"},
            {"nome": "inovação",    "cor": "blue"},
            {"nome": "mentoria",    "cor": "green"},
        ],
    },
    {
        "id": 2,
        "nome": "PROGRAMA DE ESTÁGIO PETROBRAS",
        "img": "petrobras.png",
        "img2": "petrobras-mini.png",
        "descricao": "Programa de estágio nacional da Petrobras para estudantes de nível técnico ou superior.",
        "topicos_lista": """
            <ul>
                <li> Estágios para cursos técnicos ou superiores</li>
                <li> Bolsa-auxílio recente: R$ 1.825,00</li>
                <li> Carga horária típica: 20 horas semanais</li>
            </ul>
        """,
        "tags": [
            {"nome": "óleo e gás", "cor": "orange"},
            {"nome": "estágio",    "cor": "blue"},
            {"nome": "nacional",   "cor": "green"},
        ],
    },
    {
        "id": 3,
        "nome": "IGNIÇÃO PETROBRAS / ECOA PUC-RIO",
        "img": "ignicao.png",
        "img2": "ignicao-mini.png",
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
        """,
        "tags": [
            {"nome": "inovação",    "cor": "orange"},
            {"nome": "óleo e gás",  "cor": "blue"},
            {"nome": "ECOA",        "cor": "green"},
        ],
    },
    {
        "id": 4,
        "nome": "I9CULTURA / TECNOTOPIAS",
        "img": "i9cultura.png",
        "img2": "i9cultura-mini.png",
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
        """,
        "tags": [
            {"nome": "cultura",     "cor": "orange"},
            {"nome": "tecnologia",  "cor": "blue"},
            {"nome": "arte",        "cor": "green"},
        ],
    },
]



def estagios(request):
    return render(request, "estagios.html", {"estagios": ESTAGIOS_DATA})


def estagio_detalhe(request, id):
    estagio = next((e for e in ESTAGIOS_DATA if e["id"] == id), None)
    if not estagio:
        raise Http404("Estágio não encontrado.")

    ctx = {
        "categoria_label": "Programa de estágio / inovação",
        "objeto": estagio,                     # usado em detalhe_oportunidade.html
        "voltar_url": reverse("core:estagios"),
    }
    return render(request, "detalhe_oportunidade.html", ctx)



# --------------------------------------------------------------------
# ENTIDADES 
# --------------------------------------------------------------------
ENTIDADES_DATA = [
    {
        "id": 1,
        "nome": "PUC EMPRESA JÚNIOR",
        "img": "ej.png",
        "img2": "ej-mini.png",
        "descricao": "Consultoria e projetos com clientes reais para desenvolvimento dos alunos nas áreas de gestão e tecnologia.",
        "tipo": "Empresa Júnior",
        "contatos": [
            {"icone": "person",           "texto": "Maria Luiza Castro (Presidência 2025.2)"},
            {"icone": "alternate_email",  "texto": "@pucempresa"},
            {"icone": "mail",             "texto": "contato@pucempresa.br"},
        ],
        "tags": [
            {"nome": "consultoria", "cor": "orange"},
            {"nome": "gestão",      "cor": "blue"},
            {"nome": "projetos",    "cor": "green"},
        ],
    },
    {
        "id": 2,
        "nome": "DIRETÓRIO ACADÊMICO DE ENGENHARIA (DAENG)",
        "img": "deep.png",
        "img2": "daeng-mini.png",
        "descricao": "Representação estudantil dos cursos de engenharia: apoio acadêmico, eventos e integração dos alunos.",
        "tipo": "Diretório Acadêmico",
        "contatos": [
            {"icone": "alternate_email", "texto": "@daeng_puc"},
            {"icone": "mail",            "texto": "daeng@puc-rio.br"},
        ],
        "tags": [
            {"nome": "engenharia", "cor": "orange"},
            {"nome": "apoio",      "cor": "blue"},
            {"nome": "integração","cor": "green"},
        ],
    },
    {
        "id": 3,
        "nome": "CENTRO ACADÊMICO DE COMPUTAÇÃO (CACOMP)",
        "img": "com.png",
        "img2": "cacomp-mini.png",
        "descricao": "Iniciativas para alunos de Ciência da Computação: hackathons, grupos de estudo e integração com o mercado.",
        "tipo": "Centro Acadêmico",
        "contatos": [
            {"icone": "alternate_email", "texto": "@cacomp_puc"},
            {"icone": "mail",            "texto": "cacomp@puc-rio.br"},
        ],
        "tags": [
            {"nome": "hackathons", "cor": "orange"},
            {"nome": "estudos",    "cor": "blue"},
            {"nome": "mercado",    "cor": "green"},
        ],
    },
    {
        "id": 4,
        "nome": "COLETIVO ECOPUC",
        "img": "ecoa.png",
        "img2": "ecopuc-mini.png",
        "descricao": "Projetos ambientais no campus: reciclagem, comunicação e voluntariado voltados à sustentabilidade.",
        "tipo": "Coletivo",
        "contatos": [
            {"icone": "alternate_email", "texto": "@ecopuc"},
            {"icone": "mail",            "texto": "ecopuc@puc-rio.br"},
        ],
        "tags": [
            {"nome": "sustentabilidade","cor": "orange"},
            {"nome": "reciclagem",      "cor": "blue"},
            {"nome": "voluntariado",    "cor": "green"},
        ],
    },
]



def entidades(request):
    return render(request, "entidades.html", {"entidades": ENTIDADES_DATA})


def entidade_detalhe(request, id):
    entidade = next((e for e in ENTIDADES_DATA if e["id"] == id), None)
    if not entidade:
        raise Http404("Entidade não encontrada.")

    ctx = {
        "categoria_label": "Entidade estudantil",
        "objeto": entidade,                       # usado em detalhe_oportunidade.html
        "voltar_url": reverse("core:entidades"),  # botão de voltar
    }
    return render(request, "detalhe_oportunidade.html", ctx)


# --------------------------------------------------------------------
# MAPA
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


# --------------------------------------------------------------------
# INICIAÇÃO CIENTÍFICA
# --------------------------------------------------------------------
INICIACOES_DATA = [
    {
        "id": 1,
        "nome": "PIBIC – Iniciação Científica com Bolsa",
        "img": "pibic.png",
        "img2": "pibic-mini.png",
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
        """,
        "tags": [
            {"nome": "bolsa",    "cor": "orange"},
            {"nome": "pesquisa", "cor": "blue"},
            {"nome": "publicações","cor": "green"},
        ],
    },
    {
        "id": 2,
        "nome": "Laboratórios e Grupos de Pesquisa",
        "img": "laboratorios.png",
        "img2": "laboratorios-mini.png",
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
        """,
        "tags": [
            {"nome": "laboratórios", "cor": "orange"},
            {"nome": "interdisciplinar","cor": "blue"},
            {"nome": "formação",     "cor": "green"},
        ],
    },
    {
        "id": 3,
        "nome": "ECOA – Inovação e Pesquisa Criativa",
        "img": "ecoa-pesquisa.png",
        "img2": "ecoa-pesquisa-mini.png",
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
        """,
        "tags": [
            {"nome": "inovação",     "cor": "orange"},
            {"nome": "sustentabilidade","cor": "blue"},
            {"nome": "arte & tech",  "cor": "green"},
        ],
    },
]



def iniciacao(request):
    return render(request, "iniciacao.html", {"iniciacoes": INICIACOES_DATA})


def iniciacao_detalhe(request, id):
    iniciacao_obj = next((i for i in INICIACOES_DATA if i["id"] == id), None)
    if not iniciacao_obj:
        raise Http404("Iniciação científica não encontrada.")

    ctx = {
        "categoria_label": "Iniciação científica / pesquisa",
        "objeto": iniciacao_obj,
        "voltar_url": reverse("core:iniciacao"),
    }
    return render(request, "detalhe_oportunidade.html", ctx)
