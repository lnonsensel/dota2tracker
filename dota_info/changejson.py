import re



with open('heroes.json') as file:
    filedata = file.read()

heronames = re.findall(r'npc_dota_hero_[_a-z]+', filedata)
for i in heronames:
    hero = i.split('npc_dota_hero_')[-1]
    hero = hero.split('_')
    print('%20'.join([i.capitalize() for i in hero]))
    hero = '%20'.join([i.capitalize() for i in hero])
    filedata = filedata.replace(i, f'"{i}": "{hero}",')

with open('heroes_changed.json', 'w') as file:
    file.write(filedata)