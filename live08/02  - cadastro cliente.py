import os
import sqlite3

from colorama import Fore, Style, init
init ()

conexao = sqlite3.connect('./Live_08/clientes.db')
cursor=conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        nome  TEXT,
        celular  TEXT,
        cidade   TEXT
    )
''')
conexao.commit()


def cadastrar_cliente():
    nome = input ('Digite seu nome: ')
    celular = input ('Digite seu celular: ')
    cidade = input ('Digite sua cidade: ')

    cursor.execute('INSERT INTO clientes (nome, celular, cidade) VALUES (?, ?, ?)',(nome, celular, cidade))
    conexao.commit()

def listar_cliente():
    limpar_tela()
    cursor.execute('SELECT * FROM clientes')
    conexao.commit()
    clientes = cursor.fetchall()
    print (f"{'ID':<5} {'NOME DO CLIENTE':<30} {'CELULAR':<10} {'CIDADE':<20}")
    print ('-'*50)
    
    for item in clientes:
        id, nome, celular, cidade = item
        print (f"{id:<5} {nome:<30} {celular:<10} {cidade}")

    print ('-'*50)
