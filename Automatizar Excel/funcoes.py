import pyautogui as py
import pyperclip as pyper
import time


# Função para copiar o objetivo(ID) e sua descrição
def copiar_colar(dict, key, chave=''):
    for k in dict.keys():
        if not k == key:
            continue
        
        chave = k
    
    pyper.copy(chave)
    time.sleep(3)
    py.doubleClick()
    py.hotkey('ctrl', 'v')
    
    pyper.copy(f'\n{dict[key]}')
    with py.hold('ctrl'):
        py.press('enter')
    py.hotkey('ctrl', 'v')
    
    

# Funcao para colocar o dia/mes e a aula correspondente
def data(dia, mes, aula, quant):
    time.sleep(3)
    for i in range(quant):
        if not dia >= 10:
            py.write(f'0{dia}/0{mes}')
        
        else:
            py.write(f'{dia}/0{mes}')
            
        with py.hold('ctrl'):
            py.press('enter')

        py.write(f'Aula {aula}')
        dia += 1
        aula += 1
        py.press('enter')
        

# Função para colocar asteríscos que serão utilizados para digitar o planejamento
def colar_asterisco(quant):
    quant1 = 0
    time.sleep(3)
    while quant1 != quant:
        with py.hold('ctrl'):
            py.press('enter')
        py.write('*')
        quant1 += 1
        

