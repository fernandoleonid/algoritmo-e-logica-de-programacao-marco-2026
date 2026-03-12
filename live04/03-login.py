senha_cadastrada = 'asd'

senha_digitada = input('Digite sua senha: ')

while senha_cadastrada != senha_digitada:
    print (' -> Senha incorreta, tente novamente!')
    senha_digitada = input('Digite sua senha: ')

print (' -> Entrando no sistema...')