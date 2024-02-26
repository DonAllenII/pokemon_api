import requests, json
import random


#assign pokemon_api variable to url of complete pokemon_list
url = 'https://pokeapi.co/api/v2/pokemon/'

limits ='?limit=151'
offsets = '&offset=0'



#url
poke_url = 'https://pokeapi.co/api/v2/pokemon/'


#given a url as an input, connect to api & return data in json format
def get_data(url, string = '', limit = 151, offset = 0):
    if string != '':
        url += string + '/'
    else:
        url += f'?limit={limit}&offset={offset}'
    response = requests.get(url)
    return response.json()


pokedex = get_data(url)
pokemon_stats = get_data(url, 'moltres')


#print(pokedex)
#print(pokemon_stats)
print(pokemon_stats['types'])
print(pokemon_stats['weight'])
print(pokemon_stats['abilities'])
#print(pokedex['results'])

output = []

for pokemon in pokedex['results']:
    output.append(pokemon['name'])

#for i,  pokemon in enumerate(pokedex['results']):
    #print(pokemon['name'], i+1)


#random.randint(0, )


#define using pokemon_api, pokemon as inputs; use string concat and variable to ouput url for a specific pokemon
#def poke_name_url(url, pokemon_name):
 #   return f'url' + str(pokemon_name)

#def using pokemon_api as an input, retrieve  of all pokemon names from pokemon_api using limiters, outputs a list pokemon_names
    #define pokemon_api url for all pokemon

#for pokemon in pokedex:
 #   list.append()
#def retrieve type, name, abilities, weight

#def using pokemon_names as an input; 20 as default input of amount of pokemon names returned,  return a list of 20 pokemon names
def random_poke_list(list, no_of_poke = 20):
    poke_list = []
    i=0
    while i < no_of_poke:
        current = list[random.randint(0, len(list))]
        poke_list.append(current)
        i += 1

    return poke_list

print(random_poke_list(output))
      #  poke_list = [x for x in range(0, no_of_poke -1)]


#create a dictionary of pokemon by type: {name:  {ablities: [], weight:}