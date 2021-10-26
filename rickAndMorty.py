import requests
import pprint

url = 'https://rickandmortyapi.com/api'
endpointCharacter = '/character'

userResponse = ''

characterNameList = []

def fetchData(url, listName, data):
    print('Fetching data...\n')

    response = requests.get(url).json()

    for item in response.get('results'):
            listName.append(item.get(data))
    
    if response.get('info').get('next'):
        fetchData(response.get('info').get('next'), listName, data)


print('\nWelcome to the Rick & Morty knoledge database.')

while userResponse != '5':
    print('''What do you want to do?

[1] List all characters
[5] Exit
''')
    userResponse = input()

    if userResponse == '1':
        if not characterNameList:
            responseCharacter = fetchData(url + endpointCharacter, characterNameList, 'name')

        for i in range(len(characterNameList)):
            print(i + 1, '-', characterNameList[i])

print('\nGoodbye')