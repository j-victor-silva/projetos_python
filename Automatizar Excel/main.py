"""
Esse programa foi pensado para fazer primeiramente automações básicas
para o Excel, já que eu fazia muitas coisas usando ele
O programa vai basicamente copiar coisas que são muito usadas para as células do Excel
"""
import funcoes as func
import pyperclip as pyper
import pyautogui as py
import time


# Objetivos
conhecimento = {

    1: 'O Eu, O Outro e O Nós',
    2: 'Escuta, fala, pensamento e imaginação',
    3: 'Corpo, gestos e movimentos',
    4: 'Traços, sons, cores e formas',
    5: 'Espaços, tempos, quantidades, relações e tranformações',
}

objetivos = {
    'EI03EF01CRU': 'Expressar ideias, desejos e sentimentos sobre suas vivências, por meio da linguagem oral e escrita',
    'EI03CG05CRU': 'Coordenar suas habilidades manuais no atendimento adequadro a seus interesses e necessidades',
    'EI03TS02CRU': 'Expressar-se livremente por meio de desenhos, pintura e colagem',
    'EI03ET07CRU': 'Relacionar números a suas respectivas quantidades',
    'EI03CG03CRU': 'Criar movimentos, gestos, olhares e mímicas em brincadeiras, jogos e atividades artísticas como: dança, teatro e música voltadas para a exploração e valorização da cultura regional, local',
    'EI03CG02CRU': 'Demonstrar controle e adequação do uso de seu corpo em brincadeiras, jogos, escuta e reconto de histórias, atividades artísticas e culturais',
    'EI03EF06CRU': 'Produzir suas próprias histórias orais e escritas (escrita espontânea), em situação com função social significativa',
    'EI03TS01CRU': 'Utilizar sons produzidos por materiais, objetos e instrumentos musicais durante brincadeiras de faz de conta',
    'EI03ET03CRU': 'Identificar e selecionar fontes de informações, para responder a questões sobre a natureza',
    'EI03CG05CRU': 'Coordenar suas habilidades manuais no atendimento',
    'EI03ET01CRU': 'Estabelecer relações de comparação entre objetos, observando suas propriedades',
    'EI03CG01CRU': 'Criar com o corpo formas diversificadas de expressão de sentimentos, sensações e emoções, tanto nas situações do cotidiano quanto em brincadeiras, dança, teatro, etc.'
}


def pula_linha():
    print()


while True:
    print('\nDigite qual função você deseja executar:')
    escolha = input(f'\t1- Colar conhecimento;\n\t2- Colar objetivos;\n\t'
                    f'3- Colocar asteríscos;\n\t4- Colocar data e aula.\n\t->')

    pula_linha()

    if escolha == '1':
        conhecimento_formatado = ''
        for x, y in conhecimento.items():
            conhecimento_formatado += f'{x}:{y}\n'

        escolha = input(
            f'Aqui está a lista de conhecimentos:\n\n{conhecimento_formatado}\n->')
        time.sleep(1)
        func.copiar_conhecimento(conhecimento, int(escolha))

    elif escolha == '2':
        objetivos_formatados = ''
        for x, y in objetivos.items():
            objetivos_formatados += f'{x}:{y}\n\n'

        escolha = input(
            f'Aqui está a lista de objetivos:\n\n{objetivos_formatados}\n->')
        time.sleep(1)
        func.copiar_objetivo(objetivos, escolha)

    elif escolha == '3':
        escolha = input(
            'Digite a quandidade de asteríscos que deseja colocar: ')
        time.sleep(1)
        func.colar_asterisco(int(escolha))

    else:
        dia = input('Digite o dia: ')
        mes = input('Digite o mês: ')
        aula = input('Digite a aula: ')
        quantidade = input('Digite a quantidade de repetições: ')
        time.sleep(1)
        func.data(int(dia), int(mes), int(aula), int(quantidade))
