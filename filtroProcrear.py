import requests

def regresar_request(url):
    request_ground =requests.get(url)
    return request_ground.json()

def eliminar_duplicado():
    data_ground = regresar_request('https://pokeapi.co/api/v2/egg-group/5/')
    data_fairy = regresar_request('https://pokeapi.co/api/v2/egg-group/6/')
    elemento = data_ground["pokemon_species"] + data_fairy["pokemon_species"]
    lista_no_duplicado = []
    for nombre in elemento:
        if nombre not in lista_no_duplicado:
            lista_no_duplicado.append(nombre)
    return len(lista_no_duplicado)


        