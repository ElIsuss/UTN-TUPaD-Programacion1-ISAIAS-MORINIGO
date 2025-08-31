distancia = float(input("Introduzca la distancia del viaje: "))
precio_gasolina = float(input("Introduzca el precio de la gasolina: "))
gasolina_usada = (distancia * 8)/100 
print ("La gasolina que se necesita para hacer ese viaje es de:", gasolina_usada)
print ("El precio por la gasolina a usar es de:", gasolina_usada * precio_gasolina)
tiempo_estimado = distancia / 90 
print ("El tiempo estimado es de: ", tiempo_estimado, "hrs")