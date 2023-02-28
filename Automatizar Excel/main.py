"""
Esse programa foi pensado para fazer primeiramente automações básicas
para o Excel, já que eu fazia muitas coisas usando ele
O programa vai basicamente copiar coisas que são muito usadas para as células do Excel

O que foi mudado nesta versão:
    - Adicionado opção para sair;
    - Corrigido escrita do conhecimento que não escrevia caracteres utf-8;
    - Melhorada a função de data/aula;
    - Refatorado código de funções e corrigido alguns bugs.
"""
# coding: utf-8

import funcoes as func
import time as t
import json
from pathlib import Path


DIRECTORY = Path(__file__).parent
conhecimento = {
    1: 'O Eu, O Outro e O Nós',
    2: 'Escuta, fala, pensamento e imaginação',
    3: 'Corpo, gestos e movimentos',
    4: 'Traços, sons, cores e formas',
    5: 'Espaços, tempos, quantidades, relações e tranformações',
}
objetivos = DIRECTORY / 'objectives.json'


with open(objetivos) as file:
    objectives = json.load(file)
    
    while True:
        try:
            print('\nDigite qual função você deseja executar:')
            escolha = input(f'\t1- Colar conhecimento;'
                            f'\n\t2- Colar objetivos;'
                            f'\n\t3- Colocar asteríscos;'
                            f'\n\t4- Colocar data e aula.'
                            f'\n\t5- Sair' 
                            f'\n\t-> ')
            
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
            
            # Sair do programa
            elif escolha == '5':
                break
            
        except:
            print('Você precisa digitar uma opção válida.')
            t.sleep(1)
            continue
        