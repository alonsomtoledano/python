import rickAndMortySDK as rams


menuResponse = '' #Variable to manage user response in the menu

print('\nWelcome to the Rick & Morty knoledge database')

while menuResponse != '3': #Menu loop
    print('''
What do you want to do?

[1] List all characters
[2] Show character info
[3] Exit
''')

    menuResponse = input()

    #_________ OPTION 1 - LIST ALL CHARACTERS _________#

    if menuResponse == '1':
        characterList = rams.listAllCharacters()

        for i in range(len(characterList)):
            print(characterList[i].get('id'), '-', characterList[i].get('name')) #print characterNameList with his identificator
    
    #_________ OPTION 2 - SHOW CHARACTER INFO _________#

    elif menuResponse == '2':
        print('''
Choose a character by his identification number shown in [1] List all characters.

[1] Introduce an identificator
[2] Back to menu
''')
        userResponse = input()

        if userResponse == '1': #Introduce an identificator
            print('\nIdentificator: ', end='')

            id = input()

            characterInfo = rams.showCharacterInfo(id)

            if characterInfo[0]['name']: print('\nName: ' + characterInfo[0]['name'], end='') #If Character parameter exists, print it
            if characterInfo[0]['status']: print('\nStatus: ' + characterInfo[0]['status'], end='')
            if characterInfo[0]['species']: print('\nSpecies: ' + characterInfo[0]['species'], end='')
            if characterInfo[0]['type']: print('\nType: ' + characterInfo[0]['type'], end='')
            if characterInfo[0]['gender']: print('\nGender: ' + characterInfo[0]['gender'], end='')
            if characterInfo[0]['origin']: print('\nOrigin: ' + characterInfo[0]['origin'], end='')
            if characterInfo[0]['location']: print('\nLocation: ' + characterInfo[0]['location'])
            
        elif userResponse == '2': #Back to menu
            pass

        else: #Introduce a valid option
            print('Introduce a valid option')

    #_________ OPTION 4 - EXIT PROGRAM _________#

    elif menuResponse == '3':
        print('\nGoodbye\n')

    else:
        print('Introduce a valid option')