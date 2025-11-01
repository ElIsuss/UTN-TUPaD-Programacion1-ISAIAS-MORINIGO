def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
num = int(input("dime un numero: "))
digito = int(input("Ahora un digito: "))
print(contar_digito(num, digito))
