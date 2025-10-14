frase = input("Escribí una frase: ")
frase = frase.lower().replace(",", "").replace(".", "")
palabras = frase.split()

palabras_unicas = set(palabras)
print("Palabras únicas:")
for palabra in palabras_unicas:
    print(palabra)

contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

print("Cantidad de veces que aparece cada palabra:")
for palabra, cantidad in contador.items():
    print(f"{palabra}: {cantidad}")
