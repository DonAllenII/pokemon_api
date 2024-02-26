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

#given a url, pokemon name as inputs, connect to api & return data about that pokemon
def get_pokemon_stats(pokemon_name):
    return get_data(url, pokemon_name)

#given a pokemon_name, retrive weight, type & ability. Then return a dicitonary of info for pokemon.
def stat_package(pokemon_name):
    output = {}
    output['name'] = pokemon_name
    output['weight'] = get_pokemon_stats(pokemon_name)['weight']
    output['type'] = {}
    output['ability'] = {}

    for i, type in enumerate(get_pokemon_stats(pokemon_name)['types']):
        output['type'][i] = type['type']['name']

    for i, ability in enumerate(get_pokemon_stats(pokemon_name)['abilities']):
        output['ability'][i] = ability['ability']['name']

    return output


print(stat_package('moltres'))

#print(pokedex)
#print(pokemon_stats)
#or type in get_pokemon_stat('moltres')['types']:
    #print(type['type']['name'])
#print(get_pokemon_stats('moltres')['types'])
#print(get_pokemon_stat('moltres')['weight'])
#for ability in get_pokemon_stat('moltres')['abilities']:
    #print(ability['ability']['name'])
#print(get_pokemon_stats('moltres')['abilities'])
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