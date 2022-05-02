import random


def gera_senha(tam=8, minus=False, maius=False, numbers=False, special=False
               ):
    senha = ''
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '0123456789'
    especiais = '!@#$%&*()+=-_/;:{}[]'
    while not len(senha) == tam:
        num = random.randint(0, 3)
        if minus and num == 0:
            senha += random.choice(minusculas)
        elif maius and num == 1:
            senha += random.choice(maiusculas)
        elif numbers and num == 2:
            senha += random.choice(numeros)
        elif special and num == 3:
            senha += random.choice(especiais)
        elif not minus and not maius and not numbers and not special:
            return "Selecione alguma das caixas!"

    return senha


if __name__ == '__main__':
    print(gera_senha(8, minus=False, maius=False, numbers=False, special=False))
