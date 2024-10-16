import random 

# Lista de palabras para adivinar
palabras = ["python", "java", "csharp", "javascript", "ruby"]

# Elegir una palabra aleatoria
palabra_secreta = random.choice(palabras)
intentos = 3

# Bucle para permitir intentos
while intentos > 0:
    adivinanza = input("Adivina la palabra (tienes 3 intentos): ").lower()
    if adivinanza == palabra_secreta:
        print("¡Correcto! Has adivinado la palabra.")
        break
    else:
        intentos -= 1
        print(f"Incorrecto. Te quedan {intentos} intentos.")

if intentos == 0:
    print(f"Lo siento, la palabra era: {palabra_secreta}.")
