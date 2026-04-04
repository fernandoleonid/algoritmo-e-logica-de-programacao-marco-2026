import requests

API_KEY = '991e9acbb22e5d90b8ba0768ae0060d6'

def consultar_filme (nome_filme):
    url = 'https://api.themoviedb.org/3/search/movie'
    response = requests.get(url, params={
        "api_key": API_KEY,
        "query": nome_filme,
        "language":  "pt-br"
    })
    data = response.json()
    return data


nome_filme = input ('Digite um nome de filme: ')


info = consultar_filme(nome_filme)

# Importa o dicionário de gêneros
from genres import GENRES

# Exibe cabeçalho
print(f'{"Nome do Filme":40} | {"Gênero":20} | {"Nota":4}')
print('-'*70)

# Percorre os resultados
for filme in info.get('results', []):
    nome = filme.get('title', 'N/A')
    generos_id = filme.get('genre_ids', [])
    # Pega o primeiro gênero, se existir
    genero = GENRES.get(generos_id[0], 'N/A') if generos_id else 'N/A'
    nota = filme.get('vote_average', 'N/A')
    print(f'{nome[:40]:40} | {genero:20} | {nota!s:4}')