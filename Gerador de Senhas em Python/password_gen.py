import string as s
import random as r


# Esse programa irá ler, primeiramente:
# - Para que site/programa o usuário quer gerar uma senha;
# - Qual o usuário ou e-mail daquele site/programa;
# - Irá gerar uma senha baseado no tamanho da senha que o usuário quer, mínimo 8;
# - Salvar em um documento de texto;
#

# Função para gerar a senha
def password(tam=8):
    senha = ''
    for i in range(tam):
        valor_letters = r.randint(0, len(s.ascii_letters)-1)
        valor_digits = r.randint(0, len(s.digits)-1)
        valor_punctuation = r.randint(0, len(s.punctuation)-1)
        senha += s.ascii_letters[valor_letters] + \
            s.digits[valor_digits] + s.punctuation[valor_punctuation]

    return senha[0:tam]


# Loop para gerar quantas senhas o usuário precisar
while True:
    file = open("senhas.txt", "a+")
    topico = input('\nSite ou programa que a senha será gerada: ')
    file.write(f'\nSite ou Programa: {topico}\n')
    user = input('\nUsuário ou Email que vai receber a nova senha: ')
    file.write(f'\n\tUsuario ou Email: {user}\n')
    inp_senha = input(
        '\nDigite o tamanho que terá sua senha, caso não digite nada ou digite um valor '
        'menor que 8 a senha terá um tamanho de 8 caracteres: ')

    if inp_senha == "" or int(inp_senha) < 7:
        file.write(f'\tSenha: {password()}\n')

    else:
        file.write(f'\tSenha: {password(int(inp_senha))}\n')

    topico_continue = input(
        '\nVocê deseja criar uma nova senha? Digite Sim ou Nao.\n\n->')
    if topico_continue.lower() == 'sim':
        continue

    else:
        file.close()
        break
