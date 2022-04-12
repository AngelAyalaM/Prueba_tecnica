import requests, re

def nombre_con_A():
    request = requests.get('https://pokeapi.co/api/v2/pokemon?offset=0&limit=1200')
    data = request.json()
    count = 0
    for element in data["results"]:
        if element["name"].count('a') == 2 and re.findall(r'at', element["name"]):
            count += 1
    return count 

