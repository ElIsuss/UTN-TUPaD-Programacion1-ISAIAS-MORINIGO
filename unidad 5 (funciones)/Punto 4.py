
def calcular_Area_circulo(valor_radio):
    area = 3,1415 * valor_radio * valor_radio
    return area
def calcualr_perimetro_circulo(valor_radio):
    perimetro = 2 * 3.1415 * valor_radio
    return perimetro
radio = float(input("Dime el radio de un circulo\n"))
print("El perimetro del circulo es de: ",calcualr_perimetro_circulo(radio))
print(f"El área del círculo es de: {calcular_Area_circulo(radio)}")
