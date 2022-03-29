import string


def pula_linha(quantidade=1):
    print('\n' * quantidade)
    

def decor(quantidade=30, lacos=1):
    for i in range(lacos):
        print('#' * quantidade)
        

def criptografia(msg):
    lista = list(string.printable)
    

criptografia()