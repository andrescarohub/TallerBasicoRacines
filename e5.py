# Solicitar al usuario un número del 1 al 7
numero = int(input("Inserte un número del 1 al 7: "))

# Usar match para determinar el día de la semana
match numero:
    case 1:
        dia = "Lunes"
    case 2:
        dia = "Martes"
    case 3:
        dia = "Miércoles"
    case 4:
        dia = "Jueves"
    case 5:
        dia = "Viernes"
    case 6:
        dia = "Sábado"
    case 7:
        dia = "Domingo"
    case _:
        dia = "Introduce un número. Debe ser del 1 al 7."

if numero < 1 or numero > 7:
    print("El valor es inválido.")
else:
    print(f"Hoy es {dia}.")
