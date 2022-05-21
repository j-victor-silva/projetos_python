import sys

sys.path.insert(0, 'E:\Python-\projetos\Gerenciador de Banco de Dados\Gerenciador')

import design.erro_tabela as e_table
import design.erro_dados as e_data
import design.erro_alterar_valores as e_values
import design.erro_del as e_del
import design.sucesso as sucesso
import design.erro_db as e_db
from PyQt5.QtWidgets import QDialog


class ErroDatabase(QDialog, e_db.Ui_Dialog):
    '''Classe para criar janela de erro ao selecionar database'''

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        
        
class ErroTabela(QDialog, e_table.Ui_Dialog):
    '''Classe para criar a janela de erro na criação da tabela'''

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)


class Sucesso(QDialog, sucesso.Ui_Sucesso):
    '''Classe para criar a janela de sucesso na criação da tabela'''

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)


class ErroDados(QDialog, e_data.Ui_Dialog):
    '''Classe para criar a janela de erro ao inserir dados'''

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)


class ErroAlterarValores(QDialog, e_values.Ui_Dialog):
    '''Classe para criar janela de erro ao editar valores'''

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)


class ErroDel(QDialog, e_del.Ui_Dialog):
    '''Classe para criar janela de erro ao deletar valores'''

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
