class Almacen:
    nombre= ''
    precio= 0
    costo= 0
    sku= 0
    bodega= ""
    cantidad = 0
    inventario = []

    def crear_producto(self):
        """Metodo principal para crear un producto"""
        print("-------------Creando Producto----------------------")
        self.nombre = input("Nombre: ")
        self.precio = input("Precio de venta: ")
        self.costo = input("Costo: ")
        self.sku = input("Codigo del producto (SKU): ")
        self.bodega = input("Nombre de la bodega: ")
        self.cantidad = input("Cantidad a estar disponibles: ")

        producto = { 'nombre': self.nombre, 'precio': self.precio, 'sku': self.sku,
                     'costo': self.costo,  'bodega': self.bodega, 'cantidad': self.cantidad
                   }
        self.inventario.append(producto)
        print("Producto creado con Exito :) \n\n")

    def consultar(self):
        """Metodo para consultar un producto del almacen"""
        print("-------------Buscando Producto----------------------")
        id =  input("Ingrese el SKU o nombre del producto: ")

        for x in self.inventario:
            if x['sku'] == id or x['nombre'] == id:
                print("Producto....")
                print(x)

    def editar_producto(self):
        print("-------------Editar Producto----------------------")
        id =  input("Ingrese el SKU o nombre del producto: ")
        producto = self.buscar(id)

        if producto and producto['nombre'] != '':
            print("Modificando el producto ", producto['nombre'])

            for clave, valor in producto.items():
                respuesta = input("Deseas Cambiar el "+clave+ " Si (1)/ No (0)")

                if respuesta == "1" and clave == "nombre":
                    producto[clave] = input("Ingrese el nuevo "+ clave)
                    break


        else:
            print("El producto que esta buscando no existe.")

    def vender_producto(self, descuento = None):
        print("-------------Venta de Producto----------------------")
        id =  input("Ingrese el SKU o nombre del producto: ")
        producto = self.buscar(id)
        if producto and producto['nombre'] != '':
            print("Disponible ", producto['cantidad'])
            cant  = int(input("Ingrese la cantidad a comprar: "))

            producto['cantidad'] = int(producto['cantidad'])

            if cant <= producto['cantidad']:
                
                producto['cantidad'] -= cant

                total = float(producto['precio']) * cant

                
                calculo_descuento = 0

                if descuento != None:
                    print("Aplicando descuento")
                   
                    calculo_descuento = total * self.descuento(cant)

                    total = total - calculo_descuento
                    print("Descuento del: ", calculo_descuento)
                    print("Total a pagar con descuento es: ", total)
                else:
                    print("Total a pagar es: ", total)

                print("Compras exitosa")
            else:
                print("Cantidad a comprar superar el limite disponible >(")
        else:
            print("Producto no encontrado")

    def descuento(self, cant_comprada):
        cant_comprada = int(cant_comprada)
        descuento = 0
        if cant_comprada >= 3:
            descuento = 0.65
        elif cant_comprada >= 2:
            descuento = 0.55
        elif cant_comprada >= 1:
            descuento = 0.50
        else:
            descuento = 0
        return descuento

    def buscar(self, id):
        for x in self.inventario:
            if x['sku'] == id or x['nombre'] == id:
                return  x
