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

def main():
    while True:
        print("Opciones:")
        print("1. Ver Listado de Pinturas")
        print("2. Buscar Pintura")
        print("3. Agregar Pintura")
        print("4. Eliminar Pintura")
        print("5. Exportar Pinturas")
        print("6. Salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            ver_listado_de_pinturas()
        elif opcion == "2":
            codigo_o_nombre = input("Ingrese el código o nombre de la pintura: ")
            buscar_pintura(codigo_o_nombre)
        elif opcion == "3":
            codigo = input("Ingrese el código de la pintura: ")
            nombre = input("Ingrese el nombre de la pintura: ")
            descripcion = input("Ingrese la descripción de la pintura: ")
            cantidad = int(input("Ingrese la cantidad de la pintura: "))
            agregar_pintura(codigo, nombre, descripcion, cantidad)
        elif opcion == "4":
            codigo = input("Ingrese el código de la pintura: ")
            eliminar_pintura(codigo)
        elif opcion == "5":
            exportar_pinturas()
        elif opcion == "6":
            print("Adiós!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()





