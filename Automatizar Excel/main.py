"""
Esse programa foi pensado para fazer primeiramente automações básicas
para o Excel, já que eu fazia muitas coisas usando ele
O programa vai basicamente copiar coisas que são muito usadas para as células do Excel
"""
import funcoes as func
import time as t
import json
from pathlib import Path


DIRECTORY = Path(__file__).parent
conhecimento = {
    1: 'O Eu, O Outro e O Nos',
    2: 'Escuta, fala, pensamento e imaginacao',
    3: 'Corpo, gestos e movimentos',
    4: 'Traços, sons, cores e formas',
    5: 'Espacos, tempos, quantidades, relações e tranformacoes',
}
objetivos = DIRECTORY / 'objectives.json'


with open(objetivos) as file:
    objectives = json.load(file)
    
    while True:
        try:
            print('\nDigite qual função você deseja executar:')
            escolha = input(f'\t1- Colar conhecimento;\n\t2- Colar objetivos;\n\t'
                            f'3- Colocar asteríscos;\n\t4- Colocar data e aula.\n\t->')
            
            # Opção para colar os conhecimentos
            if escolha == '1':
                conhecimento_formatado = ''
                for x, y in conhecimento.items():
                    conhecimento_formatado += f'{x}:{y}\n'

                esc = [x for x in input(
                    f'\nAqui está a lista de conhecimentos:\n\n{conhecimento_formatado}\n->'
                    ).split(',')]
                func.copiar_conhecimento(conhecimento, esc)

            # Opção para colar os objetivos
            elif escolha == '2':
                esc = [x for x in input(
                    f'\nDigite aqui os códigos dos objetivos:\n->'
                    ).split(',')]
                func.copiar_objetivo(objectives, esc)

            # Irá colar os asteriscos
            elif escolha == '3':
                escolha = input(
                    '\nDigite a quandidade de asteríscos que deseja colocar: '
                    )
                func.colar_asterisco(int(escolha))

            # Irá colocar os dias e aulas
            elif escolha == '4':
                dia = int(input('\nDigite o dia: '))
                mes = int(input('Digite o mês: '))
                aula = int(input('Digite a aula: '))
                quantidade = int(input('Digite a quantidade de repetições: '))
                func.data(dia, mes, aula, quantidade)
        except:
            print('Você precisa digitar uma opção válida.')
            t.sleep(1)
            continue
        