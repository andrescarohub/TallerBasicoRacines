# Solicitar los tres ángulos del triángulo al usuario
angulo1 = float(input("Introduce el primer ángulo en grados: "))
angulo2 = float(input("Introduce el segundo ángulo en grados: "))
angulo3 = float(input("Introduce el tercer ángulo en grados: "))

# Verificar que los ángulos suman 180 grados
if angulo1 + angulo2 + angulo3 != 180:
    print("Los ángulos no forman un triángulo válido.")
else:
    # Clasificar el triángulo según sus ángulos
    if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        tipo_triangulo = "Rectángulo"
    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        tipo_triangulo = "Obtuso"
    else:
        tipo_triangulo = "Agudo"

    # Mostrar el tipo de triángulo
    print(f"El triángulo es {tipo_triangulo}.")
