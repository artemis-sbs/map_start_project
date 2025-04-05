from sbs_utils.procedural.prefab import prefab_spawn

def enemy_fleets_arvonian_01(OFFSET_X=0, OFFSET_Z=0):
    map_data = [{'label': 'prefab_fleet_raider', 'data': {'fleet_difficulty': 0, 'race': 'arvonian', 'ship_roles': 'raider', 'START_X': 171863.0, 'START_Y': 0, 'START_Z': -134500.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'Fleet'}}, {'label': 'prefab_fleet_raider', 'data': {'fleet_difficulty': 0, 'race': 'arvonian', 'ship_roles': 'raider', 'START_X': 175675.0, 'START_Y': 0, 'START_Z': -133738.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'Fleet'}}, {'label': 'prefab_fleet_raider', 'data': {'fleet_difficulty': 0, 'race': 'arvonian', 'ship_roles': 'raider', 'START_X': 173900.0, 'START_Y': 0, 'START_Z': -135550.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'Fleet'}}]
    for p in map_data:
        prefab_spawn(p['label'], p['data'], OFFSET_X, OFFSET_Z )
def enemy_fleets_arvonian_02(OFFSET_X=0, OFFSET_Z=0):
    map_data = [{'label': 'prefab_fleet_raider', 'data': {'fleet_difficulty': 0, 'race': 'arvonian', 'ship_roles': 'raider', 'START_X': 42250.0, 'START_Y': 0, 'START_Z': -31287.5, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'Fleet'}}, {'label': 'prefab_fleet_raider', 'data': {'fleet_difficulty': 0, 'race': 'arvonian', 'ship_roles': 'raider', 'START_X': 40512.5, 'START_Y': 0, 'START_Z': -29650.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'Fleet'}}, {'label': 'prefab_fleet_raider', 'data': {'fleet_difficulty': 0, 'race': 'arvonian', 'ship_roles': 'raider', 'START_X': 40187.5, 'START_Y': 0, 'START_Z': -33175.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'Fleet'}}, {'label': 'prefab_fleet_raider', 'data': {'fleet_difficulty': 0, 'race': 'arvonian', 'ship_roles': 'raider', 'START_X': 37812.5, 'START_Y': 0, 'START_Z': -31075.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'Fleet'}}]
    for p in map_data:
        prefab_spawn(p['label'], p['data'], OFFSET_X, OFFSET_Z )
def enemy_arvonian_stations(OFFSET_X=0, OFFSET_Z=0):
    map_data = [{'label': 'prefab_station_arvonian', 'data': {'side_value': 'arvonian', 'roles_value': 'raider,station', 'START_X': 40000.0, 'START_Y': 0, 'START_Z': -31200.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'SA ##'}}, {'label': 'prefab_station_arvonian', 'data': {'side_value': 'arvonian', 'roles_value': 'raider,station', 'START_X': 173600.0, 'START_Y': 0, 'START_Z': -133600.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'SA ##'}}, {'label': 'trigger_rect', 'data': {'end_on_ennter': True, 'trigger_label': 'trigger_enemy_fleets_arvonian_01', 'trigger_roles': '__player__', 'START_X': 128921.0, 'START_Y': 0, 'START_Z': -95139.4, 'SIZE_X': 99878.8, 'SIZE_Y': 0, 'SIZE_Z': -81260.6, 'NAME': 'Arvonian fleet Spwan trigger'}}, {'label': 'trigger_rect', 'data': {'end_on_ennter': True, 'trigger_label': 'trigger_enemy_fleets_arvonian_02', 'trigger_roles': '__player__', 'START_X': 121.212, 'START_Y': 0, 'START_Z': -10739.400000000001, 'SIZE_X': 99878.8, 'SIZE_Y': 0, 'SIZE_Z': -81260.6, 'NAME': 'Arvonian fleet Spwan trigger'}}, {'label': 'prefab_station_civil', 'data': {'side_value': 'tsn', 'START_X': 218800.0, 'START_Y': 0, 'START_Z': -190400.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'DS ##'}}]
    for p in map_data:
        prefab_spawn(p['label'], p['data'], OFFSET_X, OFFSET_Z )
def quad_one(OFFSET_X=0, OFFSET_Z=0):
    map_data = [{'label': 'prefab_terrain_asteroid_box', 'data': {'START_X': 260150.0, 'START_Y': 0, 'START_Z': -269700.0, 'SIZE_X': 5950.0, 'SIZE_Y': 0, 'SIZE_Z': -5100.0, 'NAME': 'Asteroid Box'}}, {'label': 'prefab_terrain_nebula_box', 'data': {'START_X': 242400.0, 'START_Y': 0, 'START_Z': -269550.0, 'SIZE_X': 5100.0, 'SIZE_Y': 0, 'SIZE_Z': -4350.0, 'NAME': 'nebula'}}, {'label': 'prefab_terrain_nebula_box', 'data': {'START_X': 244750.0, 'START_Y': 0, 'START_Z': -264900.0, 'SIZE_X': 3800.0, 'SIZE_Y': 0, 'SIZE_Z': -3200.0, 'NAME': 'nebula'}}, {'label': 'prefab_terrain_asteroid_box', 'data': {'START_X': 253825.0, 'START_Y': 0, 'START_Z': -276150.0, 'SIZE_X': 6100.0, 'SIZE_Y': 0, 'SIZE_Z': -4900.0, 'NAME': 'Asteroid Box'}}, {'label': 'prefab_station_command', 'data': {'side': 'tsn', 'START_X': 250400.0, 'START_Y': 0, 'START_Z': -270400.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'DS ##'}}, {'label': 'prefab_fleet_raider', 'data': {'fleet_difficulty': 0, 'race': 'kralien', 'ship_roles': 'raider', 'START_X': 238661.0, 'START_Y': 0, 'START_Z': -271941.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'Fleet'}}, {'label': 'prefab_station_torgoth', 'data': {'side_value': 'torgoth', 'roles_value': 'raider,station', 'START_X': 240383.0, 'START_Y': 0, 'START_Z': -273933.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'DS ##'}}, {'label': 'prefab_typhon_classic', 'data': {'START_X': 259215.0, 'START_Y': 0, 'START_Z': -271136.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'Typhon'}}, {'label': 'prefab_station_kralien', 'data': {'side_value': 'kralien', 'roles_value': 'raider,station', 'START_X': 240100.0, 'START_Y': 0, 'START_Z': -266550.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'DS ##'}}, {'label': 'prefab_station_arvonian', 'data': {'side_value': 'arvonian', 'roles_value': 'raider,station', 'START_X': 239850.0, 'START_Y': 0, 'START_Z': -269950.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'DS ##'}}, {'label': 'prefab_station_civil', 'data': {'side_value': 'tsn', 'START_X': 243950.0, 'START_Y': 0, 'START_Z': -263550.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'DS ##'}}, {'label': 'prefab_station_science', 'data': {'side_value': 'tsn', 'START_X': 248200.0, 'START_Y': 0, 'START_Z': -263550.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'DS ##'}}, {'label': 'prefab_station_industry', 'data': {'side_value': 'tsn', 'START_X': 246400.0, 'START_Y': 0, 'START_Z': -263300.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'DS ##'}}, {'label': 'prefab_station_command', 'data': {'side': 'tsn', 'START_X': 0.0, 'START_Y': 0, 'START_Z': -250000.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'DS ##'}}, {'label': 'prefab_station_industry', 'data': {'side_value': 'tsn', 'START_X': 500000.0, 'START_Y': 0, 'START_Z': -250000.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'DS ##'}}, {'label': 'prefab_station_science', 'data': {'side_value': 'tsn', 'START_X': 250000.0, 'START_Y': 0, 'START_Z': -0.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'DS ##'}}, {'label': 'prefab_station_civil', 'data': {'side_value': 'tsn', 'START_X': 252000.0, 'START_Y': 0, 'START_Z': -500000.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': 'DS ##'}}, {'label': 'prefab_terrain_asteroid_polyline', 'data': {'points': [(8300.0, -5250.0), (18250.0, -11950.0), (26050.0, -9550.0), (18350.0, -9100.0), (12400.0, -2300.0), (8600.0, -12450.0)], 'is_polyline': True, 'START_X': 232400.0, 'START_Y': 0, 'START_Z': -260800.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': -0.0, 'NAME': None}}]
    for p in map_data:
        prefab_spawn(p['label'], p['data'], OFFSET_X, OFFSET_Z )
