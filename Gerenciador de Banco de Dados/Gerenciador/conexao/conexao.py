import pymysql.cursors


class ConexaoDB():
    '''Conexão com o banco de dados Funcionarios'''

    def __init__(self, database: str, conexao: str = '127.0.0.1') -> None:
        self.conexao = pymysql.connect(
            host=conexao,
            user='root',
            password='',
            db=database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.Cursor
        )

        self.cursor = self.conexao.cursor()

    def encerrar(self):
        self.cursor.close()
        self.conexao.close()
        