contactos ={"Contactos" : "Numeros"}
for i in range (2):
    nombre = str(input("Contacto Nuevo: ")).strip().lower().capitalize()
    numero = int(input("Numero del contacto: "))
    contactos[nombre] = numero 

for nombre, numero in contactos.items():
    print(f"{nombre}: {numero}")
    
buscar = str(input("Buscar contacto\n")).strip().lower().capitalize()
if buscar in contactos:
    print(f"El número de {buscar} es: {contactos[buscar]}")
else:
    print("Ese contacto no existe.")