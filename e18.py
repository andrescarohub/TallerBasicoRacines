# Solicitar el número de materias cursadas
num_materias = int(input("Introduce el número de materias cursadas: "))

# Inicializar el contador de créditos
creditos_totales = 0

# Iterar sobre cada materia
for i in range(num_materias):
    # Solicitar el puntaje de cada materia
    puntaje = float(input(f"Introduce el puntaje obtenido en la materia {i + 1}: "))
    
    # Evaluar si la materia está aprobada o no
    if puntaje >= 60:
        # Cada materia aprobada otorga 3 créditos
        creditos_totales += 3

# Mostrar el número total de créditos
print(f"El número total de créditos obtenidos es: {creditos_totales}")
