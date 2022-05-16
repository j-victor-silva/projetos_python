import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog
from typing import Type
from pathlib import Path
from data.data import *
from design.criar_tabela import *
from design.gerenciador import *
from conexao.conexao import *


class CriarTabela(QDialog, Ui_Dialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)


class Gerenciador(QMainWindow, Ui_MainWindow, ConexaoDB):
    def __init__(self, database: str, window: Type[CriarTabela],
                 conexao: str = '127.0.0.1', parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        ConexaoDB.__init__(self, database, conexao)

        self.window = window  # Será chamado a janela para criar a tabela

        self.FILE_DIR = Path(__file__).parent  # Por padrão o diretório que irá
        # ser aberto é o do programa

        self.btnAbrirDB.clicked.connect(self.abrir_db)  # Botão para abrir a DB

        self.btnDados.clicked.connect(
            self.select_table)  # Botão para ver dados

        self.btnCriarTable.clicked.connect(
            self.window.show)  # Botão para criar
        # a tabela
        self.window.btnCreate.clicked.connect(self.create_table)

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
            for l in i:
                tables.append(l)

        return tables

    def view_data(self, tabela):
        self.cursor.execute(f'SELECT * FROM {tabela}')
        self.conexao.commit()
        resultados = self.cursor.fetchall()

        num_column = len(self.cursor.description)
        nome_colunas = [x[0] for x in self.cursor.description]

        final = (resultados, nome_colunas)

        return final

    def select_table(self):
        try:
            tabela = self.listTables.selectedIndexes()[0]
            dados = self.view_data(tabela.data())

            self.modelo = CustomTableModel(dados)
            self.dadosViewer.setModel(self.modelo)
            self.dadosViewer.setStyleSheet(
                'font-size: 11px;'
            )
        except:
            return

    def create_table(self):
        table_name = self.window.inputNameTable.text()
        print(table_name)
        # self.cursor.execute('CREATE TABLE {} ('
        #     '{},'
        #     '{}'
        #     ')'.format())

    def delete_table(self):
        ...

    def insert_data(self):
        ...

    def alter_data(self):
        ...

    def delete_data(self):
        ...


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    criar_tabela = CriarTabela()
    app = Gerenciador('funcionarios', criar_tabela)

    app.show()
    qt.exec_()

    if app.close:
        app.encerrar()
