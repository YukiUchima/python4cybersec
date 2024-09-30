# Making api requests
import requests # $pip3 install requests
import json

# ------------------------------------ SIMPLE API ------------------------------------
# api_url = 'https://api.chucknorris.io/jokes/random'
# res = requests.get(api_url)     # get response from joke site
# # get json format
# res = res.json()
# punchline = res['value']
# print(f'Here is the joke: {punchline}')

# ------------------------------------ COMPLEX API ------------------------------------
# https://www.cocktaildb.com/api.php
# Shows a cocktail depending on parameters
base_url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s='
query = input('Enter a drink to search  ')

r = requests.get(f'{base_url}{query}')

result = r.json()['drinks']
instructions = result[0]['strInstructions']
print(f'Instructions: {instructions}')





