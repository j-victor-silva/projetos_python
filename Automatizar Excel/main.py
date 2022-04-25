"""
Esse programa foi pensado para fazer primeiramente automações básicas
para o Excel, já que eu fazia muitas coisas usando ele
O programa vai basicamente copiar coisas que são muito usadas para as células do Excel
"""
import funcoes as func
import pyperclip as pyper
import pyautogui as py
import time as t


conhecimento = {

    1: 'O Eu, O Outro e O Nós',
    2: 'Escuta, fala, pensamento e imaginação',
    3: 'Corpo, gestos e movimentos',
    4: 'Traços, sons, cores e formas',
    5: 'Espaços, tempos, quantidades, relações e tranformações',
}

objetivos = {
    'EI03EF01CRU': 'Expressar ideias, desejos e se     tntos sobre suas vivências, por meio da linguagem oral e escrita',
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
    'EI03CG01CRU': 'Criar com o corpo formas diversificadas de expressão de se     tntos, sensações e emoções, tanto nas situações do cotidiano quanto em brincadeiras, dança, teatro, etc.',
    'EI03ET05': 'Classificar e reconhecer objetos e figuras de acordo com suas semelhanças e diferenças',
    'EI03E003CRU': 'Ampliar as relações interpessoais, desenvolvendo atitudes de participação, cooperação e solidariedade',
    'EI03EF02CRU': 'Inventar brincadeiras, cantadas, poemas e canções, criando rimas',
    'EI03ET04CRU': 'Registrar observações, manipulações e medidas, usando múltiplas linguagens (desenho, registro por números ou escrita espontânea)',
    'EI02CG05CRU': 'Coordenar suas habilidades manuais no atendimento adequado a seus interesses e necessidades em situações diversas',
    'EI03EF07CRU': 'Levantar hipóteses sobre gêneros textuais veiculados em portadores conhecidos recorrendo a estratégias de observação',
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
        py.hotkey('alt', 'tab')
        t.sleep(0.1)
        func.copiar_conhecimento(conhecimento, int(escolha))

    elif escolha == '2':
        objetivos_formatados = ''
        for x, y in objetivos.items():
            objetivos_formatados += f'{x}:{y}\n\n'

        escolha = input(
            f'Aqui está a lista de objetivos:\n\n{objetivos_formatados}\n->')
        py.hotkey('alt', 'tab')
        t.sleep(0.1)
        func.copiar_objetivo(objetivos, escolha)

    elif escolha == '3':
        escolha = input(
            'Digite a quandidade de asteríscos que deseja colocar: ')
        py.hotkey('alt', 'tab')
        t.sleep(0.1)
        func.colar_asterisco(int(escolha))

    elif escolha == '4':
        dia = input('Digite o dia: ')
        mes = input('Digite o mês: ')
        aula = input('Digite a aula: ')
        quantidade = input('Digite a quantidade de repetições: ')
        py.hotkey('alt', 'tab')
        t.sleep(0.1)
        func.data(int(dia), int(mes), int(aula), int(quantidade))

    else:
        print('Você precisa digitar uma opção válida.')
        t.sleep(1)
        continue
