# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(219, 124)
        MainWindow.setMinimumSize(QtCore.QSize(219, 124))
        MainWindow.setMaximumSize(QtCore.QSize(219, 124))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.inputUser = QtWidgets.QLineEdit(self.centralwidget)
        self.inputUser.setObjectName("inputUser")
        self.gridLayout.addWidget(self.inputUser, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.inputPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPassword.setText("")
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassword.setObjectName("inputPassword")
        self.gridLayout.addWidget(self.inputPassword, 1, 1, 1, 1)
        self.btnEntrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEntrar.setObjectName("btnEntrar")
        self.gridLayout.addWidget(self.btnEntrar, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Usuário"))
        self.label_2.setText(_translate("MainWindow", "Senha"))
        self.btnEntrar.setText(_translate("MainWindow", "Entrar"))