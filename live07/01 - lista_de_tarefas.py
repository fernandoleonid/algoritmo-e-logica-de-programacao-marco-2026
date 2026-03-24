import os

from colorama import Fore, Style, init

init ()

banco_dados = [
    {"id":1,"tarefa":"Comprar passagem", "feito":False},
    {"id":2,"tarefa":"Pagar aluguel", "feito":True},
    {"id":3,"tarefa":"Correr", "feito": False}
]

proximo_id = 4

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
    for item in banco_dados:
        if item['id'] == id_escolhido:
            return item    
    return False

def cadastrar_tarefa():
    global proximo_id
    tarefa = input ("Digite uma nova tarefa: ")
    nova_tarefa = {
        "id": proximo_id,
        "tarefa":tarefa,
        "feito": False
      }
    banco_dados.append(nova_tarefa)
    proximo_id += 1

def listar_tarefas():
    limpar_tela()
    print (f"{'ID':<5} {'TAREFA':<30} {'STATUS'}")
    print ('-'*50)

    for item in banco_dados:
        if item['feito']:
            status = f"{Fore.GREEN} Feito {Style.RESET_ALL}"
        else:
            status = f"{Fore.RED} Pendente {Style.RESET_ALL}"

        print (f"{item['id']:<5} {item['tarefa']:<30} {status}")
    print ('-'*50)

def modificar_tarefa():
    listar_tarefas()
    id_escolhido = int (input("Escolha um id para modificar: "))
    tarefa = buscar_tarefa_por_id(id_escolhido)
    if tarefa:
        nova_tarefa = input(f"Digite a nova tarefa (atual: {tarefa['tarefa']}): ")
        tarefa['tarefa'] = nova_tarefa
        print (f"{Fore.BLUE}Tarefa modificada com sucesso!{Style.RESET_ALL}")
        resposta = input ("Deseja ver a lista de tarefas [s|n]: ")
        if resposta == 's':
            listar_tarefas()

    else:
        print (f'{Fore.RED}ID não encontrado!{Style.RESET_ALL}')

def remover_tarefa():
    listar_tarefas()
    id_escolhido = int (input ("Escolha um ID para remover: "))
    tarefa = buscar_tarefa_por_id(id_escolhido)
    if tarefa:
        banco_dados.remove(tarefa)
    else:
        print (f'{Fore.RED}ID não encontrado!{Style.RESET_ALL}')

def trocar_status():
    listar_tarefas()
    id_escolhido = int (input ("Escolha um ID para trocar o status: "))
    tarefa = buscar_tarefa_por_id(id_escolhido)
    if tarefa:
        tarefa['feito'] = not tarefa['feito']
    else:
        print (f'{Fore.RED}ID não encontrado!{Style.RESET_ALL}')

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