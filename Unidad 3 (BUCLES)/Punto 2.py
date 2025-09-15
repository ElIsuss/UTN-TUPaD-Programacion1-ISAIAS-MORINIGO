num = float(input("Dime un numero "))
digitos = 0 
while num > 1:
    num = num / 10 
    digitos = digitos + 1 
print ("El numero de digitos que contiene es de: ", digitos)