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
        novo_arquivo = ''
        arquivo, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Arquivo',
            f'{self.FILE_DIR}'
        )

        for root, dir, files in os.walk(self.FILE_DIR):
            for file in files:
                arquivo_name, arquivo_ext = os.path.splitext(file)
                full_path = os.path.join(root, file)
                full_path = full_path.replace('\\', '/')
                full_path = re.sub('e', 'E', full_path, 1)
                if full_path == arquivo:
                    novo_arquivo = os.path.join(arquivo_name, arquivo_ext)
                    novo_arquivo = novo_arquivo.replace('\\', '')
                else:
                    continue

        self.inputDBName.setText(
            arquivo
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = Gerenciador()

    app.show()
    qt.exec_()
