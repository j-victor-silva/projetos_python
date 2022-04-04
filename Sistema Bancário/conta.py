from abc import ABC, abstractmethod
from typing import Type


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: int or float) -> None:
        self._agencia = agencia
        self._conta = conta
        self.saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor: int or float):
        self.saldo += valor
        print(f'\nVocê depositou o valor de: R${valor:.2f}\n'
              f'Valor total disponível: R${self.saldo:.2f}')

    def mostrar_informacoes(self):
        print(f"\n-Informações da Conta-\nAgência: {self.agencia}\n"
              f"Conta: {self.conta}\nSaldo Disponível: R${self.saldo:.2f}")

    @classmethod
    def class_name(cls):
        return cls.__name__


class ContaPoupanca(Conta):
    def sacar(self, valor: int or float):
        if valor > self.saldo:
            print('ERRO: Saldo insuficiente.')
            return

        self.saldo -= valor
        print(f'\nVocê sacou o valor de: R${valor:.2f}\n'
              f'Valor restante: R${self.saldo:.2f}')


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite: int or float) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: int or float):
        valor_salvo = 0
        if self.limite >= valor > self.saldo:
            valor_salvo += valor
            valor -= self.saldo
            self.saldo -= valor_salvo

            if self.saldo < 0:
                self.saldo = 0
                self.limite -= valor

            print(f'\nVocê sacou o valor de: R${valor_salvo:.2f}'
                  f'\nSaldo restante: R${self.saldo:.2f}'
                  f'\nLimite restante: R${self.limite:.2f}')
            return

        elif valor > self.limite:
            print('\nSALDO E LIMITE INSUFICIENTES.')
            return

        self.saldo -= valor
        print(f'\nVocê sacou o valor de: R${valor:.2f}'
              f'\nSaldo restante: R${self.saldo:.2f}'
              f'\nLimite restante: R${self.limite:.2f}')

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f'Limite disponível: {self.limite}')
