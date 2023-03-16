from server import Server
from open_protracker import open_window
from parse_gsi import  get_xpm_gpm, get_net_worth, get_time, get_items, get_draft, get_game_state, get_win_team
from overlay import define_label, update_label
import os
from utils.utils import clear_parsed_folder



clear = lambda: os.system('cls')
clear_parsed_folder()

working = False
def protracker(last_state, state):
    global working
    if not working:
        try:
            hero_full_name = state['hero']['name']
            open_window(hero_full_name)
            working = True
        except KeyError:
            pass
    else:
        pass


label = False
def gpm_xpm(last_state, state):
    global label 
    if not label:
        label = define_label()
    try:
        xpm, gpm = get_xpm_gpm(state)
        net_worth = get_net_worth(state)
        time = get_time(state)
        mins = time / 60
        update_label(label, f'gpm: {gpm}   xpm: {xpm}    net worth: {net_worth}  agpm {round(net_worth/mins)}   net_worth_2: {round(float(gpm) * mins)}')
    except KeyError:
        pass

#27 6700
#19-50 10750
#31-30 17700

if __name__ == '__main__':
    server = Server()
    server.on_update(protracker)
    server.on_update(gpm_xpm)
    server.start()