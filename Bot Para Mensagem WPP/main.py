import pyautogui as pygui
import time as ti

"""
156 742 = EDGE
16 260 = WPP
16 260
596 700 = Chat
458 716  
399 742
699 465
"""

# O programa fará:
# - Vai clicar no EDGE na barra de tarefas
# - Vai clicar na aba do Whatsapp
# - Vai clicar no chat de Elis
# - Vai digitar "Oi, isso foi digitado por um bot -By: Seu Namorado"
# - Vai minimizar o EDGE
# - Vai clicar em um espaço vazio do VSCODE
# - Vai dar um espaço e digitar "# Isso é um comentário"

pygui.click(156, 742)
pygui.click(16, 260)
pygui.click(250, 260)
pygui.click(596, 700)
pygui.write("Oi, isso foi digitado por um bot -By: Seu Namorado")
ti.sleep(0.1) # Isso  um comentario
pygui.press("enter")
pygui.click(399, 742)
pygui.click(699, 465)
pygui.press('end')
pygui.write(" # Isso é um comentario")