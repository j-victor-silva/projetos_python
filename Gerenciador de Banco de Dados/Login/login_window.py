import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from design.login import *
from design.login_erro import *
from typing import Type
from conexao_login.conexao_login import *


class LoginError(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnErro.clicked.connect(self.close)


class LoginWindow(QMainWindow, Ui_MainWindow, Conexao):
    def __init__(self, database: str, error: Type[LoginError],
                 conexao: str = '127.0.0.1', parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        # Inicializador da classe Conexao
        Conexao.__init__(self, database, conexao)

        self.error = error  # Instancia que irá chamar a DialogBox de erro
        self.btnEntrar.clicked.connect(self.autenticar)

    def autenticar(self):
        index = 0
        while True:
            self.dados('usuariosroot')
            user = self.inputUser.text()
            password = self.inputPassword.text()

            try:
                if not user == self.listagem[index]['usuario'] or not password == self.listagem[index]['senha']:
                    index += 1

                if user == self.listagem[index]['usuario'] and password == self.listagem[index]['senha']:
                    return True

            except IndexError as e:
                self.error.show()
                return


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    error = LoginError()
    app = LoginWindow('usuarios', error)

    app.show()
    qt.exec_()

    if app.close:
        app.encerrar()
