# Solicitar la calificación del estudiante
calificacion = float(input("Introduce la calificación del estudiante (0-100): "))

# Preguntar si hizo tareas adicionales
tareas_adicionales = input("¿El estudiante hizo tareas adicionales? (sí/no): ").lower()

# Si hizo tareas adicionales, añadir un 5% extra
if tareas_adicionales == "sí":
    calificacion += calificacion * 0.05

# Asegurarse de que la calificación no exceda 100
if calificacion > 100:
    calificacion = 100

# Mostrar la calificación final
print(f"La calificación final del estudiante es: {calificacion:.2f}")
