# Solicitar al usuario que ingrese la temperatura y la escala
temperatura = float(input("Ingrese la temperatura: "))
escala = input("Ingrese la escala (C para Celsius, F para Fahrenheit): ").upper()

# Convertir la temperatura según la escala proporcionada
match escala:
    case 'C':
        # Convertir de Celsius a Fahrenheit
        temperatura_fahrenheit = (temperatura * 9/5) + 32
        print(f"{temperatura} grados Celsius son {temperatura_fahrenheit:.2f} grados Fahrenheit.")
    case 'F':
        # Convertir de Fahrenheit a Celsius
        temperatura_celsius = (temperatura - 32) * 5/9
        print(f"{temperatura} grados Fahrenheit son {temperatura_celsius:.2f} grados Celsius.")
    case _:
        print("Escala no válida. Por favor, ingrese 'C' para Celsius o 'F' para Fahrenheit.")
