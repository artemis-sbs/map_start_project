def test(OFFSET_X=1760, OFFSET_Z=-780):
    map_data = [{'label': 'prefab_station_torgoth', 'data': {'side_value': 'raider', 'START_X': 42533.3, 'START_Y': 0, 'START_Z': -35233.3, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': 0.0, 'NAME': ''}}, {'label': 'prefab_station_science', 'data': {'side_value': 'tsn', 'START_X': 27113.0, 'START_Y': 0, 'START_Z': -36087.0, 'SIZE_X': 0.0, 'SIZE_Y': 0, 'SIZE_Z': 0.0, 'NAME': ''}}]
    for p in map_data:
        prefab_spawn(p['label'], p['data'], OFFSET_X, OFFSET_Z )
