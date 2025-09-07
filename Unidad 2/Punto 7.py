frase = str(input("Dime una frase:"))
largo_frase = len(frase)
if frase[-1].lower() in ("a", "e", "i", "o", "u"):
    print (frase,"!!")
else:
    print (frase)
