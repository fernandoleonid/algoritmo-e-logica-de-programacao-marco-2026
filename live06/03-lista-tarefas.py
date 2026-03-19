import os

from colorama import Fore, Style, init

init ()

banco_dados = ['Comprar passagem', 'Pagar aluguel']


def limpar_tela():
    os.system('clear')

def exibir_menu():
    print ('#'*20)
    print ('1 - Cadastrar uma tarefa')
    print ('2 - Listar as tarefas')
    print ('3 - Modificar tarefa')
    print ('4 - Remover tarefa')
    print ('0 - Sair')
    print ('#'*20)

def cadastrar_tarefa():
    tarefa_nova = input('Digite uma nova tarefa: ')
    banco_dados.append(tarefa_nova)

def listar_tarefas():
    limpar_tela()
    for pos, tarefa in enumerate(banco_dados):
        print (f'{pos + 1} - {tarefa}')
    print()

def modificar_tarefa():
    listar_tarefas()
    pos = int(input ('Escolha o número da tarefa para modificar: '))
    tarefa_modificada = input ('Digite a nova tarefa: ')
    banco_dados[pos - 1] = tarefa_modificada

def remover_tarefa():
    listar_tarefas()
    pos = int(input('Escolha o número da tarfa para remover: '))
    banco_dados.pop(pos - 1)

def lista_tarefas():
    while True:
        exibir_menu()
        resposta = int(input('Escolha um opção: '))
        if resposta == 1:
            cadastrar_tarefa()
        elif resposta == 2:
            listar_tarefas()
        elif resposta == 3:
            modificar_tarefa()
        elif resposta == 4:
            remover_tarefa()
        elif resposta ==0:
            print('Sainda do sistema...')
            break
        else:
            print ('Opção errada, tenta novamente!')

if __name__ == '__main__':
    lista_tarefas()