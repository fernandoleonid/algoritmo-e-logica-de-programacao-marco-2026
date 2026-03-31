import requests

def consultar_cep (cep):
    end_point = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(end_point)

    if response.status_code == 200:
        data = response.json()
        if 'erro' not in data:
            return data
        else:
            return {'erro': 'CEP não encontrado'}
    else:
        return {'erro': 'Erro de solicitação'}


cep = input ('Digite um cep para pesquisar: ')
info = consultar_cep(cep)

print ('*'*30)
print (f'CEP: {info["cep"]}')
print (f'Localidade: {info["localidade"]}' )
print (f'UF: {info["uf"]}')