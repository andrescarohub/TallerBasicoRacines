# Solicitar el peso y la altura al usuario
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

# Calcular el IMC
imc = peso / (altura ** 2)

# Mostrar el IMC
print(f"Tu IMC es: {imc:.2f}")

# Clasificar el estado de peso
if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc <= 24.9:
    clasificacion = "Peso normal"
elif 25 <= imc <= 29.9:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

# Mostrar la clasificación del IMC
print(f"Tu clasificación es: {clasificacion}")
