import requests
import pprint
import time

########## API PARAMETERS ##########

url = 'https://rickandmortyapi.com/api'
endpointCharacter = '/character'

########## API RESPONSE VARIABLES ##########

userResponse = ''

characterNameList = []
characterInfo = []

########## FETCH DATA FUNCTION ##########

def fetchData(url, listName, data=''):
    print('Fetching data...\n')

    response = requests.get(url).json()

    if not response.get('error'):
        if response.get('results'):
            for item in response.get('results'):
                listName.append(item.get(data))
            
            if response.get('info').get('next'):
                fetchData(response.get('info').get('next'), listName, data)
        
        else:
            characterInfo.append({
                'id': response.get('id'),
                'name': response.get('name'),
                'status': response.get('status'),
                'species': response.get('species'),
                'type': response.get('type'),
                'gender': response.get('gender'),
                'origin': response.get('origin').get('name'),
                'location': response.get('location').get('name')
            })

    else:
        print('\n' + response.get("error") + ', please try again' + '\n')


########## MAIN PROGRAM ##########

print('\nWelcome to the Rick & Morty knoledge database')

while userResponse != '5': #Menu loop
    print('''
What do you want to do?

[1] List all characters
[2] Show character info
[5] Exit
''')

    userResponse = input()

    #_________ OPTION 1 - LIST ALL CHARACTERS _________#

    if userResponse == '1':
        if not characterNameList:
            fetchData(url + endpointCharacter, characterNameList, 'name')

        for i in range(len(characterNameList)):
            print(i + 1, '-', characterNameList[i])
    
    #_________ OPTION 2 - SHOW CHARACTER INFO _________#
    
    elif userResponse == '2':
        
        print('''
Choose a character by his identification number shown in [1] List all characters.

[1] Introduce an identificator
[2] Back to menu
''')
        userResponse = input()

        if userResponse == '1': #Introduce an identificator

            print('\nIdentificator: ', end='')

            userResponse = input()

            if not characterInfo:
                fetchData(url + endpointCharacter + '/' + userResponse, characterInfo)

                if characterInfo[0]['name']: print('\nName: ' + characterInfo[0]['name'], end='')
                if characterInfo[0]['status']: print('\nStatus: ' + characterInfo[0]['status'], end='')
                if characterInfo[0]['species']: print('\nSpecies: ' + characterInfo[0]['species'], end='')
                if characterInfo[0]['type']: print('\nType: ' + characterInfo[0]['type'], end='')
                if characterInfo[0]['gender']: print('\nGender: ' + characterInfo[0]['gender'], end='')
                if characterInfo[0]['origin']: print('\nOrigin: ' + characterInfo[0]['origin'], end='')
                if characterInfo[0]['location']: print('\nLocation: ' + characterInfo[0]['location'])
            
            else:
                characterExist = False

                for item in characterInfo:
                    if str(item['id']) == userResponse:
                        characterExist = True

                        if item['name']: print('\nName: ' + item['name'], end='')
                        if item['status']: print('\nStatus: ' + item['status'], end='')
                        if item['species']: print('\nSpecies: ' + item['species'], end='')
                        if item['type']: print('\nType: ' + item['type'], end='')
                        if item['gender']: print('\nGender: ' + item['gender'], end='')
                        if item['origin']: print('\nOrigin: ' + item['origin'], end='')
                        if item['location']: print('\nLocation: ' + item['location'])

                if not characterExist:
                    fetchData(url + endpointCharacter + '/' + userResponse, characterInfo)
                    
                    if item['name']: print('\nName: ' + characterInfo[len(characterInfo) - 1]['name'], end='')
                    if item['status']: print('\nStatus: ' + characterInfo[len(characterInfo) - 1]['status'], end='')
                    if item['species']: print('\nSpecies: ' + characterInfo[len(characterInfo) - 1]['species'], end='')
                    if item['type']: print('\nType: ' + characterInfo[len(characterInfo) - 1]['type'], end='')
                    if item['gender']: print('\nGender: ' + characterInfo[len(characterInfo) - 1]['gender'], end='')
                    if item['origin']: print('\nOrigin: ' + characterInfo[len(characterInfo) - 1]['origin'], end='')
                    if item['location']: print('\nLocation: ' + characterInfo[len(characterInfo) - 1]['location'])
                    

            #for k, v in characterInfo[0].items():
            #    print(v)

            #print(characterInfo)

            


        elif userResponse == '2': #Back to menu
            pass

        else: #Introduce a valid option
            print('Introduce a valid option')

    #_________ OPTION 5 - EXIT PROGRAM _________#

    elif userResponse == '5':
        print('\nGoodbye\n')

    else:
        print('Introduce a valid option')