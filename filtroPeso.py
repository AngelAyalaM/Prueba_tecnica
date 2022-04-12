import  requests

def regresa_request(url):
    request_ground = requests.get(url)
    return request_ground.json()

def max_min(elemento1, elemento2):
    lista_peso = []
    for p in elemento1:
        for p2 in elemento2:
            if p["name"] == p2["name"]:
                resultado = regresa_request (p["url"])
                lista_peso.append(resultado["weight"])
    return([max(lista_peso)], [min(lista_peso)])

def peso_fighting_genracion1():
    data_type = regresa_request("https://pokeapi.co/api/v2/type/fighting/")
    data_generacion = regresa_request("https://pokeapi.co/api/v2/generation/1/")
    data_type = data_type["pokemon"]
    peso_fighting = []
    for p in data_type:
        lista_string = p["pokemon"]["url"].split('/')
        if int(lista_string[6]) <= 151:
            peso_fighting.append(p["pokemon"])
    return max_min(peso_fighting, data_generacion["pokemon_species"])

   
 