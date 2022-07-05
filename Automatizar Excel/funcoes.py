import pyautogui as py
import keyboard as kb
import pyperclip as pyper
import time as t


def copiar_conhecimento(dict, lista):
    """Função para copiar o campo de conhecimento"""
    counter = 1
    py.hotkey('alt', 'tab')
    py.press('enter')
    
    for i in lista:
        try:
            pyper.copy(dict[int(i)])
            
            with py.hold('ctrl'):
                py.press('v')
                t.sleep(0.3)
                if len(lista) == 1 or counter == len(lista):
                    break
                py.press('enter')
                
            counter += 1       
        except:
            continue
        
    # Ajuste e centralização
    with py.hold('alt'):
        py.press('h')
        py.press('w')
    py.hotkey('ctrl', 'shift', 'e')
    t.sleep(0.1)
    kb.send('tab')


def copiar_objetivo(dict, key_list, chave=''):
    """Função para copiar o objetivo(ID) e sua descrição"""
    counter = 1
    py.hotkey('alt', 'tab')
    py.press('enter')
    
    for i in key_list:
        pyper.copy(i)
        t.sleep(0.4)
        
        # Colando o código
        py.hotkey('ctrl', 'v')
        pyper.copy(f'{dict[i]}')        
        
        # Colando a descrição
        with py.hold('ctrl'):
            t.sleep(0.4)
            py.press('enter')
            t.sleep(0.4)
            py.press('v')
            if len(key_list) == 1 or counter == len(key_list):
                break
            py.hotkey('enter')
            py.hotkey('enter')
        
        counter += 1
    
    # Ajuste e centralização
    with py.hold('alt'):
        py.press('h')
        py.press('w')
    py.hotkey('ctrl', 'shift', 'e')
    t.sleep(0.1)
    kb.send('tab')


def colar_asterisco(quant):
    """Função para colocar asteríscos que serão utilizados para 
       digitar o planejamento"""
    py.hotkey('alt', 'tab')
    t.sleep(0.1)
    py.press('enter')
    
    for i in range(quant):
        py.write('*')
        if (i+1) == quant:
            break
        py.hotkey('ctrl', 'enter')
    
    # Ajuste e centralização
    with py.hold('alt'):
        py.press('h')
        py.press('w')
    py.hotkey('ctrl', 'shift', 'e')
    t.sleep(0.1)
    kb.send('tab')


def data(dia, mes, aula, quant):
    """Funcao para colocar o dia/mes e a aula correspondente"""
    py.hotkey('alt', 'tab')
    t.sleep(0.1)
    py.press('enter')
    
    for i in range(quant):
        py.write(f'{dia}/{mes}')   
        t.sleep(0.3)
        py.hotkey('ctrl', 'enter')
        t.sleep(0.1)
        
        py.write(f'Aula {aula}')
        
        dia += 1
        aula += 1
        
        # Ajuste e centralização
        with py.hold('alt'):
            py.press('h')
            py.press('w')
        py.hotkey('ctrl', 'shift', 'e')
        t.sleep(0.1)
        kb.send('enter')
        kb.send('enter')
        

if __name__ == '__main__':
    ...
