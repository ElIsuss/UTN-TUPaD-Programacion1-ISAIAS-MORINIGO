def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}")
    return
nombre = str(input("Dime tu nombre\n")).strip().lower().capitalize()
apellido = str(input("Dime tu apellido\n")).strip().lower().capitalize()
edad = int(input("Dime tu edad\n"))
residencia = str(input("Dime donde vives\n")).strip().lower().capitalize()
informacion_personal(nombre,apellido,edad,residencia)