import sys
import pymysql.cursors
import os
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from criar_tabela import *
from gerenciador import *
from pathlib import Path


class Gerenciador(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.FILE_DIR = Path(__file__).parent

        self.btnAbrirDB.clicked.connect(self.abrir_db)

    def abrir_db(self):
        arquivo, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Arquivo',
            f'{self.FILE_DIR}'
        )

        dir, novo_arquivo = os.path.split(arquivo)
        

        self.inputDBName.setText(
            novo_arquivo
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = Gerenciador()

    app.show()
    qt.exec_()
