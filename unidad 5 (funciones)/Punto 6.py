def tabla_multiplicar(num_multiplicar,tabla):
    print(f"{num_multiplicar} * {tabla} = {num_multiplicar * tabla}")
    return
num = int(input("Dime un numero y te dire su tabla de multiplicar\n"))
for i in range(11):
    tabla_multiplicar(num,i)
    