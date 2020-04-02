from Almacen import Almacen

def menu():
    opc = 0
    print("----------MENU DE PRODUCTO---------------")
    print("1. Crear")
    print("2. Consultar")
    print("3. Editar")
    print("4. Vender")
    print("5. Descuento")
    print("6. Salir")
    opc = input("Seleccione una opcion -----> ")

    return int(opc)

if __name__ == '__main__':
    campeon = Almacen()

    salir = False

    while (salir != True):
        seleccion = 0
        seleccion = menu()
        print("La opción selecciona es: ", seleccion)

        if seleccion == 1:
            campeon.crear_producto()
        elif seleccion == 2:
            campeon.consultar()
        elif seleccion == 3:
            campeon.editar_producto()
        elif seleccion == 4:
            campeon.vender_producto()
        elif seleccion ==  5:
            campeon.vender_producto(True)
        elif seleccion == 6:
            salir = True
        else:
            print("!!! Ops Opcion incorrecta !!!!")
