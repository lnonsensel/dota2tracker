import requests
import json 

base_url = 'https://www.dota2protracker.com/hero'
with open('heroes_changed.json') as file:
    heroes = json.load(file)

heroes = heroes['heroes']
for i in heroes.values():
    code = requests.get(f'{base_url}/{i}').status_code
    if code != 200:
        print(code, i)
    break
