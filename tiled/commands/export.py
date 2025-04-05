import xml.etree.ElementTree as ET
from io import StringIO
import sys


def process_group(group, prefix):
    group_name = group.attrib.get("name","")
    if prefix=="" or prefix is None:
        sub_prefix = group_name
    else:
        sub_prefix = f"{prefix}_{group_name}"

    ret = []

    for child in group:
        if child.tag =="group":
            ret.extend(process_group(child, sub_prefix))
        elif child.tag =="objectgroup":
            ret.extend(process_object_group(child, sub_prefix))
        else:
            print("Error Groups can only contain ")

    # return a list for function code strings
    return ret

def get_custom_properties(node):
    props = {}
    for child in node:
        if child.tag == "properties":
            for p in child:
                if p.tag == "property":
                    name = p.attrib.get("name")
                    if name is None:
                        continue
                    value = p.get("value")
                    t = p.get("type", None)
                    if t == "float":
                        props[name] = float(value)
                    elif t == "int":
                        props[name] = int(value)
                    elif t == "bool":
                        props[name] = value == "true"
                    # file
                    elif t == "file":
                        props[name] = value
                    # link to an object
                    elif t == "object":
                        props[name] = int(value)
                    elif t == "color":
                        props[name] = value
                    else:
                        props[name] = value

    return props    

def process_object_group(group, prefix):
    # Object_groups are the place that create functions
    # 
    ret = []
    objs = []
    group_name = group.attrib.get("name","")
    func_name = f"{group_name}".lower().replace(" ", "_")
    if prefix is not None:
        func_name = f"{prefix}_{group_name}".lower().replace(" ", "_")
    
    for child in group:
        if child.tag =="objectgroup":
            ret.extend(process_object_group(child, func_name))
        if child.tag =="object":
            o = process_object(child)
            if o is not None:
                objs.append(o)
    
    if len(objs)>0:
        stream = StringIO()
        stream.write(f"def {func_name}(OFFSET_X={OFFSET_X}, OFFSET_Z={OFFSET_Y}):\n")
        stream.write(f"    map_data = {objs}\n")
        stream.write(f"    for p in map_data:\n")
        stream.write(f"        prefab_spawn(p['label'], p['data'], OFFSET_X, OFFSET_Z )\n")

        ret.append(stream.getvalue())

    return ret

def process_object(ob):
    x = float(ob.attrib.get("x",0))
    x *= 100
    y = float(ob.attrib.get("y",0))
    y *= 100
    w = float(ob.attrib.get("width",0))
    w *= 100
    h = float(ob.attrib.get("height",0))
    h *= 100
    name = ob.attrib.get("name")
    template = ob.attrib.get("template")
    label = ob.attrib.get("type")
    props = get_custom_properties(ob)
    

    for child in ob:
        if child.tag =="polyline" or child.tag =="polygon":
            s_points = child.get("points")
            points = []
            pairs = s_points.split()
            

            for pair in pairs:
                coords = pair.split(',')
                px = float(coords[0]) *100
                # Flip Z
                py = -float(coords[1]) * 100 
                points.append((px, py))

            props["points"] = points
            if child.tag =="polygon":
                props["is_polygon"] = True
            else:
                props["is_polyline"] = True

            continue
        if child.tag =="point":
            props["is_point"] = True
            continue
        if child.tag =="ellipse":
            props["is_ellipse"] = True
            continue

    
    # pytmx does not properly support templates
    # which sucks
    # luckly its a simple file
    prefab = label
    if template is not None:
        # Parse the XML file
        tree = ET.parse(template)
        root = tree.getroot()
        for child in root:
            if child.tag == "object":
                #merged =  child.attrib | ob.attrib
                if name is None or name == "":
                    name = child.attrib.get("name")
                if prefab is None or prefab == "":
                    prefab = child.attrib.get("type")
            temp_props = get_custom_properties(child)
        props = temp_props | props
        


    #
    #
    #
    start_y = props.get("START_Y", 0)
    size_y = props.get("size_Y", 0)
    props["START_X"] = x
    props["START_Y"] = start_y
    props["START_Z"] = -y
    props["SIZE_X"] = w
    props["SIZE_Y"] = size_y
    #
    # Z-is flipped in engine
    # The best way to express this is
    # also negating SIZE_Z
    # Math usually works, if not the 
    # library code maybe should be updated
    # - SIZE_Z also tells other code it is from the map
    #
    props["SIZE_Z"] = -h
    props["NAME"] = name

    if prefab is not None:
        return  {"label": prefab, "data": props}
    

OFFSET_X = 0
OFFSET_Y = 0
def process_map(map_file):
    tree = ET.parse(map_file)
    map_out = map_file.replace(".tmx", ".py")

    map_data = ["from sbs_utils.procedural.prefab import prefab_spawn\n\n"]
    for child in tree.getroot():
        if child.tag =="group":
            map_data.extend(process_group(child, None))
        elif child.tag =="objectgroup":
            map_data.extend(process_object_group(child, None))

    with open(map_out, "w") as stream:
        for s in map_data:
            stream.writelines(s)
            print(s)

import json
def process_world(map_file):
    global OFFSET_X
    global OFFSET_Y

    try:
        with open(map_file, 'r') as file:
            data = json.load(file)
            maps = data.get("maps", [])
            for map in maps:
                file_name = map.get("fileName")
                if file_name is None:
                    continue
                OFFSET_X = map.get("x", 0)
                OFFSET_Y = map.get("y", 0)
                process_map(file_name)

    except Exception as e:
         print(f"An unexpected error occurred: {e}")
         return None




if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        map_file = sys.argv[1]
    else:
        print("No map specified")
        sys.exit()

    if map_file.endswith("world"):
        process_world(map_file)
        sys.exit()
    else:
        process_map(map_file)
        sys.exit()
    

    



