import sys
from PyQt5.QtWidgets import QApplication
from Gerenciador.data import data
from Gerenciador import app_gerenciador
from Login.login_window import *


class App:
    def __init__(self):
        self.login = LoginWindow('usuarios')
        self.gerenciador = app_gerenciador.Gerenciador()
        
        self.login.btnEntrar.clicked.connect(self.entrar)
        
    def abrir(self):
        self.login.show()

    def entrar(self):
        self.login.autenticar()
        if self.login.valido:
            self.login.close()
            self.gerenciador.show()

        
qt = QApplication(sys.argv)
app = App()

app.abrir()
qt.exec()
