import os

from colorama import Fore, Style, init

init ()


def limpar_tela():
    os.system('clear')

def exibir_menu():
    print ('#'*20)
    print ('1 - Cadastrar uma tarefa')
    print ('2 - Listar as tarefas')
    print ('3 - Modificar tarefa')
    print ('4 - Remover tarefa')
    print ('5 - Trocar status')
    print ('0 - Sair')
    print ('#'*20)

def  buscar_tarefa_por_id(id_escolhido):
    print ('Buscar tarefa por ID...')

def cadastrar_tarefa():
    print ('Cadastrar tarefa...')

def listar_tarefas():
    print ('Listar tarefas...')

def modificar_tarefa():
    print ('Modificar Tarefa...')

def remover_tarefa():
    print ('Remover tarefa...')

def trocar_status():
    print ('Trocar status...')

def app():
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
        elif resposta == 5:
            trocar_status()
        elif resposta == 0:
            print('Saindo do sistema...')
            break
        else:
            print (f'{Fore.RED}Opção errada, tenta novamente!{Style.RESET_ALL}')

if __name__ == '__main__':
    app()