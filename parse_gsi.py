import json

with open('items.json') as file:
    costs = json.load(file)

get_xpm_gpm = lambda state: map(str,[state['player']['xpm'], state['player']['gpm']])
get_time = lambda state: state['map']['clock_time']
get_items = lambda state: state['items']
get_items_cost = lambda state: sum([costs[i['name']]  if i['name'] != 'empty' else 0 for i in get_items(state).values()])
get_net_worth = lambda state: state['player']['gold'] + get_items_cost(state)
get_draft = lambda state: state['draft']
get_game_state = lambda state: state['map']['game_state']
get_win_team = lambda state: state['map']['win_team']