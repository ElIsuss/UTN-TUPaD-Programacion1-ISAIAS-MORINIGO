contrasenha = input("Dime una constraseña: ")
contrasenha_aux = contrasenha.replace(" ","")
print(contrasenha_aux)
longitud = len(contrasenha_aux)
if longitud > 8 and longitud < 14:
    print("Contraseña registrada correctamente")
else:
    print("Por favor, Introduzca una contraseña de entre 8 y 14 caracteres")