productos = {"Stock":"Valor"}
opcion = 999
while opcion != 0:
    print('''
1. Consultar Stock
2. Agregar Producto a stock
3. Agregar nuevo producto
4. Salir''')
    try:
     opcion = int(input("Elija una opcion\n"))
    except ValueError:
        print("Ocurrio un Error....")
    if opcion == 1: 
          print("Stock actual:")
          for productos, cantidad in productos.items():
             print(f"{productos}: {cantidad}")
    if opcion == 2:
        buscar = str(input("¿Qué producto vas a modificar? ")).strip()
        if buscar in productos:
            try:
                cantidad = int(input("¿Cuánto producto vas a agregar? "))
                productos[buscar] += cantidad
                print("Stock actualizado correctamente.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")
        else:
            print("Error: Ese producto no existe en el stock.")

    if opcion == 3:
        nuevo = str(input("Producto nuevo:\n"))
        if nuevo in productos:
            print("Producto ya existente")
        else:
            cantidad_nuevo_producto = int(input("Cuantos productos va añadir?\n"))
            productos[nuevo] = cantidad_nuevo_producto
    if opcion == 4:
        print("Saliendo del programa...")
        break    