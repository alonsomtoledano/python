import requests
import time
import random
import pprint

########## API PARAMETERS ##########

url = 'https://pokeapi.co/api/v2/'
endpointPokedex = 'pokedex/1/'
endpointGames = 'generation/'

########## API RESPONSE VARIABLES ##########

menuResponse = '' #Variable to manage user response in the menu

pokemonList = [] #List to save pokemon names from the pokedex
gamesList = [] #List to save pokemon games names

########## FETCH DATA FUNCTION ##########

def fetchData(url, listName, option, waitTime):
    response = requests.get(url).json()

    if not response.get('error'):
        if not option:
            for item in response.get('pokemon_entries'):
                listName.append(item.get('pokemon_species').get('name'))
            
            time.sleep(waitTime)
            print('\nPokemon names fetched')

        else:
            numberOfGenerations = requests.get(url).json().get('count')

            for generationNumber in range(1, numberOfGenerations + 1):
                games = requests.get(url + str(generationNumber)).json().get('version_groups')

                for gameName in games:
                    gamesList.append(gameName.get('name'))

            time.sleep(waitTime)
            print('\nPokemon games fetched')

    else: #If something goes wrong
        print('\n' + response.get('error') + ', please try again' + '\n') #Print the error message




########## MAIN PROGRAM ##########

print('\nWelcome to the Pokemon knoledge database')

while menuResponse != '4': #Menu loop
    print('''
What do you want to do?

[1] Request for pokemon names
[2] Request for pokemon games names
[3] Check requests lists
[4] Exit
''')

    menuResponse = input()

    #_________ OPTION 1 - REQUEST FOR POKEMON NAMES _________#

    if menuResponse == '1':
        print('\nAsking for Pokemon List')

        waitTime = random.randint(5, 10)

        print('\nIt will be available in ' + str(waitTime) + ' seconds approximately')

        fetchData(url + endpointPokedex, pokemonList, False, waitTime)
        
    #_________ OPTION 2 - REQUEST FOR POKEMON GAMES NAMES _________#
    
    elif menuResponse == '2':
        print('\nAsking for Pokemon Games List')

        waitTime = random.randint(5, 10)

        print('\nIt will be available in ' + str(waitTime) + ' seconds approximately')

        fetchData(url + endpointGames, gamesList, True, waitTime)

    #_________ OPTION 3 - CHECK REQUESTS LISTS _________#

    elif menuResponse == '3':
        print('\nPokemon names: ' + str(pokemonList))
        print('\nPokemon games names: ' + str(gamesList))

    #_________ OPTION 4 - EXIT PROGRAM _________#

    elif menuResponse == '4':
        print('\nGoodbye\n')

    else:
        print('Introduce a valid option')