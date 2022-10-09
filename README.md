# Brawl-Stars-API

## Introduction
Brawl Stars client based on official Brawl Stars API

## Installation
`pip install ` for the stable version

## Examples

### Getting Started
```py
import brawlstars

token = "your token goes here" # You can create your token in: https://developer.brawlstars.com/#/getting-started
client = brawlstars.Client(token)

player1 = client.get_player("88QRYCJRG")
club1 = client.get_club("2LVRYU29C")

print(player1.get_info())
print(club1.get_info())

```
