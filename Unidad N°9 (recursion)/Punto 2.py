def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input("Ingrese hasta qué posición mostrar la serie: "))
for i in range(pos):
    print(fibonacci(i), end=" ")
