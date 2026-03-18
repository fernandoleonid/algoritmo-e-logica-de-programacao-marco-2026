def mostrarMenu():
    print ('#'*40)
    print ('1 - Adicionar')
    print ('2 - Subtrair')
    print ('3 - Multiplicar')
    print ('4 - Dividir')
    print ('5 - Fatorial')
    print ('0 - Sair')

def somar(a, b):
    return a + b

def subtrair (a, b):
    return a - b

def multiplicar (a, b):
    return a * b

def dividir (a, b):
    return a / b


def fatorial (a):
    fat = 1
    while a > 1:
        fat *= a
        a -=  1 

    return fat

    

def calculadora():
    mostrarMenu()
    opcao = input ('Escolha uma opçao: ')
    if opcao == "1":
        n1 = int(input('Digite o numero 1: '))
        n2 = int(input('Digite o numero 2: '))
        resultado = somar(n1, n2)
        print (resultado)
    elif opcao == "2":
        n1 = int(input('Digite o numero 1: '))
        n2 = int(input('Digite o numero 2: '))
        resultado = subtrair(n1, n2)
        print (resultado)
    elif opcao == "3":
        n1 = int(input('Digite o numero 1: '))
        n2 = int(input('Digite o numero 2: '))
        resultado = multiplicar(n1, n2)
        print (resultado)
    elif opcao == "4":
        n1 = int(input('Digite o numero 1: '))
        n2 = int(input('Digite o numero 2: '))
        resultado = dividir(n1, n2)
        print (resultado)
    elif opcao == "5":
        n1 = int(input('Digite um numero: '))
        resultado  = fatorial (n1)
        print (resultado)
    elif opcao == "0":
        return 0
    else:
        print ('Opção invalida, tente novamente!')
    calculadora()

calculadora()