from datetime import datetime
import instaloader as is_


# Irá carregar a lib e fazer login na conta do Instagram
dados = is_.Instaloader()
dados.login('USUÁRIO', 'SENHA')


# Vai verificar os dados do usuário escolhido
seguidores = is_.Profile.from_username(dados.context, "j.victor_slv <- Aqui vai ser colocado o user").get_followers()
seguindo = is_.Profile.from_username(dados.context, "j.victor_slv <- Aqui vai ser colocado o user").get_followees()


# Vai exibir no terminal o total de seguidores e de pessoas que o user segue e as informações dos seguidores
print('\n')
print('Seguidores: ' + str(seguidores._data['count']))
print('\nSeguindo: ' + str(seguindo._data['count']))
print('\n\n')
print('Lista e informações de seguidores:')
print('\n')
print(seguidores._data['edges'])
