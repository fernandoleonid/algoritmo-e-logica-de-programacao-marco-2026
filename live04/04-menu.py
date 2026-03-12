opcao = None

while opcao != '0':
    print ('#'*30)
    print ('1 - Mostrar nome')
    print ('2 - Mostrar nota')
    print ('3 - Mostrar situação')
    print ('0 - Sair')
    print ('#'*30)
    opcao = input ('Escolha uma opção: ')
    if opcao == '1':
        print (' -> Fernando Leonid')
    elif opcao == '2':
        print (' -> 6.0')
    elif opcao == '3':
        print (' -> Aprovado')
    elif opcao == '0':
        print (' -> Saindo do sistema...')
    else:
        print (' -> Opção errada, tente novamente')