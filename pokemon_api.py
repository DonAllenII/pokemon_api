import requests, json
import random
import time


#assign pokemon_api variable to url of complete pokemon_list
url = 'https://pokeapi.co/api/v2/'

limits ='?limit=151'
offsets = '&offset=0'
pokemon = 'pokemon'



#url
poke_url = 'https://pokeapi.co/api/v2/pokemon/'


#given a url as an input, connect to api & return data in json format
def get_data(url, string = '', limit = 151, offset = 0):
    if string == 'type':
        url += string + '/'
    elif string != '':
        url += 'pokemon/' + string
    else:
        url += f'pokemon/?limit={limit}&offset={offset}'
    response = requests.get(url)
    return response.json()


poke_data = get_data(url)
#print(poke_data)
#print(poke_data['results'])

#given pokemon name as inputs connect to api & return data about that pokemon
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

########pokemon_info retrieval test#######
#print(stat_package('moltres'))
#print(stat_package('moltres')['type'])
#for type in stat_package('moltres')['type']:
#   print(stat_package('moltres')['type'][type])

#given pokemon_api data as input, return a list of pokemon
def pokedex(poke_data):
    pokedex = []
    for pokemon in poke_data['results']:
        pokedex.append(pokemon['name'])
    return pokedex

pokedex = pokedex(poke_data)
#test for pokedex variable#
#for i,  pokemon in enumerate(pokedex['results']):
    #print(pokemon['name'], i+1)


#def using pokemon_names as an input; 20 as default input of amount of pokemon names returned,  return a list of 20 pokemon names
def random_poke_list(list, no_of_poke = 20):
    poke_list = []
    i=0
    while i < no_of_poke:
        current = list[random.randint(0, len(list))]
        poke_list.append(current)
        i += 1

    return poke_list

poke_list = random_poke_list(pokedex)
#print(poke_list)
      #  poke_list = [x for x in range(0, no_of_poke -1)]
    #poke_list = [(list[random.randint(0, len(list))]) for i in enumerate(no_of_poke)]

#get attribute name for attribute in list of attributes(retrieved from api)
types = [type['name'] for type in (get_data(url, 'type'))['results']]
#print(types)



def pokemon_collection(types, poke_list):
    start = time.time()
    pokemon_collection = {}
    for type in types:
        #print(f'########{type}#######')
        for pokemon in poke_list:
            for this_pokemons_type in stat_package(pokemon)['type']:
                    
                    if type == stat_package(pokemon)['type'][this_pokemons_type]:
                        if type not in pokemon_collection.keys():
                            ability_weight = {}
                            ability_weight['abilities'] = [(stat_package(pokemon)['ability'][value]) for value in stat_package(pokemon)['ability']]
                            ability_weight['weight'] = stat_package(pokemon)['weight']
                            poke_stats = {}
                            poke_stats[stat_package(pokemon)['name']] = ability_weight
                            pokemon_collection[type] = poke_stats
                                                        
                        else:
                            ability_weight = {}
                            ability_weight['abilities'] = [(stat_package(pokemon)['ability'][value]) for value in stat_package(pokemon)['ability']]
                            ability_weight['weight'] = stat_package(pokemon)['weight']
                            pokemon_collection[type][stat_package(pokemon)['name']] = ability_weight

    end = time.time()
    #print(end - start)
    return pokemon_collection

#given a list of pokemon, create a dictionary of pokemon where the key is type
def pokemon_collection_faster(poke_list):
    start = time.time()
    pokemon_collection = {}

    for pokemon in poke_list:
        for this_pokemons_type in stat_package(pokemon)['type'].values():
                    
            if this_pokemons_type not in pokemon_collection.keys():
                ability_weight = {}
                ability_weight['abilities'] = [(stat_package(pokemon)['ability'][value]) for value in stat_package(pokemon)['ability']]
                ability_weight['weight'] = stat_package(pokemon)['weight']
                poke_stats = {}
                poke_stats[stat_package(pokemon)['name']] = ability_weight
                pokemon_collection[this_pokemons_type] = poke_stats
                                                        
            else:
                ability_weight = {}
                ability_weight['abilities'] = [(stat_package(pokemon)['ability'][value]) for value in stat_package(pokemon)['ability']]
                ability_weight['weight'] = stat_package(pokemon)['weight']
                pokemon_collection[this_pokemons_type][stat_package(pokemon)['name']] = ability_weight

    end = time.time()
    #print(end - start)
    return pokemon_collection

print(pokemon_collection_faster(poke_list))

