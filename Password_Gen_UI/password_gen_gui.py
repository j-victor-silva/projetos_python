import sys
import string
from PyQt5.QtWidgets import QApplication, QMainWindow
from password import gera_senha
from design import *


class Gerador(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.minus = False
        self.maius = False
        self.digits = False
        self.special = False

        self.btnGerar.clicked.connect(self.gerar_senha)

    def gerar_senha(self):
        if self.boxMinusculo.isChecked():
            self.minus = True
        else:
            self.minus = False

        if self.boxMaiuscula.isChecked():
            self.maius = True
        else:
            self.maius = False

        if self.boxNumeros.isChecked():
            self.digits = True
        else:
            self.digits = False

        if self.boxEspeciais.isChecked():
            self.special = True
        else:
            self.special = False

        self.inputRetorno.setText(
            str(gera_senha(self.boxQntd.value(), self.minus,
                           self.maius, self.digits, self.special))
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = Gerador()
    app.show()
    qt.exec_()
