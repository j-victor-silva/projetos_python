from conta import ContaCorrente, ContaPoupanca, Conta
from typing import Type


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def _nome(self):
        return self.nome

    @_nome.setter
    def _nome(self, valor: str):
        self.nome = valor.title()

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def adicionar_conta(self, conta: Type[Conta]):
        self.conta = conta

    def mostrar_informacoes_cliente(self):
        print(f"-Informações do Cliente-\nNome: {self.nome}\n"
              f"Idade: {self.idade}"
              f"\nTipo de Conta: {self.conta.class_name()}")
        self.conta.mostrar_informacoes()
