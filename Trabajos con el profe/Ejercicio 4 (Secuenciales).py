monto_solicitado = float(input("Ingrese el monto solicitado: "))
interes = 0.02 
meses = 12
factor = (1 + interes) ** meses
cuota = monto_solicitado * (interes * factor) / (factor - 1)
total = cuota * meses
print(f"\nMonto solicitado: ${monto_solicitado:.2f}")
print(f"Cuota mensual: ${cuota:.2f}")
print(f"Total a devolver: ${total:.2f}")
