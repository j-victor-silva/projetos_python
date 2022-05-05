import sys
import pymysql.cursors
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from login import *
from login_erro import *
from typing import Type


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
           a database na hora que for chamada a classe
           ATUALIZAÇÃO: Consegui resolver me baseando no erro de quando
           a classe é chamada na "filha" sem usar o super(), mudando o nome
           do inicializador resolveu o problema'''
        self.cursor = self.conexao.cursor()

    def dados(self, table) -> dict:
        comando = f'SELECT * FROM {table}'
        self.cursor.execute(comando)
        self.listagem = self.cursor.fetchall()
        print(self.listagem)

    def encerrar(self):
        self.cursor.close()
        self.conexao.close()


class LoginWindow(QMainWindow, Ui_MainWindow, Conexao):
    def __init__(self, database: str, error: Type[Conexao],
                 conexao: str = '127.0.0.1', parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        super().__initt__(database, conexao)  # Inicializador da classe Conexao
        '''Por algum motivo se a classe for chamada ao invés de ser usado o
           super() o programa dá erro, então tive que alterar o nome do 
           inicializador da classe Conexao'''
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


class LoginError(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnErro.clicked.connect(self.close)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    error = LoginError()
    app = LoginWindow('usuarios', error)

    app.show()
    qt.exec_()

    if app.close:
        app.encerrar()
