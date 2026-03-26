import os
import sqlite3

from colorama import Fore, Style, init
init ()

conexao = sqlite3.connect('./live08/tarefa.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas  (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        tarefa  TEXT,
        feito   INTEGER DEFAULT 0
    )
''')
conexao.commit()


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
    tarefa_nova = input ('Digite uma nova tarefa: ')
    cursor.execute('INSERT INTO tarefas (tarefa) VALUES (?)',(tarefa_nova,))
    conexao.commit()


def listar_tarefas():
    limpar_tela()
    cursor.execute('SELECT * FROM tarefas')
    tarefas = cursor.fetchall()
    print (f"{'ID':<5} {'TAREFA':<30} {'STATUS'}")
    print ('-'*50)

    for item in tarefas:
        id, tarefa, feito = item

        if feito:
            status = f"{Fore.GREEN} Feito {Style.RESET_ALL}"
        else:
            status = f"{Fore.RED} Pendente {Style.RESET_ALL}"
        
        print (f"{id:<5} {tarefa:<30} {status}")
    
    print ('-'*50)


def modificar_tarefa():
    listar_tarefas()
    id_escolhido = int(input('Escolha o ID para modificar: '))
    tarefa_nova = input ('Digite a nova tarefa: ')
    cursor.execute ('UPDATE tarefas SET  tarefa = ? WHERE id = ?', (tarefa_nova, id_escolhido))
    conexao.commit()

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