def promedio (a, b, c):
    promedio_numeros = (a + b + c)/3
    return promedio_numeros
promedio1 = float(input("Dime un numero\n"))
promedio2 = float(input("Dime un numero\n"))
promedio3 = float(input("Dime un numero\n"))
print(f"El promedio de esos 3 numeros es de: {promedio(promedio1,promedio2,promedio3)}")