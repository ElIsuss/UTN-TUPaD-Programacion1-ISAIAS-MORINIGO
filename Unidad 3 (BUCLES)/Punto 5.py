import random
numero_ia = random.randint(0,9)
intentos = 0
condicion = False
while condicion == False:
    num = int(input("Intenta adivinar el numero entre el 0 y el 9: "))
    if num == numero_ia:
        condicion = True
    else:
        intentos = intentos + 1
print ("Los intentos fueron de: ", intentos)