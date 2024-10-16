# Solicitar al usuario que ingrese una nota numérica
nota = float(input("Ingrese la nota numérica: "))

# Clasificar la nota en una calificación
if 90 <= nota <= 100:
    calificacion = "A"
elif 80 <= nota < 90:
    calificacion = "B"
elif 70 <= nota < 80:
    calificacion = "C"
elif 60 <= nota < 70:
    calificacion = "D"
elif 0 <= nota < 60:
    calificacion = "F"
else:
    calificacion = "Nota fuera del rango permitido."

print(f"La calificación es: {calificacion}")
