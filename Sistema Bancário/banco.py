from cliente import Cliente
from conta import Conta, ContaCorrente, ContaPoupanca
from typing import Type


class Banco:
    def __init__(self, agencia: int, conta: int) -> None:
        self._agencia = agencia
        self._conta = conta
        self.cliente_conta = []
        self.cliente_dict = dict({})

    def adicionar_cliente(self, conta: Type[Conta], cliente: Type[Cliente]) -> None:
        self.cliente = cliente
        self.cliente.adicionar_conta(conta)
        self.cliente_dict[cliente] = conta
        self.cliente_conta.append(self.cliente)

    def info_unico(self, index: int):
        self.cliente_conta[index].mostrar_informacoes_cliente()

    def info_total(self):
        for cliente in self.cliente_conta:
            cliente.mostrar_informacoes_cliente()
            self.separa()

    def autenticacao(self, cliente):
        if self.cliente_dict[cliente]._agencia == self._agencia:
            if cliente in self.cliente_conta:
                if self.cliente_dict[cliente]._conta == self._conta:
                    print('Cliente autenticado!')
                else:
                    print('Não autenticado!')
            else:
                print('Não autenticado!')
        else:
            print('Não autenticado!')

    @staticmethod
    def separa():
        print('#' * 30)
