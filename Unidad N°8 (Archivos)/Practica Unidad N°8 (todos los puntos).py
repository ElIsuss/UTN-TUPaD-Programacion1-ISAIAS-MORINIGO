import os

# crear archivo con 3 componentes
with open("componentes.txt", "w", encoding="utf-8") as archivo:
    archivo.write('nombre,precio,cantidad\n')
    archivo.write('Procesador Ryzen 5 5600,95000,5\n')
    archivo.write('Placa madre B550M,82000,3\n')
    archivo.write('Memoria RAM 16GB DDR4,35000,12\n')

# leer y mostrar los componentes
with open("componentes.txt", "r") as archivo:
    next(archivo)

    for linea in archivo:
        linea = linea.strip()
        item, valor, stock = linea.split(",")
        print(f"Componente: {item} | Precio: {valor} | Cantidad: {stock}")

# agregar componentes
with open("componentes.txt", "a") as archivo:
    try:
        nuevo_item = str(input("Nombre del componente que desea agregar: "))
        nuevo_valor = int(input("Precio del componente: "))
        nuevo_stock = int(input("Cantidad del componente: "))
        archivo.write(f'{nuevo_item},{nuevo_valor},{nuevo_stock}\n')
    except ValueError:
        print("ERROR. Valor ingresado incorrecto.")

# cargar componentes en lista de diccionarios
componentes = []
with open("componentes.txt", "r", encoding="utf-8") as archivo:
    next(archivo)  # saltar encabezado

    for linea in archivo:
        linea = linea.strip()
        item, valor, stock = linea.split(",")
        componentes.append({
            "nombre": item,
            "precio": valor,
            "cantidad": stock
        })

# buscar componente por nombre y mostrar sus datos
encontrado = False

with open("componentes.txt", "r", encoding="utf-8") as archivo:
    next(archivo)

    buscar_item = input("Nombre del componente que quiere buscar: ")
    for linea in archivo:
        linea = linea.strip()
        item, valor, stock = linea.split(",")
        if buscar_item.lower() == item.lower():
            print(f"Componente: {item} | Precio: {valor} | Cantidad: {stock}")
            encontrado = True
            break

if not encontrado:
    print(f"El componente '{buscar_item}' no existe en el inventario.")

# guardar componentes actualizados
with open("componentes.txt", "w", encoding="utf-8") as archivo:
    archivo.write("nombre,precio,cantidad\n")
    print("\nComponentes actualizados:\n")
    for comp in componentes:
        archivo.write(f"{comp['nombre']},{comp['precio']},{comp['cantidad']}\n")
        print(f"Componente: {comp['nombre']} | Precio: {comp['precio']} | Cantidad: {comp['cantidad']}")
