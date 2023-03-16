import requests
from parse_element import parse_element
import eel
import json
from random import randint
from overlay import define_label, update_label
import os
from requests.exceptions import RequestException

APP_NAME = 'protracker'


class ProtrackerNotWorking(BaseException):
    pass

def check_protracker_status_code() -> None:
    if requests.get("https://www.dota2protracker.com/").status_code != 200:
        raise ProtrackerNotWorking('dota2protracker is unavailable right now. Check your internet connection or try later.')


def get_hero_name(hero: str) -> str:

    with open("heroes.json") as file:
        heroes = json.load(file)
    
    for i in heroes:
        if i['name'] == hero:
            hero = i['name_english_loc']
            break

    hero = hero.replace(' ', '%20')
    return hero


def parse_protracker(hero):

    check_protracker_status_code()
    url = 'https://www.dota2protracker.com'
    full_url = f'{url}/hero/{hero}#'
    responce = requests.get(full_url).text
    responce = responce.replace('/static', url+'/static')
    filename = parse_element(responce, hero, APP_NAME)
    return filename

def open_window(hero):

    hero = get_hero_name(hero)
    filename = parse_protracker(hero)
    eel_filename = f'{hero}_parsed.html'

    # Using os
    file_path = os.path.abspath(filename)
    os.system(f'chrome.exe --app="{file_path}"')


    # Using eel
    # eel.init(APP_NAME)
    # eel.start(eel_filename, size = (714,709), block = False)
    # eel.sleep(1.0)




if __name__ == '__main__':
    open_window('npc_dota_hero_invoker')