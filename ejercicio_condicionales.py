#separo la fecha para pode validarla
print ("--------------Instituto del ingles--------------")
fecha = input("ingrese la fecha en formato dia, DD/MM: ")
dia, fecha = fecha.split (",")
dd, mm = fecha.split("/")
dia = str(dia)
dd = int(dd)
mm = int(mm)
#valido dias y meses
if mm <= 12 and mm >= 1 :
    if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12 : 
     if dd < 31 and dd >= 1:
        print ("Hoy es: ",dia, "del ", dd,"/",mm  )
    if mm == 2 :
     if  dd <=28 and dd >=1: 
        print ("Hoy es: ",dia, "del ", dd,"/ febrero"  )     
    if mm == 4 or mm == 6 or mm == 9 or mm == 11:
     if dd >=1 and dd <= 31:
        print ("Hoy es: ",dia, "del ", dd,"/",mm  )
else: 
    print("fecha inexistente")
#analizamos los dias

if dia == "lunes": 
    print("------------Nivel Inicial------------")
    confirmacion = int(input("Hoy se tomaron examenes? (1.SI / 2.NO) "))
    if confirmacion == 1 :
        aprobados = int(input("Cuantos alumnos aprobaron? "))
        desaprobaron = int(input("Cuanotos alumnos desaprobaron?"))
        total_alumnos= aprobados + desaprobaron
        porcentaje_aprobados = (aprobados / total_alumnos)*100
        porcentaje_aprobados = round(porcentaje_aprobados)
        print("El ", porcentaje_aprobados, " % ", " aprobaron")
        
if dia == "martes": 
    print("------------Nivel Intermedio------------")
    confirmacion = int(input("Hoy se tomaron examenes? (1.SI / 2.NO) "))
    if confirmacion == 1 :
        aprobados = int(input("Cuantos alumnos aprobaron? "))
        desaprobaron = int(input("Cuanotos alumnos desaprobaron?"))
        total_alumnos= aprobados + desaprobaron
        porcentaje_aprobados = (aprobados / total_alumnos)*100
        porcentaje_aprobados = round(porcentaje_aprobados)
        print("El ", porcentaje_aprobados, " % ", " aprobaron")
        
if dia == "miercoles": 
    print("------------Nivel Avanzado------------")
    confirmacion = int(input("Hoy se tomaron examenes? (1.SI / 2.NO) "))
    if confirmacion == 1 :
        aprobados = int(input("Cuantos alumnos aprobaron? "))
        desaprobaron = int(input("Cuanotos alumnos desaprobaron?"))
        total_alumnos= aprobados + desaprobaron
        porcentaje_aprobados = (aprobados / total_alumnos)*100
        porcentaje_aprobados = round(porcentaje_aprobados)
        print("El ", porcentaje_aprobados, " % ", " aprobaron")
if dia  == "jueves":
    print("------------Practica Hablada------------") 
    total_alumnos = int(input("Cuantos alumnos hay en su clase? "))
    asistencia = int(input("Cuantos alumnos asistieron hoy?"))
    total_asistencia = (asistencia / total_alumnos)*100
    if total_asistencia >= 50 :
        print("Asistio la mayoria de alumnos")
    else:
        print("No asistio la mayoria de alumnos")
if dia == "viernes" and dd == 1 and (mm == 1 or mm == 7): 
    print("------------Ingles para Viajeros------------")
    print("Inicio de nuevo ciclo")
    num_alumnos = int(input("Cuantos alumnos comiezan este nuevo ciclo?"))
    arrancel = 50000
    print("El total de ingreso este neuvo ciclo es de: ", num_alumnos * arrancel)
else: 
    print("Bienvenidos al Ingles para Viajeros")