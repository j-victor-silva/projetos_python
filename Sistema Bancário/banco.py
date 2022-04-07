from cliente import Cliente
from conta import Conta, ContaCorrente, ContaPoupanca
from typing import Type


class Banco:
    def __init__(self) -> None:
        self.agencia = [1111, 2222, 3333]
        self.conta = []
        self.cliente = []
        self.cliente_dict = dict({})

    def adicionar_cliente_e_conta(self, conta: Type[Conta], cliente: Type[Cliente]) -> None:
        self.cliente.append(cliente)
        self.conta.append(conta)
        # if not cliente.conta:
        cliente.adicionar_conta(conta)
        self.cliente_dict[cliente] = conta

    def info_total(self):
        for cliente in self.cliente:
            cliente.mostrar_informacoes_cliente()
            self.separa()

    def autenticacao(self, cliente):
        if self.cliente_dict[cliente]._agencia not in self.agencia:
            return False
        
        if cliente not in self.cliente:
            return False
        
        if self.cliente_dict[cliente] not in self.conta:
            return False
        
        return True

    @staticmethod
    def separa():
        print('#' * 30)


banco_1 = Banco()
cliente_1 = Cliente('João', 19)
conta_1 = ContaCorrente(1112, 2222, 0, 100)

banco_1.adicionar_cliente_e_conta(conta_1, cliente_1)
if banco_1.autenticacao(cliente_1):
    cliente_1.conta.sacar(10)
    
else:
    print('Cliente não autenticado.')
