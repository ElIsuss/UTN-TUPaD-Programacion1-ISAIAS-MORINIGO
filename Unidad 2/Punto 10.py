emisferio = int(input("Dime en cual hemisferio te encuentras:\n1.Norte \n2.Sur \n"))
mes = int(input("Dime el número de mes: "))
dia = int(input("Dime el día: "))

if emisferio in (1, 2):
    if 1 <= mes <= 12 and 1 <= dia <= 31:
        if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and dia <= 20):
            if emisferio == 1:
                print("Invierno")
            elif emisferio == 2:
                print ("Verano")
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and dia <= 20):
            if emisferio == 1:
                print("Primavera")
            elif emisferio == 2:
                print("Otoño")
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and dia <= 20):
            if emisferio == 1:
                print("Verano")
            elif emisferio ==2:
                print("Invierno")
        elif (mes == 9 and dia >= 21) or (10 <= mes <= 12 and dia <= 20):
            if emisferio == 1:
                print ("Otoño")
            elif emisferio ==2:
                print ("Primavera")
    else:
        print("Fecha inexistente")
else:
    print("En qué mundo vivís???")
