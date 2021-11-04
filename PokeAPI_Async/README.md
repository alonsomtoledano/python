#  🔴 PokeAPI_Async
## 📝 Table of contents

- Introduction
- pokeDatabase<!---->.py
- pokeDatabaseSDK<!---->.py
- main<!---->.py

## 📔 Introduction

Acquisition of data from Pokemon games through asynchronous requests to [PokeAPI](https://pokeapi.co/).

## ◼️ pokeDatabase<!---->.py

Project with a menu where there are four options:
- Request for pokemon names: shows all the pokemon names and store them in a list
- Request for pokemon games names: shows all the pokemon game names and store them in a list
- Check requests lists: checks if there is data in the two different lists
- Exit: Exit the program

## ◼️ pokeDatabaseSDK<!---->.py

SDK based on the previous program where the main functions are encapsulated and can be used as a library. These are:

```py
pokemonNames()
```

```py
gameNames()
```

```py
requestsList()
```

## ◼️ main<!---->.py
Program where the library developed in the previous projects is used as follows:

```py
import pokeDatabaseSDK as pdb
```

Being able to access its functions in the following way:

```py
pdb.pokemonNames()
```

```py
pdb.gameNames()
```

```py
pdb.requestsList()
```