from sbs_utils.procedural.prefab import prefab_spawn

def test(OFFSET_X=0, OFFSET_Z=0):
    map_data = [{'label': 'prefab_station_torgoth', 'data': {'side_value': 'torgoth', 'roles_value': 'raider,station', 'START_X': 42533.3, 'START_Y': 0, 'START_Z': -35233.3, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': 0.0, 'NAME': ''}}, {'label': 'prefab_station_science', 'data': {'side_value': 'tsn', 'START_X': 27113.0, 'START_Y': 0, 'START_Z': -36087.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': 0.0, 'NAME': ''}}, {'label': 'prefab_terrain_asteroid_polyline', 'data': {'points': [(0.0, 0.0), (35.0, 31.25), (71.5, 18.0), (112.5, -2.75), (122.0, -43.75), (117.0, -72.25)], 'START_X': 117.0, 'START_Y': 0, 'START_Z': 72.25, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': 0.0, 'NAME': ''}}]
    for p in map_data:
        prefab_spawn(p['label'], p['data'], OFFSET_X, OFFSET_Z )
