def seg_a_hrs(segundos):
    horas = segundos/3600
    return horas
segundos = int(input("Dime una cantidad de segundos y la paso a horas\n"))
print(f"La cantidad de horas seria de {seg_a_hrs(segundos)}")