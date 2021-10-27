import requests
import pprint
import time

########## API PARAMETERS ##########

url = 'https://rickandmortyapi.com/api'
endpointCharacter = '/character'

########## API RESPONSE VARIABLES ##########

userResponse = ''

characterNameList = []
characterInfoList = []

########## FETCH DATA FUNCTION ##########

def fetchData(url, listName, data=''): #Function parameters --> url: API url, listName: list to append the results, data: specific data to append from results being nothing by default
    print('Fetching data...\n') #Status control message

    response = requests.get(url).json() #response from API

    if not response.get('error'): #If everything is correct calling the API
        if response.get('results'): #If 'results' exist means the response from the API is character's name list
            for item in response.get('results'):
                listName.append(item.get(data)) #Apped data to the list
            
            if response.get('info').get('next'): #As the API respond is paginated, if there is another page
                fetchData(response.get('info').get('next'), listName, data) #Call fetchData again with new function parameters --> new page url, same list name to apped the data, and the specific data to append
        
        else: #If 'results' does not exist means the response from the API is a specific character info
            characterInfoList.append({ #Apped data to the list
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
        if not characterNameList: #If characterNameList list is empty
            fetchData(url + endpointCharacter, characterNameList, 'name') #Call API fetchData with --> API url with characters endpoint, characterNameList to apped the data, and 'name' to append

        for i in range(len(characterNameList)):
            print(i + 1, '-', characterNameList[i]) #print characterNameList with his identificator
    
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

            if not characterInfoList: #If characterInfoList list is empty
                fetchData(url + endpointCharacter + '/' + userResponse, characterInfoList) #Call API fetchData with --> API url with the character id, characterInfoList and to apped the data

                if characterInfoList[0]['name']: print('\nName: ' + characterInfoList[0]['name'], end='') #If Character parameter exists, print it
                if characterInfoList[0]['status']: print('\nStatus: ' + characterInfoList[0]['status'], end='')
                if characterInfoList[0]['species']: print('\nSpecies: ' + characterInfoList[0]['species'], end='')
                if characterInfoList[0]['type']: print('\nType: ' + characterInfoList[0]['type'], end='')
                if characterInfoList[0]['gender']: print('\nGender: ' + characterInfoList[0]['gender'], end='')
                if characterInfoList[0]['origin']: print('\nOrigin: ' + characterInfoList[0]['origin'], end='')
                if characterInfoList[0]['location']: print('\nLocation: ' + characterInfoList[0]['location'])
            
            else: #If characterInfoList is not empty
                characterExist = False #Flag to see if character where already searched

                for item in characterInfoList:
                    if str(item['id']) == userResponse:
                        characterExist = True #Character already searched

                        if item['name']: print('\nName: ' + item['name'], end='') #If Character parameter exists, print it
                        if item['status']: print('\nStatus: ' + item['status'], end='')
                        if item['species']: print('\nSpecies: ' + item['species'], end='')
                        if item['type']: print('\nType: ' + item['type'], end='')
                        if item['gender']: print('\nGender: ' + item['gender'], end='')
                        if item['origin']: print('\nOrigin: ' + item['origin'], end='')
                        if item['location']: print('\nLocation: ' + item['location'])

                if not characterExist: #Character already searched
                    fetchData(url + endpointCharacter + '/' + userResponse, characterInfoList) #Call API to get character info
                    
                    if item['name']: print('\nName: ' + characterInfoList[len(characterInfoList) - 1]['name'], end='') #If Character parameter exists, print it
                    if item['status']: print('\nStatus: ' + characterInfoList[len(characterInfoList) - 1]['status'], end='')
                    if item['species']: print('\nSpecies: ' + characterInfoList[len(characterInfoList) - 1]['species'], end='')
                    if item['type']: print('\nType: ' + characterInfoList[len(characterInfoList) - 1]['type'], end='')
                    if item['gender']: print('\nGender: ' + characterInfoList[len(characterInfoList) - 1]['gender'], end='')
                    if item['origin']: print('\nOrigin: ' + characterInfoList[len(characterInfoList) - 1]['origin'], end='')
                    if item['location']: print('\nLocation: ' + characterInfoList[len(characterInfoList) - 1]['location'])
                    
        elif userResponse == '2': #Back to menu
            pass

        else: #Introduce a valid option
            print('Introduce a valid option')

    #_________ OPTION 5 - EXIT PROGRAM _________#

    elif userResponse == '5':
        print('\nGoodbye\n')

    else:
        print('Introduce a valid option')