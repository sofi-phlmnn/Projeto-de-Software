from django.shortcuts import render

def equipe_view(request):
    equipes = [
        {
            "nome": "RIOROBOTZ",
            "img": "rio.jpg",  # coloque em static/img/rio.jpg
            "descricao": (
                "A RioBotz é a equipe de competições robóticas da PUC-Rio, que visa projetar, "
                "otimizar e construir robôs de combate, humanoides, de sumô, e para diversas outras categorias. "
                "A RioBotz é uma referência mundial de inovação em Robótica, permitindo aos alunos desenvolverem "
                "capacidades não apenas em engenharia mas também em liderança, organização, comunicação, gestão e trabalho em equipe."
            ),
        },
        {
            "nome": "PEGASUS",
            "img": "pegasus.png",  # static/img/pegasus.png
            "descricao": (
                "A equipe PEGASUS é responsável por desenvolver carros de corrida no estilo Fórmula SAE, "
                "desde o projeto até a competição. Com um ambiente plural e inclusivo, reunimos estudantes de diferentes áreas, "
                "promovendo a troca de ideias e inovação. Divididos em dois núcleos — Projeto e Comercial — organizamos esforços em sete setores especializados. "
                "Nosso objetivo é aprimorar conhecimentos e alcançar a excelência na competição, aplicando na prática o que aprendemos em sala de aula."
            ),
        },
        {
            "nome": "AERORIO",
            "img": "aero.jpg",  # static/img/aero.jpg
            "descricao": (
                "A AeroRio é uma equipe de desenvolvimento e construção de aeronaves não tripuladas, como drones e aviões de asa fixa. "
                "O grupo busca constantemente novos conhecimentos e desafios, participando de competições nacionais e internacionais, "
                "bem como atuando no desenvolvimento de projetos de pesquisa. A equipe é composta por alunos de diversas Engenharias, "
                "integrando teoria e prática com foco em multidisciplinaridade, trabalho em equipe, proatividade e organização."
            ),
        },
        {
            "nome": "REPTILES BAJA",
            "img": "reptiles.png",  # static/img/reptiles.png
            "descricao": (
                "A equipe Reptiles Baja PUC-Rio constrói um veículo off-road, desde o projeto até a manufatura, "
                "para participar de competições organizadas pela SAE-Brasil. Além da aplicação prática dos conteúdos de sala, "
                "estimula habilidades como liderança, proatividade, organização, respeito e disciplina."
            ),
        },
    ]
    return render(request, "equipe.html", {"equipes": equipes})
