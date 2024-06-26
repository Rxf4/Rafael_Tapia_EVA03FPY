import json

def cargar_inventario():
    with open('inventario.json','r') as f:
        return json.load(f)

def guardar_inventario(inventario):
    with open('inventario.json','w') as f:
        json.dump(inventario, f, indent = 4)

def ver_listado_de_pinturas():
    inventario = cargar_inventario()
    for pintura in inventario['pinturas']:
        print(f'codigo: {pintura['codigo']}, tipo:{pintura['tipo']}, nombre:{pintura['nombre']}')


def buscar_pintura(codigo_o_nombre):
    inventario = cargar_inventario()
    for pintura in inventario['pinturas']:
        if pintura['codigo'] == codigo_o_nombre or pintura['nombre'] == codigo_o_nombre:
            print(f'codigo: {pintura['codigo']}, nombre:{pintura['nombre']}, {pintura['descripcion']}, cantidad:{pintura['cantidad']}, stock:{pintura['stock']}')
            return
        
def agregrar_pintura(codigo, nombre,descripcion,cantidad):
    inventario = cargar_inventario()
    nueva_pintura = {'codigo': codigo, 'nombre': nombre, 'descripcion': descripcion, 'cantidad': cantidad}
    inventario['pinturas'].append(nueva_pintura)
    guardar_inventario(inventario)

def eliminar_pintura(codigo):
    inventario = cargar_inventario()
    for pintura in inventario['pinturas']:
        if pintura['codigo'] == codigo:
            inventario['pinturas'].remove(pintura)
            guardar_inventario(inventario)
            print('pintura eliminada')
            return
        print('pintura no encontrada')

def exportar_pinturas():
    inventario = cargar_inventario()
    with open('pinturas.txt','w') as f:
        for pintura in inventario['pinturas']:
            f.write(f'codigo: {pintura['codigo']}, nombre:{pintura['nombre']}, {pintura['descripcion']}, cantidad:{pintura['cantidad']}, stock:{pintura['stock']}')





