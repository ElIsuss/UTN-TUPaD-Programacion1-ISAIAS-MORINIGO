nombre = str(input("Dime tu nombre: "))
condicion = int(input("Elige una opcion:\n1.MAYUSCULAS\n2.minusculas\n3.Primera letra mayuscula\n..."))
if condicion == 1:
    nombre = nombre.upper()
if condicion == 2:
    nombre = nombre.lower()
if condicion == 3: 
    nombre = nombre.title()
print("Resultado:", nombre)