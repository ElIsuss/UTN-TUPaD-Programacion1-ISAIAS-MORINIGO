def saludo(nombre):
    print("Hola ",nombre," como te va?")
    return
nombre = str(input("Dime tu nombre\n"))
nombre = nombre.strip().lower().capitalize()
saludo(nombre)