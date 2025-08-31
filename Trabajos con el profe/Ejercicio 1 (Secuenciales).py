parciales1 = float(input("Nota del primer parcial: "))
parciales2 = float(input("Nota del segundo parcial: "))
parciales3 = float(input("Nota del tercer parcial: "))
examen_final = float(input("Nota del Examen Final: "))
trabajo_final = float(input("Nota del Trabajo Final: "))
calificacion = parciales1 + parciales2 + parciales3 + examen_final + trabajo_final 
calificacion = calificacion / 5 
print ("Su calificacion final es de: ", calificacion)