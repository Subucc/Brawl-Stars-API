# Brawl-Stars-API

## Introduction
Brawl Stars client based on official Brawl Stars API

## Installation
`pip install`  for the stable version

## Examples

### Getting Started
```py
import brawlstars

token = "YOUR TOKEN" # You can create your token in: https://developer.brawlstars.com/#/getting-started
client = brawlstars.Client(token)

player1 = client.get_player("PLAYER TAG")
club1 = client.get_club("CLUB TAG")

print(player1.get_info())
print(club1.get_info())

```
### Getting Specific Informations
```py

player1_info = player1.get_info()
print(player1_info['trophies'])

>> 10000
```

### Example of printing all brawlers
```py

player1_info = player1.get_info()
for brawler in player1_info['brawlers']:
    print("Brawler name: " + brawler['name'] + " | Trophies: " + str(brawler['trophies']))

>> Brawler name: SHELLY | Trophies: 500
>> Brawler name: COLT | Trophies: 359
>> Brawler name: BULL | Trophies: 438
>> Brawler name: BROCK | Trophies: 395

```

