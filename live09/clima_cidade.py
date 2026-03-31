import requests

def consulta_clima(cidade):
    end_point = 'https://geocoding-api.open-meteo.com/v1/search'

    response = requests.get(end_point, {'name':  cidade, 'count': 1})

    data = response.json()

    print (data)

cidade = input ('Digite o nome de uma cidade: ')

info = consulta_clima(cidade)