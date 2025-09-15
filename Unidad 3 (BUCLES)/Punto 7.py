numero = int(input("Dime un numero entero poitivo: "))
suma = 0
if  numero > 0:
    for i in range(numero + 1):
        suma = suma + i
else:
    print("Entero Positivo dije")
print ("El resultado es de: ", suma)
