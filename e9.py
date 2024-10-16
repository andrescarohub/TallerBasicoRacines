# Solicitar al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))

# Clasificar la edad en categorías
if edad < 0:
    print("Le falta tiempo por nacer.")
elif 0 <= edad <= 12:
    print("Es un niño.")
elif 13 <= edad <= 17:
    print("Es un adolescente.")
elif 18 <= edad <= 64:
    print("Es un adulto.")
else:
    print("Es un anciano.")
