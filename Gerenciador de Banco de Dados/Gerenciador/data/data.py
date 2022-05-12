from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex
from PyQt5.QtGui import QColor


class CustomTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)
        self._dados = data[0]
        self._colunas = data[1]
        
        self.load_data(self._dados)
        
    def load_data(self, dados):
        self.numero_linhas = len(dados)
        self.numero_colunas = len(dados[0])
        
    def rowCount(self, parent=QModelIndex()):
        return self.numero_linhas
    
    def columnCount(self, parent=QModelIndex()):
        return self.numero_colunas
    
    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return self._colunas[section].upper()
        else:
            return section
    
    def data(self, index, role=Qt.DisplayRole):
        column = index.column()
        row = index.row()
        
        if role == Qt.DisplayRole:
            return self._dados[row][column]
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignLeft
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        
        return None