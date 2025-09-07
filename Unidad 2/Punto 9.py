magnitud = float(input("Dime la magnitud del temblor/terremoto: "))
if magnitud < 3:
    print("El temblor fue impercitible")
if magnitud >= 3 and magnitud < 4:
    print("Ligeramente perseptible")
if magnitud >= 4 and magnitud < 5:
    print ("Moderado")
if magnitud >= 5 and magnitud < 6:
    print ("Fuerte")
if magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
if magnitud >= 7:
    print("Extremo")