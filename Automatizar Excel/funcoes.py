# coding: utf-8

import pyautogui as py
import keyboard as kb
import pyperclip as pyper
import time as t


def ajuste_centralizar(mode=0):
    # Ajuste e centralização
    kb.press_and_release('alt+h')
    t.sleep(0.3)
    py.press('w')
    py.hotkey('ctrl', 'shift', 'e')
    t.sleep(0.4)
    if not mode == 0:
        kb.send('enter')
        kb.send('enter')
    else:
        kb.send('tab')
        

def copiar_conhecimento(dict, lista):
    """Função para copiar o campo de conhecimento"""
    counter = 1
    py.hotkey('alt', 'tab')
    py.press('enter')
    
    for i in lista:
        try:
            kb.write(dict[int(i)])
            
            if len(lista) == 1 or counter == len(lista):
                break
            kb.press_and_release('ctrl+enter')
                
            counter += 1       
        except:
            continue
        
    ajuste_centralizar()


def copiar_objetivo(dict, key_list):
    """Função para copiar o objetivo(ID) e sua descrição"""
    counter = 1
    py.hotkey('alt', 'tab')
    py.press('enter')
    
    for i in key_list:
        # Irá escrever o código do objetivo
        kb.write(i)
        kb.press_and_release('ctrl+enter, ctrl+enter')
        
        # Irá escrever o objetivo
        kb.write(dict[i])
        t.sleep(1)
        
        if len(key_list) > 1:
            if counter == len(key_list):
                break
            kb.press_and_release('ctrl+enter, ctrl+enter')
        
        counter += 1
    
    ajuste_centralizar()


def colar_asterisco(quant):
    """Função para colocar asteríscos que serão utilizados para 
       digitar o planejamento"""
    py.hotkey('alt', 'tab')
    t.sleep(0.1)
    py.press('enter')
    
    for i in range(quant):
        py.write('*')
        py.hotkey('ctrl', 'enter')
        if (i) == quant:
            break
    
    ajuste_centralizar()


def data(dia, mes, aula, quant):
    """Funcao para colocar o dia/mes e a aula correspondente"""
    py.hotkey('alt', 'tab')
    t.sleep(0.1)
    py.press('enter')
    
    for i in range(quant):
        if dia < 10:
            if mes < 10:
                py.write(f'0{dia}/0{mes}')
            else:
                py.write(f'0{dia}/{mes}')
        elif dia > 10:
            if mes < 10:
                py.write(f'{dia}/0{mes}')
            else:
                py.write(f'{dia}/{mes}')
           
        t.sleep(0.3)
        py.hotkey('ctrl', 'enter')
        t.sleep(0.1)
        
        if aula < 10:
            py.write(f'Aula 0{aula}')
        else:
            py.write(f'Aula {aula}')
        
        dia += 1
        aula += 1
        
        ajuste_centralizar(mode=1)        
        

if __name__ == '__main__':
    ...
