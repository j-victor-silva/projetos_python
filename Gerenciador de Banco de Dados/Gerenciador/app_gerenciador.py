import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog
from typing import Type
from pathlib import Path
from data.data import *
from design.criar_tabela import *
from design.gerenciador import *
from conexao.conexao import *
import design.sucesso as sucesso


class CriarTabela(QDialog, Ui_Dialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        

class Sucesso(QDialog, sucesso.Ui_Sucesso):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)


class Gerenciador(QMainWindow, Ui_MainWindow, ConexaoDB):
    def __init__(self, database: str,
                 conexao: str = '127.0.0.1', parent=None) -> None:
        # Conectando a tela do programa
        super().__init__(parent)
        super().setupUi(self)
        # Chamando a conexão com a database
        ConexaoDB.__init__(self, database, conexao)

        # Será chamado a janela para criar a tabela
        self.window = CriarTabela()
        # Janela que irá aparecer após criar a tabela com sucesso
        self.sucesso = Sucesso()

        # Por padrão o diretório que irá ser aberto é o do programa
        self.FILE_DIR = Path(__file__).parent  

        # Botão para abrir a DB
        self.btnAbrirDB.clicked.connect(self.abrir_db)  

        # Botão para ver dados
        self.btnDados.clicked.connect(self.select_table)
        
        # Botão para abrir a janela de criação de tabelas
        self.btnCriarTable.clicked.connect(self.window.show)  
        
        # Botão para criar a tabela
        self.window.btnCreate.clicked.connect(self.create_table)
        
        # Botão para fechar a tela que indica que foi criada a tabela
        self.sucesso.btnSucesso.clicked.connect(self.sucesso.close)

    def abrir_db(self) -> None:
        '''Método para abrir o arquivo DB
        
        Esse método irá realizar a conexão com o computador para que indique
        qual o arquivo dump que irá ser aberto para assim, poder visualizar
        as tabelas, dados e realizar alterações'''
        
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
        '''Método para visualizar as tabelas do banco de dados
        
        Esse método irá (até o momento) visualizar as tabelas quando
        o arquivo for selecionado'''
        
        tables = []
        self.cursor.execute('SHOW tables')
        self.conexao.commit()
        self.tabelas = self.cursor.fetchall()

        for i in self.tabelas:
            for l in i:
                tables.append(l)

        return tables

    def view_data(self, tabela):
        '''Método executar o comando de dados da tabela selecionada
        
        Esse método irá executar dentro de um botão, onde irá ser mostrado
        os dados daquela tabela selecionada, por enquanto, não irá ser
        mostrado tabelas que não possuem dados
        
        Esse método não é executado sozinho, mas com o método abaixo'''
        
        self.cursor.execute(f'SELECT * FROM {tabela}')
        self.conexao.commit()
        resultados = self.cursor.fetchall()

        num_column = len(self.cursor.description)
        nome_colunas = [x[0] for x in self.cursor.description]

        final = (resultados, nome_colunas)

        return final

    def select_table(self):
        '''Método para mostrar os dados na tela
        
        Esse método, junto com o anterior, irão mostrar os dados na tela'''
        
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
        '''Método para criar uma tabela
        
        Esse método irá ser executado ao clicar em um botão, onde irá ser
        exibida uma nova janela com novas opções, onde você irá colocar:
        o nome da tabela, as colunas e a chave primária
        
        OBS: Por enquanto a chave primária deve ser colocada sozinha, fora
        do campo de colunas, onde também será necessário especificar qual
        tipo de variável ela será'''
        
        table_name = self.window.inputNameTable.text()
        table_property = self.window.inputNameColumn.toPlainText()
        table_primary = self.window.inputPrimaryKey.text()
        
        try:
            comando = ''
            if self.window.boxAI.isChecked():
                comando = (f'CREATE TABLE {table_name} ('
                    f'{table_primary} PRIMARY KEY AUTO_INCREMENT, '
                    f'{table_property}'
                    f')'
                    )
            else:
                comando = (f'CREATE TABLE {table_name} ('
                    f'{table_primary} PRIMARY KEY, '
                    f'{table_property}'
                    f')'
                    )

            self.cursor.execute(comando)
            self.conexao.commit()
            self.sucesso.show()
        except:
            return

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
    app = Gerenciador('funcionarios')

    app.show()
    qt.exec_()

    if app.close:
        app.encerrar()
