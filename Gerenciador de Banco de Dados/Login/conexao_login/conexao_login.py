import pymysql.cursors


class Conexao():
    def __init__(self, database: str, conexao: str = '127.0.0.1') -> None:
        self.conexao = pymysql.connect(
            host=conexao,
            user='root',
            password='',
            db=database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        '''Resolvido problema de herança das classes'''
        self.cursor = self.conexao.cursor()

    def dados(self, table) -> dict:
        comando = f'SELECT * FROM {table}'
        self.cursor.execute(comando)
        self.listagem = self.cursor.fetchall()

    def encerrar(self):
        self.cursor.close()
        self.conexao.close()
