def a_binario(n):
    if n == 0:
        return ""
    else:
        return a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número decimal: "))
print(f"Binario: {a_binario(num)}")
