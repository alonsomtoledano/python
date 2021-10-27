import requests
import pprint
import time

########## API PARAMETERS ##########

url = 'https://rickandmortyapi.com/api'
endpointCharacter = '/character'

########## API RESPONSE VARIABLES ##########

userResponse = ''

characterList = [] #List to append character info
allCharacterInfo = False #Contol variable to detect if all character info are gathered

########## FETCH DATA FUNCTION ##########

def fetchData(url, listName): #Function parameters --> url: API url, listName: list to append the results
    print('Fetching data...\n') #Status control message

    response = requests.get(url).json() #Response from API

    if not response.get('error'): #If everything is correct calling the API
        if response.get('results'): #If 'results' exist means the response from the API is all character's list
            for item in response.get('results'):
                listName.append({ #Apped data to the list
                    'id': item.get('id'),
                    'name': item.get('name')
                })
            
            if response.get('info').get('next'): #As the API respond is paginated, if there is another page
                fetchData(response.get('info').get('next'), listName) #Call fetchData again with new function parameters --> new page url, and same list name to apped the data
        
        else: #If 'results' does not exist means the response from the API is a specific character info
            characterList.append({ #Apped data to the list
                'id': response.get('id'),
                'name': response.get('name'),
                'status': response.get('status'),
                'species': response.get('species'),
                'type': response.get('type'),
                'gender': response.get('gender'),
                'origin': response.get('origin').get('name'),
                'location': response.get('location').get('name')
            })

    else: #If something goes wrong vaalling the API
        print('\n' + response.get('error') + ', please try again' + '\n') #Print the error message


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
        if not characterList: #If characterList list is empty
            fetchData(url + endpointCharacter, characterList) #Call API fetchData with --> API url with characters endpoint, and characterList to apped the data
        
        elif characterList and not allCharacterInfo: #characterList is not empty and all characters are not gathered
            characterList.clear() #Restore list

            fetchData(url + endpointCharacter, characterList) #Call API fetchData with --> API url with characters endpoint, and characterList to apped the data

        allCharacterInfo = True #All character info are gathered

        for i in range(len(characterList)):
            print(characterList[i].get('id'), '-', characterList[i].get('name')) #print characterNameList with his identificator
        
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

            if not characterList: #If characterList list is empty
                fetchData(url + endpointCharacter + '/' + userResponse, characterList) #Call API fetchData with --> API url with the character id, and characterList to apped the data

                if characterList[0]['name']: print('\nName: ' + characterList[0]['name'], end='') #If Character parameter exists, print it
                if characterList[0]['status']: print('\nStatus: ' + characterList[0]['status'], end='')
                if characterList[0]['species']: print('\nSpecies: ' + characterList[0]['species'], end='')
                if characterList[0]['type']: print('\nType: ' + characterList[0]['type'], end='')
                if characterList[0]['gender']: print('\nGender: ' + characterList[0]['gender'], end='')
                if characterList[0]['origin']: print('\nOrigin: ' + characterList[0]['origin'], end='')
                if characterList[0]['location']: print('\nLocation: ' + characterList[0]['location'])
            
            else: #If characterList is not empty
                if allCharacterInfo: #All character info are already gathered
                    break #ya esta toda la lista, por lo que hay que buscar en ella

                else: #All character info are not gathered
                    characterExist = False #Flag to see if character where already searched

                    for item in characterList: #Search character in the list
                        if str(item['id']) == userResponse:
                            characterExist = True #Character already searched

                            if item['name']: print('\nName: ' + item['name'], end='') #If Character parameter exists, print it
                            if item['status']: print('\nStatus: ' + item['status'], end='')
                            if item['species']: print('\nSpecies: ' + item['species'], end='')
                            if item['type']: print('\nType: ' + item['type'], end='')
                            if item['gender']: print('\nGender: ' + item['gender'], end='')
                            if item['origin']: print('\nOrigin: ' + item['origin'], end='')
                            if item['location']: print('\nLocation: ' + item['location'])

                    if not characterExist: #Character is not in the list
                        fetchData(url + endpointCharacter + '/' + userResponse, characterList) #Call API fetchData with --> API url with the character id, and characterInfoList to apped the data
                        
                        if characterList[len(characterList) - 1]['name']: print('\nName: ' + characterList[len(characterList) - 1]['name'], end='') #If Character parameter exists, print it
                        if characterList[len(characterList) - 1]['status']: print('\nStatus: ' + characterList[len(characterList) - 1]['status'], end='')
                        if characterList[len(characterList) - 1]['species']: print('\nSpecies: ' + characterList[len(characterList) - 1]['species'], end='')
                        if characterList[len(characterList) - 1]['type']: print('\nType: ' + characterList[len(characterList) - 1]['type'], end='')
                        if characterList[len(characterList) - 1]['gender']: print('\nGender: ' + characterList[len(characterList) - 1]['gender'], end='')
                        if characterList[len(characterList) - 1]['origin']: print('\nOrigin: ' + characterList[len(characterList) - 1]['origin'], end='')
                        if characterList[len(characterList) - 1]['location']: print('\nLocation: ' + characterList[len(characterList) - 1]['location'])
                    
        elif userResponse == '2': #Back to menu
            pass

        else: #Introduce a valid option
            print('Introduce a valid option')

    #_________ OPTION 5 - EXIT PROGRAM _________#

    elif userResponse == '5':
        print('\nGoodbye\n')

    else:
        print('Introduce a valid option')