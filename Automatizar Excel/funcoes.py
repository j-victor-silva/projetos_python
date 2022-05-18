import pyautogui as py
import pyperclip as pyper
import time as t


def copiar_conhecimento(dict, index):
    """Função para copiar o campo de conhecimento"""
    pyper.copy(dict[index])
    py.press('enter')
    with py.hold('ctrl'):
        py.press('v')
        t.sleep(0.5)
        py.press('enter')
    t.sleep(0.5)
    py.press('enter')
    t.sleep(0.1)
    py.press('up')


def copiar_objetivo(dict, key, chave=''):
    """Função para copiar o objetivo(ID) e sua descrição"""
    for k in dict.keys():
        if not k == key:
            continue

        chave = k

    pyper.copy(chave)
    t.sleep(1)
    py.press('enter')
    py.hotkey('ctrl', 'v')

    pyper.copy(f'\n{dict[key]}')
    with py.hold('ctrl'):
        py.press('enter')
        py.press('v')
        py.press('enter')
        py.press('enter')
    py.press('enter')
    py.press('up')


def colar_asterisco(quant):
    """Função para colocar asteríscos que serão utilizados para 
       digitar o planejamento"""
    quant1 = 0
    t.sleep(1)
    while quant1 != quant:
        py.hotkey('ctrl', 'enter')
        py.write('*')
        quant1 += 1


def data(dia, mes, aula, quant):
    """Funcao para colocar o dia/mes e a aula correspondente"""
    t.sleep(1)
    for i in range(quant):
        if not dia >= 10:
            py.write(f'0{dia}/0{mes}')

        else:
            py.write(f'{dia}/0{mes}')

        py.hotkey('ctrl', 'enter')

        py.write(f'Aula {aula}')
        dia += 1
        aula += 1
        py.press('enter')
        
def formatar():
    # Função para formatar as células 14x6
    for i in range(14):
        with py.hold('shift'): py.press('down')


if __name__ == '__main__':
    t.sleep(2)
    formatar()
