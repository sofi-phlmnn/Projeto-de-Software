# core/seeds.py

from django.utils.text import slugify
from core.models import Oportunidade, Tag, Contato, CategoriaOportunidade


# --------------------------------------------------------------------
# DADOS ORIGINAIS (copiados das listas que estavam nas views)
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
            {"nome": "química",     "cor": "orange"},
            {"nome": "engenharias", "cor": "blue"},
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


# --------------------------------------------------------------------
# FUNÇÕES AUXILIARES
# --------------------------------------------------------------------

def criar_oportunidade(entry, categoria_enum):
    """
    Cria ou atualiza uma Oportunidade a partir de um dicionário das listas *_DATA.
    Também cria Tags e Contatos relacionados.
    """
    nome = entry["nome"]
    descricao = entry["descricao"]
    img = entry.get("img", "")
    img2 = entry.get("img2", "")
    tipo = entry.get("tipo", "")
    topicos_lista = entry.get("topicos_lista", "")
    resumo = entry.get("resumo") or descricao[:200]  # resumo automático se não tiver
    texto_lateral = entry.get("texto_lateral", "")

    opp, created = Oportunidade.objects.get_or_create(
        nome=nome,
        categoria=categoria_enum,
        defaults={
            "descricao": descricao,
            "img": img,
            "img2": img2,
            "tipo": tipo,
            "topicos_lista": topicos_lista,
            "resumo": resumo,
            "texto_lateral": texto_lateral,
        },
    )

    if not created:
        # Atualiza se já existia
        opp.descricao = descricao
        opp.img = img
        opp.img2 = img2
        opp.tipo = tipo
        opp.topicos_lista = topicos_lista
        if not opp.resumo:
            opp.resumo = resumo
        opp.save()

    # Cria tags
    for tag_data in entry.get("tags", []):
        Tag.objects.get_or_create(
            oportunidade=opp,
            nome=tag_data["nome"],
            defaults={"cor": tag_data.get("cor", "orange")},
        )

    # Cria contatos
    for contato_data in entry.get("contatos", []):
        Contato.objects.get_or_create(
            oportunidade=opp,
            icone=contato_data.get("icone", ""),
            texto=contato_data["texto"],
        )

    print(f"{'Criado' if created else 'Atualizado'}: {opp.nome} ({categoria_enum.label})")


def run():
    print("== Criando EQUIPES ==")
    for e in EQUIPES_DATA:
        criar_oportunidade(e, CategoriaOportunidade.EQUIPE)

    print("== Criando DIRETÓRIOS ==")
    for d in DIRETORIOS_DATA:
        criar_oportunidade(d, CategoriaOportunidade.DIRETORIO)

    print("== Criando ESTÁGIOS / PROGRAMAS ==")
    for est in ESTAGIOS_DATA:
        criar_oportunidade(est, CategoriaOportunidade.ESTAGIO)

    print("== Criando ENTIDADES ==")
    for ent in ENTIDADES_DATA:
        criar_oportunidade(ent, CategoriaOportunidade.ENTIDADE)

    print("== Criando INICIAÇÃO CIENTÍFICA ==")
    for ini in INICIACOES_DATA:
        criar_oportunidade(ini, CategoriaOportunidade.INICIACAO)

    print("Pronto! Seeds executado.")
