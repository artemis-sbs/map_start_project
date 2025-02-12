/// <reference types="@mapeditor/tiled-api" />

// ONLY EDIT THE TYPESCRIPT VERSION
class customMapFormat implements ScriptedMapFormat {
  name : string
  extension : string
  constructor() {
    this.name = "Artemis Cosmos"
    this.extension = "py"
  }

  static processLayer(layer: Layer) {
    if (layer.isGroupLayer) {
      customMapFormat.processGroup(layer as GroupLayer)
    } else if (layer.isObjectLayer) {
      customMapFormat.processObjectGroup(layer as ObjectGroup)
    } else if (layer.isTileLayer) {
      tiled.warn("Tile layers are not process", undefined)
    } else if (layer.isImageLayer) {
      tiled.warn("Image layers are not process", undefined)
    }
  }

  static processObjectGroup(objs: ObjectGroup) {
    for (const obj of objs.objects) {
      customMapFormat.processObject(obj);
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

    tiled.log(`\tobject type:  ${cls} name: ${name}`)

    for (let k in obj.resolvedProperties()) {
      let v = obj.resolvedProperty(k);
      tiled.log(`\t\tproperty: ${k} ${v}`)

    }
    
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
      
      // Replace special characters for an underscore

      
      
    }
    return ""

  }

 
}
let me = new customMapFormat()

tiled.registerMapFormat("cosmos", me);
