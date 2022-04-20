'''
Exercicio com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas correntes tem um limite extra. Banco
tem clientes e contas

Dicas:
Criar classe Cliente que herda da classe Pessoa (herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para deposito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    Polimorfismo - As subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Bancos tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível autenticar se passar na autenticação acima
'''
from classe.banco import Banco
from classe.cliente import Cliente
from classe.conta import ContaCorrente, ContaPoupanca

cliente_1 = Cliente('João', 19)
conta_1 = ContaCorrente(2222, 1111, 0, 100)
banco_1 = Banco(2222, 1111)
banco_1.adicionar_cliente(conta_1, cliente_1)
banco_1.autenticacao(cliente_1)
