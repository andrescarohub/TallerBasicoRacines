import random

# Generar un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)

# Bucle para permitir múltiples intentos
while True:
    # Pedir al usuario que ingrese un número
    intento = int(input("Adivina el número entre 1 y 10: "))
    # Comparar el número ingresado con el número aleatorio
    if intento < numero_aleatorio:
        print("El número es mayor.")
    elif intento > numero_aleatorio:
        print("El número es menor.")
    else:
        print(f"¡Correcto! El número era {numero_aleatorio}.")
        break  # Salir del bucle cuando adivina correctamente

