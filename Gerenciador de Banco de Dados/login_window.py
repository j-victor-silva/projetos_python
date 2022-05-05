import sys
import pymysql.cursors
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from login import *
from login_erro import *


class Conexao():
    def __initt__(self, database: str, conexao: str = '127.0.0.1') -> None:
        self.conexao = pymysql.connect(
            host=conexao,
            user='root',
            password='',
            db=database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        '''Conexão criada para o servidor local sql, ou então pra qualquer
           servidor que for atribuido, por algum motivo não é possível
           a database na hora que for chamada a classe'''
        self.cursor = self.conexao.cursor()

    def lista(self, table) -> dict:
        comando = f'SELECT * FROM {table}'
        self.cursor.execute(comando)
        self.listagem = self.cursor.fetchall()

    def encerrar(self) -> None:
        self.cursor.close()
        self.conexao.close()


class LoginWindow(QMainWindow, Ui_MainWindow, Conexao):
    def __init__(self, database, conexao: str = '127.0.0.1', parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        super().__initt__(database, conexao) # Inicializador da classe Conexao
        '''Por algum motivo se a classe for chamada ao invés de ser usado o
           super() o programa dá erro, então tive que alterar o nome do 
           inicializador da classe Conexao'''

        self.btnEntrar.clicked.connect(self.autenticar)

    def autenticar(self):
        while True:
            self.lista('usuariosroot')
            user = self.inputUser.text()
            password = self.inputPassword.text()

            for linha in self.listagem:
                if user in linha['usuario'] and password in linha['senha']:
                    if user == '' or password == '':
                        print('Usuário ou senha inválidos')
                        break

                    print('Usuario autenticado')
                    break
                if not user in linha['usuario'] and password in linha['senha']:
                    print('Usuário ou senha inválidos')
                    break
                else:
                    continue

            break


class LoginError(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnErro.clicked.connect(self.encerrar)

    def encerrar(self):
        self.close()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = LoginWindow('usuarios')
    error = LoginError()

    app.show()
    qt.exec_()

    # database = Conexao('usuarios')
    # database.lista('usuariosroot')
    # database.encerrar()
