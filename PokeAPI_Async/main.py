import pokeDatabaseSDK as pdb


menuResponse = '' #Variable to manage user response in the menu

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
        pdb.pokemonNames()
        
    #_________ OPTION 2 - REQUEST FOR POKEMON GAMES NAMES _________#
    
    elif menuResponse == '2':
        pdb.gameNames()

    #_________ OPTION 3 - CHECK REQUESTS LISTS _________#

    elif menuResponse == '3':
        pdb.requestsList()

    #_________ OPTION 4 - EXIT PROGRAM _________#

    elif menuResponse == '4':
        print('\nGoodbye\n')

    else:
        print('Introduce a valid option')