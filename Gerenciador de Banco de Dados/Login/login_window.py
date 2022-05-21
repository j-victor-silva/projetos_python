import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from Login.design.login import *
from Login.design.login_erro import *
from Login.conexao_login.conexao_login import *


class LoginError(QDialog, Ui_Dialog):
    '''Classe que irá criar a mensagem de erro ao não fazer login'''
    
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)


class LoginWindow(QMainWindow, Ui_MainWindow, Conexao):
    def __init__(self, database: str,
                 conexao: str = '127.0.0.1', parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        # Inicializador da classe Conexao
        Conexao.__init__(self, database, conexao)
        self.valido = False

        # Instancia que irá chamar a DialogBox de erro
        self.error = LoginError()
        
        # Botão para logar
        # self.btnEntrar.clicked.connect(self.autenticar)
        
        # Botão para fechar erro de login
        self.error.btnErro.clicked.connect(self.error.close)

    def autenticar(self):
        '''Método de autenticação
        
        Irá verificar na base de dados se o usuário e a senha correspondem
        para assim, logar'''
        
        index = 0
        while True:
            self.dados('usuariosroot')
            user = self.inputUser.text()
            password = self.inputPassword.text()

            try:
                if not user == self.listagem[index]['usuario'] or not password == self.listagem[index]['senha']:
                    index += 1

                if user == self.listagem[index]['usuario'] and password == self.listagem[index]['senha']:
                    self.valido = True
                    return

            except IndexError as e:
                self.valido = False
                self.error.show()
                return


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = LoginWindow('usuarios')

    app.show()
    qt.exec_()

    if app.close:
        app.encerrar()
