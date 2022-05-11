import sys
import pymysql.cursors
import os
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from criar_tabela import *
from gerenciador import *
from pathlib import Path


class ConexaoDB():
    '''Conexão com o banco de dados Funcionarios'''

    def __initt__(self, database: str, conexao: str = '127.0.0.1') -> None:
        self.conexao = pymysql.connect(
            host=conexao,
            user='root',
            password='',
            db=database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        self.cursor = self.conexao.cursor()

    def encerrar(self):
        self.cursor.close()
        self.conexao.close()


class Gerenciador(QMainWindow, Ui_MainWindow, ConexaoDB):
    def __init__(self, database: str, conexao: str = '127.0.0.1',
                 parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        super().__initt__(database, conexao)

        self.FILE_DIR = Path(__file__).parent  # Por padrão o diretório que irá
        # ser aberto é o do programa

        self.btnAbrirDB.clicked.connect(self.abrir_db)  # Botão para abrir a DB

    def abrir_db(self) -> None:
        # Método para abrir o arquivo DB
        arquivo, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Arquivo',
            f'{self.FILE_DIR}'
        )

        _, novo_arquivo = os.path.split(arquivo)

        if not '.sql' in novo_arquivo:
            return

        self.inputDBName.setText(
            novo_arquivo
        )

        self.listTables.addItems(
            self.view_table()
        )

    def view_table(self):
        tables = []
        self.cursor.execute('SHOW tables')
        self.conexao.commit()
        self.tabelas = self.cursor.fetchall()

        for i in self.tabelas:
            for t in i.values():
                tables.append(t)
            # tables.replace("dict_values([''])", '')

        return tables
    
    def view_data(self):
        ...


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = Gerenciador('funcionarios')

    app.show()
    qt.exec_()

    if app.close:
        app.encerrar()
