# Solicitar una calificación numérica al usuario
calificacion = float(input("Introduce la calificación numérica (0-100): "))

# Usar match para convertir la calificación a una letra
match calificacion:
    case _ if 90 <= calificacion <= 100:
        letra = "A"
    case _ if 80 <= calificacion < 90:
        letra = "B"
    case _ if 70 <= calificacion < 80:
        letra = "C"
    case _ if 60 <= calificacion < 70:
        letra = "D"
    case _ if 0 <= calificacion < 60:
        letra = "F"
    case _:
        letra = "Calificación fuera del rango permitido."

# Mostrar la calificación en letra
print(f"La calificación en letra es: {letra}")
