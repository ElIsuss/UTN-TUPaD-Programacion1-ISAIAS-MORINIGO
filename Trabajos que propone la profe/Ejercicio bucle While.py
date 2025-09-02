import random
print("---------------------Piedra, Papel o Tijeras---------------------")
salir = 3
while salir < 4:
    decicion = int(input("Elige una opcion:\n 1.Piedra \n 2.Papel \n 3.Tijeras\n 4.salir\n"))
    decicion_Ia = random.randint (1,3)
    if decicion != decicion_Ia :
        if decicion == 1 and decicion_Ia ==2:
            print ("---Perdiste---")
        elif decicion == 1 and decicion_Ia == 3:
            print ("---Ganaste---")
        if decicion == 2 and decicion_Ia == 3:
            print ("---Perdiste---")
        elif decicion == 2 and decicion_Ia == 1:
            print ("---Ganaste---")
        if decicion == 3 and decicion_Ia == 1:
            print ("---Perdiste---")
        elif decicion == 3 and decicion_Ia == 2:
            print ("---Ganaste---")    
        if decicion == 4:
            print ("Saliendo del juego...")
            salir = 4
    else:
        print ("---Empate---")
 
        