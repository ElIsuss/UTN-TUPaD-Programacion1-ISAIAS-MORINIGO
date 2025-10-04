def celcius_a_fahrenheit(celcius):
    fahrenheit  = celcius  * 1.8 + 32
    return fahrenheit
celcius = float(input("Dime la temperatura:\n"))
print (f"La temperatura en fahrenheit es de {celcius_a_fahrenheit(celcius)}")