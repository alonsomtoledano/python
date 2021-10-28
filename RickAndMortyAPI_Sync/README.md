#  🥒 RickAndMortyAPI_Sync
## 📝 Table of contents

- Introduction
- rickAndMorty<!---->.py
- rickAndMortySDK<!---->.py
- main<!---->.py

## 📔 Introduction

Acquisition of data from Rick and Morty characters through synchronous requests to the [Rick and Morty API](https://rickandmortyapi.com/)

## ◼️ rickAndMorty<!---->.py

Project with a menu where there are four options:
- List all characters: shows the names of all the characters and their identifier
- Show character info: by entering the identifier of a character, it shows the following information:
  - Name
  - Status
  - Species
  - Type
  - Gender
  - Origin
  - Location
 - Clear memory: all values ​​are stored in memory to make the least possible requests to the API to speed up the use of the application. This option clears the memory to collect the information again
 - Exit: Exit the program

## ◼️ rickAndMortySDK<!---->.py

SDK based on the previous program where the main functions are encapsulated and can be used as a library. These are:

```py
listAllCharacters()
```

```py
showCharacterInfo(id)
```

## ◼️ main<!---->.py
Program where the library developed in the previous projects is used as follows:

```py
import rickAndMortySDK as rams
```

Being able to access its functions in the following way:

```py
rams.listAllCharacters()
```

```py
rams.showCharacterInfo(id)
```