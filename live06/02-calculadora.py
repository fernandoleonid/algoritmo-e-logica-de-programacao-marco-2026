from matematica  import *

import os

from colorama import Fore, Style, init

init()

def limparTela():
    os.system('clear')

def pausar():
    input('Aperte ENTER para continuar...')

def mostrarMenu():
    print ('#'*40)
    print ('1 - Adicionar')
    print ('2 - Subtrair')
    print ('3 - Multiplicar')
    print ('4 - Dividir')
    print ('5 - Fatorial')
    print ('0 - Sair')

def calculadora():
    mostrarMenu()
    opcao = input ('Escolha uma opçao: ')
    if opcao == "1":
        n1 = int(input('Digite o numero 1: '))
        n2 = int(input('Digite o numero 2: '))
        resultado = somar(n1, n2)
        limparTela()
        print (f'{Fore.GREEN}{resultado}{Style.RESET_ALL}')
        pausar()
    elif opcao == "2":
        n1 = int(input('Digite o numero 1: '))
        n2 = int(input('Digite o numero 2: '))
        resultado = subtrair(n1, n2)
        limparTela()
        print (resultado)
        pausar()
    elif opcao == "3":
        n1 = int(input('Digite o numero 1: '))
        n2 = int(input('Digite o numero 2: '))
        resultado = multiplicar(n1, n2)
        limparTela()
        print (resultado)
        pausar()
    elif opcao == "4":
        n1 = int(input('Digite o numero 1: '))
        n2 = int(input('Digite o numero 2: '))
        resultado = dividir(n1, n2)
        limparTela()
        print (resultado)
        pausar()
    elif opcao == "5":
        n1 = int(input('Digite um numero: '))
        resultado  = fatorial (n1)
        limparTela()
        print (resultado)
        pausar()
    elif opcao == "0":
        return 0
    else:
        print (f'{Fore.RED}Opção invalida, tente novamente!{Style.RESET_ALL}')
    calculadora()

if __name__ == '__main__':
    calculadora()