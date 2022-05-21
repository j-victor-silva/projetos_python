import sys
from PyQt5.QtWidgets import QApplication
from Gerenciador.data import data
from Gerenciador import app_gerenciador
from Login.login_window import *


class App:
    '''Classe que conecta os dois programas
    
    A classe App irá conectar a janela de login e caso seja autenticado
    com sucesso, irá abrir o gerenciador'''
    
    def __init__(self):
        # Instância para conectar a tela de login e sua Database
        self.login = LoginWindow('usuarios')
        # Instância para conectar o gerenciador
        self.gerenciador = app_gerenciador.Gerenciador()
        
        self.login.btnEntrar.clicked.connect(self.entrar)
        
    def abrir(self):
        '''Método para abrir a tela de login'''
        
        self.login.show()

    def entrar(self):
        '''Método para abrir o gerenciador
        
        Caso seja autenticado o login, irá abrir o gerenciador e fechar
        a tela de login'''
        
        self.login.autenticar()
        if self.login.valido:
            self.login.close()
            self.gerenciador.show()

        
qt = QApplication(sys.argv)
app = App()

app.abrir()
qt.exec()
