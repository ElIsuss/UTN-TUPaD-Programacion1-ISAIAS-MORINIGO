original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción",
    "Perú": "Lima",
    "Bolivia": "La Paz",
    "Ecuador": "Quito",
    "Colombia": "Bogotá",
    "Venezuela": "Caracas",
    "México": "Ciudad de México",
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma",
    "Alemania": "Berlín",
    "Reino Unido": "Londres",
    "Japón": "Tokio",
    "China": "Pekín",
    "Australia": "Canberra",
    "Canadá": "Ottawa"
}

invertido = {capital: pais for pais, capital in original.items()}

print("Diccionario invertido:\n")
for capital, pais in invertido.items():
    print(f"{capital}: {pais}")
