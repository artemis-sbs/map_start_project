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

                    props[name] = value

    return props    

def process_object_group(group, prefix):
    # Object_groups are the place that create functions
    # 
    ret = []
    objs = []
    group_name = group.attrib.get("name","")
    func_name = f"{prefix}_{group_name}".lower().replace(" ", "_")
    
    for child in group:
        if child.tag =="objectgroup":
            ret.extend(process_object_group(child, func_name))
        if child.tag =="object":
            objs.append(process_object(child))
    
    if len(objs)>0:
        stream = StringIO()
        stream.write(f"def {func_name}(OFFSET_X=0, OFFSET_Z=0):\n")
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
    name = ob.attrib.get("name","")
    template = ob.attrib.get("template")
    label = ob.attrib.get("type")
    props = get_custom_properties(ob)
    
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
                prefab = child.get("type")
                merged =  child.attrib | ob.attrib
                print(merged)
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
    props["SIZE_Z"] = h
    props["NAME"] = name

    if prefab is not None:
        return  {"label": prefab, "data": props}
    

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        map_file = sys.argv[1]
    else:
        print("No map specified")
        sys.exit()
    
    tree = ET.parse(map_file)
    map_out = map_file.replace(".tmx", ".py")


    map_data = []
    for child in tree.getroot():
        if child.tag =="group":
            map_data.extend(process_group(child, None))

    with open(map_out, "w") as stream:
        for s in map_data:
            stream.writelines(s)
            print(s)





