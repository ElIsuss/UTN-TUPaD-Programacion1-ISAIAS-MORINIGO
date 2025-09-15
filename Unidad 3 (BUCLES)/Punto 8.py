par = 0
impar = 0
positivos = 0
negativos = 0 
for i in range (100):
    num = int(input("Dime un numero: "))
    if num % 2 == 0:
        par = par + 1
    if num % 2 == 1:
        impar = impar + 1
    if num > 0:
        positivos = positivos + 1
    if  num < 0:
        negativos = negativos + 1 
print ("Numeros par: ", par)
print ("Numero impar: ", impar)
print ("Numeros positivos: ", positivos)
print ("Numeros negativos: ", negativos)