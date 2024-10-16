# Solicitar la distancia y la velocidad al usuario
distancia = float(input("Introduce la distancia a recorrer en km: "))
velocidad = float(input("Introduce la velocidad promedio en km/h: "))

# Calcular el tiempo de viaje en horas
tiempo_total_horas = distancia / velocidad

# Calcular las horas y minutos
horas = int(tiempo_total_horas)
minutos = int((tiempo_total_horas - horas) * 60)

# Mostrar una advertencia si la velocidad es mayor a 120 km/h
if velocidad > 120:
    print("Advertencia: La velocidad es mayor a 120 km/h, ten cuidado.")

# Mostrar el tiempo de viaje
print(f"El tiempo de viaje es de {horas} horas y {minutos} minutos.")
