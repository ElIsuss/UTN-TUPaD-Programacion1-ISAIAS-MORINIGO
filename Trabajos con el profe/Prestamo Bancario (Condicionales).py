nombre_apellido = str(input("Nombre y apellido: "))
cuit = input("Ingrse el CUIL: " )
cuit = cuit.replace("-","").strip()
cuit2 = len(cuit) 
if cuit2 != 11 : 
    print ("cuit invalido")
else :
 ingresos_mensuales = float(input("Ingresos Mensuales: "))
 tiempo_laborar = float(input("Años de trabajo: "))
 historial_crediticio =int(input("Historial crediticio:\n1.Bueno\n2.Regular\n3.Malo\n"))
 if historial_crediticio == 3 :
    historial_crediticio = str("Malo") 
    print("Rechazado")
 elif ingresos_mensuales < 200000 :
    print ("Rechazado")
 elif ingresos_mensuales >= 200000 and tiempo_laborar < 2 : 
    print ("Solo se puede pedir hasta $500.000")
    monto_aprobado = 500000
 elif ingresos_mensuales >= 200000 and tiempo_laborar >= 2 : 
    if historial_crediticio == 2 : 
       historial_crediticio = str("Regular")
       print("Puedes pedir hasta $1.000.000")
       monto_aprobado = 1000000
    elif historial_crediticio == 1 :
       historial_crediticio = str("Bueno")
       print("Puedes pedir hasta $3.000.000")   
       monto_aprobado = 3000000
print(f"Cliente: {nombre_apellido}\nCUIT: {cuit}\nIngresos: {ingresos_mensuales}\nAntigüedad: {tiempo_laborar}\nHistorial: {historial_crediticio}\nMonto Aprobado: {monto_aprobado}")