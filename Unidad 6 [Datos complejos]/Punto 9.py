agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Gimnasio"
}
try:
  dia = str(input("Ingresá el día: ")).lower().strip()
except ValueError:
    print("Dia inexistente....")

hora =(input("Ingresá la hora (ej: 10:00): ")).strip()


clave = (dia, hora)

if clave in agenda:
    print(f"Actividad: {agenda[clave]}")
else:
    print("No hay actividad en ese día y hora.")
