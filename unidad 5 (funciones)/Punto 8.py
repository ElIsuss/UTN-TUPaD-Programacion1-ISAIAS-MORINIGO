def indice_de_masa_corporal (peso, altura):
    imc = peso/altura
    return imc
peso_corporal = float(input("Dime tu peso(en kilogramos)\n"))
altura = float(input("Dime tu altura(en centimetros)\n"))
altura = altura/100
print(f"Tu indice de masa corporal es de {indice_de_masa_corporal(peso_corporal,altura)}")