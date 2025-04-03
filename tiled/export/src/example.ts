/// <reference types="@mapeditor/tiled-api" />

// ONLY EDIT THE TYPESCRIPT VERSION
class customMapFormat implements ScriptedMapFormat {
  name : string
  extension : string
  static func_defs = []
  static path = []

  constructor() {
    this.name = "Artemis Cosmos"
    this.extension = "py"
  }

  static processLayer(layer: Layer) {
    let name = layer.name.toLowerCase();
    name = name.replace(/ /g, "_");
    customMapFormat.path.push(name);
    if (layer.isGroupLayer) {
      customMapFormat.processGroup(layer as GroupLayer)
    } else if (layer.isObjectLayer) {
      customMapFormat.processObjectGroup(layer as ObjectGroup)
    } else if (layer.isTileLayer) {
      tiled.warn("Tile layers are not process", undefined)
    } else if (layer.isImageLayer) {
      tiled.warn("Image layers are not process", undefined)
    }
    customMapFormat.path.pop()
  }

  static processObjectGroup(objs: ObjectGroup) {
    let name = customMapFormat.path.join("_")
    

    let indent = "    ";
    let code = `def ${name}(START_X=0, START_Z=0):`;
    code += `\n${indent}map_data = `
    let code_objects = []
    for (const obj of objs.objects) {
      let data = customMapFormat.processObject(obj);
      code_objects.push(data)
    }
    if (code_objects.length >0) {
      let j = JSON.stringify(code_objects);
      j = j.replace(/:true/g, ":True")
      j = j.replace(/:false/g, ":False")
      code += `${j}`
      code += `\n${indent}prefab_spawn(map_data, START_X, START_Z)`
      customMapFormat.func_defs.push(code)
    }
  }

  static processObject(obj: MapObject) {
    ///
    /// AND this is were we stop
    /// This does NOT get the template's type/className properly
    ///
    let cls = obj.className
    cls = obj.type
    
    let start_x = obj.x
    let start_z = obj.y
    let size_x = obj.width
    let size_z = obj.height
    let name = obj.name

    let label = cls // This is Incomplete due to bug in Tiled
    let data = Object()
    data.START_X = start_x
    data.START_Y = 0 // Check properties
    data.START_Z = start_z

    data.SIZE_X = size_x
    data.SIZE_Y = 0 // Check properties
    data.SIZE_Z = size_z
    data.NAME = name
    // Need to then 


    tiled.log(`\tobject type:  ${cls} name: ${name}`)

    for (let k in obj.resolvedProperties()) {
      let v = obj.resolvedProperty(k);
      data[k] = v
      //tiled.log(`\t\tproperty: ${k} ${v}`)
    }

    return {"label": label, "data": data}
    
  }

  static processGroup(group: GroupLayer) {
      tiled.log(`layer ${group.name}`)
      for (const l  of group.layers) {
        customMapFormat.processLayer(l)
      }
  }
  //write?(map: TileMap, fileName: string): string | undefined;
  write(p_map: TileMap, p_fileName: string) :  string | undefined {
    tiled.log(`Exporting ${p_fileName}`);
    tiled.log(`${this}`);

    for (let layer of p_map.layers) {
      customMapFormat.processLayer(layer)
    }
    tiled.log(`Writing: ${p_fileName}`)
    let out = new TextFile(p_fileName, TextFile.WriteOnly)
    out.write(customMapFormat.func_defs.join("\n\n"));
    out.commit();
    
    return ""
  }
  

 
}
let me = new customMapFormat()

tiled.registerMapFormat("cosmos", me);
